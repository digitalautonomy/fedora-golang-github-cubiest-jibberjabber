#!/usr/bin/env bash

set -e

build_for_release() {
    local release=$1;

    echo "Building for $release ..."
    fedpkg --release $release local
    scp -r -P4243 *.rpm fedora-repo@fedora.autonomia.digital:packages/upload/$release
    rm -rf *.rpm
    echo "Done build for $release!"
}

for r in "$@"; do
    build_for_release $r
done
