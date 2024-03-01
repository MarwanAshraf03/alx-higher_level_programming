#!/bin/bash
# a comment
curl -sI "$1" | grep Allow | sed 's/Allow: //'
