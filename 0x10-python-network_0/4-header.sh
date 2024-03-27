#!/bin/bash
# takes URL as argument sends GET request to the URL
curl -sH "X-School-User-Id: 98" "${1}"
