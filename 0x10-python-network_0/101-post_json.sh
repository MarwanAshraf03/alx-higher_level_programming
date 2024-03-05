#!/bin/bash
# a comment
curl -X POST -sH 'Content-Type: application/json' -d @"$2" "$1"
