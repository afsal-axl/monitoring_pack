#!/usr/bin/env python3

from __future__ import print_function
import sys 

def action2(error):
    print(error)

if __name__ == "__main__":
    # Check if the required parameters are provided
    if len(sys.argv) < 1:
        print("Usage: {} <greeting> <count> <content>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve parameters from the command-line arguments
    error = sys.argv[1]

    # Call the greet function
    action2(error)
