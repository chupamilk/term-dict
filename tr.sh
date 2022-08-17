#!/bin/bash

while getopts 't:b' OPTION; 
do 
    case "$OPTION" in
        t) 
            echo "Using terminal - Word: $OPTARG"
            #python ~/Projects/TermDict/terminal_dict.py
            ;;
        b)
            echo "Browser Mode"

            # Get words until SIGINT 
            while true 
            do
                read -p "Word/Text: " OPTARG
                python ~/Projects/TermDict/browser_dict.py $OPTARG
            done
            ;;
        ?)
            echo "script usage: $(basename \$0) [-t word/sentence] [-b word/sentence]" 
            exit 1
            ;;
    esac
done
