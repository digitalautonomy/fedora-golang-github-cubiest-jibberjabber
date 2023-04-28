#!/usr/bin/env bash

set -e

build_for_release() {
    local release=$1;

    echo "Building for $release ..."
    mkdir -p $release
    fedpkg --release $release local
    ssh -p 4243 fedora-repo@fedora.autonomia.digital "mkdir -p packages/upload/$release"
    scp -r -P4243 $release/* fedora-repo@fedora.autonomia.digital:packages/upload/$release
    echo "Done build for $release!"
}

for r in "$@"; do
    build_for_release $r
done
