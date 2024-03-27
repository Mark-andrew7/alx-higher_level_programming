#!/bin/bash
# takes URL as argument sends GET request to the URL
curl -sI "$1" -H "X-School-User-Id: 98"
