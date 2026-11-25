#!/usr/bin/env bash
# Called by import-repository-snapshot.ps1 with Git for Windows' Bash.
set -euo pipefail
if [[ ${OSTYPE:-} == msys* ]]; then export PATH="/usr/bin:$PATH"; fi

fail() { printf 'Snapshot import: %s\n' "$*" >&2; exit 1; }

[[ $# == 3 ]] || fail 'Expected source, branch and destination.'
source_repo=$1
branch=$2
destination=${3%/}
manifest=NEXUS_BACKUP_MANIFEST.md
[[ -n $source_repo && $source_repo != *$'\n'* && $source_repo != *$'\r'* ]] ||
    fail 'Choose a source on a single line.'
[[ -n $branch ]] || fail 'Choose a branch.'
[[ $destination =~ ^repositories/([a-zA-Z0-9._-]+/)*[a-zA-Z0-9._-]+$ ]] ||
    fail 'Choose a destination inside repositories/ using letters, digits, dots, underscores or hyphens.'
IFS=/ read -r -a components <<< "$destination"
for component in "${components[@]}"; do
    case "${component,,}" in
        *.|.git|con|con.*|prn|prn.*|aux|aux.*|nul|nul.*|com[1-9]|com[1-9].*|lpt[1-9]|lpt[1-9].*)
            fail "Unsafe destination component: $component" ;;
    esac
done

unset GIT_DIR GIT_WORK_TREE GIT_COMMON_DIR GIT_INDEX_FILE GIT_OBJECT_DIRECTORY GIT_ALTERNATE_OBJECT_DIRECTORIES
root=$(git rev-parse --show-toplevel) || fail 'Run from inside the receiving Git clone.'
target="$root/$destination"
temporary=''
created_dirs=()
cleanup() {
    if [[ -n $temporary ]]; then rm -rf -- "$temporary"; fi
    # Only remove empty parents created by this run, including after a failed clone.
    for ((i=${#created_dirs[@]}-1; i>=0; i--)); do
        rmdir -- "${created_dirs[i]}" 2>/dev/null || :
    done
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

parent=$root
for ((i=0; i<${#components[@]}-1; i++)); do
    parent="$parent/${components[i]}"
    [[ ! -L $parent ]] || fail "Destination crosses a filesystem link: $parent"
    if [[ ! -d $parent ]]; then
        if mkdir -- "$parent"; then
            created_dirs+=("$parent")
        elif [[ ! -d $parent || -L $parent ]]; then
            fail "Cannot create destination directory: $parent"
        fi
    fi
done
[[ ! -e $target && ! -L $target ]] || fail "Destination already exists: $destination"
temporary=$(mktemp -d -- "$parent/.nexus-snapshot.XXXXXXXX")
tree="$temporary/tree"
snapshot_git() {
    git -c core.hooksPath="$temporary/empty-hooks" -c core.fsmonitor=false -c core.longpaths=true \
        -c core.sparseCheckout=false -c core.protectNTFS=true -c core.protectHFS=true "$@"
}
# Limit the clone's transports even after Git applies URL rewrites. Honor an
# existing protocol allowlist, or the user's per-protocol and default policies.
allowed=''
default_policy=$(git config --get protocol.allow || :)
for protocol in file git http https ssh; do
    if [[ -n ${GIT_ALLOW_PROTOCOL+x} ]]; then
        [[ :$GIT_ALLOW_PROTOCOL: == *":$protocol:"* ]] || continue
    else
        fallback=always
        if [[ $protocol == file ]]; then fallback=user; fi
        policy=$(git config --get "protocol.$protocol.allow" || printf '%s' "${default_policy:-$fallback}")
        case "${policy,,}" in
            always) ;;
            user) case "${GIT_PROTOCOL_FROM_USER-1}" in 1|[Tt][Rr][Uu][Ee]|[Yy][Ee][Ss]|[Oo][Nn]) ;; *) continue ;; esac ;;
            *) continue ;;
        esac
    fi
    allowed="${allowed:+$allowed:}$protocol"
done
GIT_ALLOW_PROTOCOL="$allowed" snapshot_git clone --template= --no-checkout --no-local --no-recurse-submodules --single-branch \
    --depth 1 --branch "$branch" -- "$source_repo" "$tree" || fail 'Clone failed.'
tree_git() { snapshot_git -C "$tree" "$@"; }
commit=$(tree_git rev-parse --verify HEAD)
expected=$(tree_git rev-parse 'HEAD^{tree}')
tree_git ls-tree -rz --full-tree HEAD > "$temporary/entries"
count=0
while IFS= read -r -d '' entry; do
    mode=${entry%% *}
    path=${entry#*$'\t'}
    first=${path%%/*}
    if [[ ${first,,} =~ ^nexus_backup_manifest\.md[.\ ]*$ ]]; then
        fail "Source already uses the reserved manifest name: $path"
    fi
    case "$mode" in
        100644|100755) ;;
        160000) fail "Source contains a submodule: $path" ;;
        120000) fail "Source contains a symbolic link: $path" ;;
        *) fail "Unsupported Git mode $mode for $path" ;;
    esac
    ((count+=1))
done < "$temporary/entries"

# Use stored blob bytes, including files marked export-ignore and export-subst.
# info/attributes overrides source/global transformations in both directions.
mkdir -p -- "$tree/.git/info"
printf '%s\n' '* -text -crlf !eol -ident !filter !working-tree-encoding' > "$tree/.git/info/attributes"
tree_git read-tree --reset -u HEAD

# An LFS pointer alone cannot make an independent copy of its payload.
if tree_git grep --cached --no-textconv -Ilz -e '^version https://git-lfs\.github\.com/spec/v1' \
        -e '^version https://hawser\.github\.com/spec/v1' -- > "$temporary/lfs-candidates"; then
    while IFS= read -r -d '' path; do
        IFS= read -r header < "$tree/$path" || :
        case "${header%$'\r'}" in
            'version https://git-lfs.github.com/spec/v1'|'version https://hawser.github.com/spec/v1')
                if grep -Eq '^oid sha256:[0-9a-f]{64}[[:space:]]?$' "$tree/$path" &&
                   grep -Eq '^size [0-9]+[[:space:]]?$' "$tree/$path"; then
                    fail "Source contains a Git LFS pointer: $path"
                fi ;;
        esac
    done < "$temporary/lfs-candidates"
else
    status=$?
    [[ $status == 1 ]] || fail 'Could not check for Git LFS pointers.'
fi

# Build a fresh index from the actual files; the checkout's stat cache cannot mask
# changed bytes, ignored files, or names collapsed by a case-insensitive filesystem.
export GIT_INDEX_FILE="$temporary/verification.index"
tree_git add --force --all -- .
actual=$(tree_git write-tree)
if [[ $actual != "$expected" ]]; then
    [[ $(tree_git config --bool core.filemode) == false ]] || fail 'Snapshot differs from the source tree.'
    # A Windows filesystem can represent executable blobs as ordinary files.
    # Every differing entry must have exactly this mode change and identical bytes.
    tree_git diff-tree -r --raw -z --no-abbrev --no-renames "$expected" "$actual" > "$temporary/differences"
    while IFS= read -r -d '' metadata && IFS= read -r -d '' path; do
        read -r old_mode new_mode old_id new_id change <<< "$metadata"
        [[ $old_mode == :100755 && $new_mode == 100644 && $old_id == "$new_id" && $change == M ]] ||
            fail "Snapshot differs from the source tree: $path"
    done < "$temporary/differences"
fi
unset GIT_INDEX_FILE

mv -- "$tree/.git" "$temporary/source.git"
[[ ! -e $tree/$manifest && ! -L $tree/$manifest ]] || fail 'Manifest collision on the destination filesystem.'
# Keep URL credentials and query parameters out of a manifest intended for Git.
label=$source_repo
if [[ $label =~ ^([a-zA-Z][a-zA-Z0-9+.-]*://)(.*)$ ]]; then
    scheme=${BASH_REMATCH[1]}
    address=${BASH_REMATCH[2]%%[?#]*}
    authority=${address%%/*}
    label="$scheme${authority##*@}${address#"$authority"}"
fi
printf '# External source snapshot\n\nSource: %s\nBranch: %s\nSource commit: %s\nTracked files copied: %s\n' \
    "$label" "$branch" "$commit" "$count" > "$tree/$manifest"
printf '\nIndependent copy of the tracked files from this commit.\n' >> "$tree/$manifest"

# Staging is on the destination volume. Never nest into or replace an existing directory.
mv -nT -- "$tree" "$target"
[[ ! -d $tree ]] || fail "Destination already exists: $destination"
printf 'Copied %s tracked files into %s at source commit %s.\n' "$count" "$destination" "$commit"
