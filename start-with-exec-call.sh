#!/bin/sh

set -exu

exec ./main.py

echo "This will never be executed"
