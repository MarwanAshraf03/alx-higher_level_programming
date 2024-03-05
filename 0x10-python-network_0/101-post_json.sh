#!/bin/bash
# a comment
curl -X POST -H 'Content-Type: application/json' -d @"$2" "$1"
