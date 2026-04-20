#!/bin/bash
HOUR=$(date +%H)
MINUTE=$(date +%M)
if [ "$HOUR" == "05" ] && [ "$MINUTE" == "00" ]; then
    python3 /home/user/2025midyear/daily_greeting.py
fi
