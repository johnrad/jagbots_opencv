#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  demoSimpleArgs.py
#  
#  Copyright 2017 johnrad <john@radkofamily.com>
#  
#  This script is to show a simple way to handle command line
#  arguments.
#
#  There is a brief article on options for this at http://stackabuse.com/command-line-arguments-in-python/
#  
#  
import sys     # you need this for this method

def main(args):
    #
    #  How many args do we have?
    #
    num_args = len(sys.argv)    # sys.argv is a list - see Chap 3 in Crash Course
    
    #
    #  Let's iterate through the arguments and show what they are
    #
    arg_pos = 0
    for arg in sys.argv:                    # this form of looping through a list is in Chap 4 in Crash Course
        print("Argument %d is %s"%(arg_pos,sys.argv[arg_pos]))
        arg_pos = arg_pos + 1
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
