#!/bin/sh
git stash;git pull;pm2 restart main.py 1>/dev/null 2>&1