#!/bin/bash -x
# Copyright (C) 2024 Maxwell G <maxwell@gtmx.me>
# SPDX-License-Identifier: MIT

# Create an archive for a tests/integration specfile

set -euo pipefail

_path="$(command -v go_vendor_archive 2>/dev/null || :)"
_default_path="pipx run --spec ../../../[specfile] go_vendor_archive"
GO_VENDOR_ARCHIVE="${GO_VENDOR_ARCHIVE:-${_path:-${_default_path}}}"
IFS=" " read -r -a command <<< "${GO_VENDOR_ARCHIVE}"
command+=("create")

spectool -g ./*.spec
ls
if [ -f "go-vendor-tools.toml" ]; then
    command+=("--config" "$(pwd)/go-vendor-tools.toml")
fi
time "${command[@]}" "$@" ./*.spec
# Test idempotency by running again with networking disabled and a timeout
# to make sure nothing is downloaded.
command+=("--idempotent")
timeout 5 unshare -rn "${command[@]}" "$@" ./*.spec | grep 'already exists'
sha512sum -c CHECKSUMS
