#!/bin/bash
# a comment
curl -sI "$1" | greb -i Content-Length
