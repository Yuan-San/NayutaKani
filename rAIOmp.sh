#!/bin/sh
git stash;git pull;pm2 restart discordbot 1>/dev/null 2>&1