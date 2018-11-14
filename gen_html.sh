#!/bin/bash -eux

pushd $(git rev-parse --show-toplevel)/doc
echo "GENERATE HTML FILES"
rm -rf ./html
reveal-md README.md --static ./html
popd
