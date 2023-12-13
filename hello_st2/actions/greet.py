#!/usr/bin/env python3

from __future__ import print_function
import sys 

def greet(content_before, content_after):
    print("Content_Before: {}".format(content_before))
    print("Content_After: {}".format(content_after))


if __name__ == "__main__":
    # Check if the required parameters are provided
    if len(sys.argv) < 2:
        print("Usage: {} <greeting> <count> <content>".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve parameters from the command-line arguments
    content_before = sys.argv[1]
    content_after = sys.argv[2]

    # Call the greet function
    greet(content_before, content_after)
