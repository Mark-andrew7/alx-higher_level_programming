#!/bin/bash
# takes a URL, sends a request to that URL

curl -sI "$1" | grep "Content-Length" | wc -c