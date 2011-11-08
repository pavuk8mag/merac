#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Pavuk"
__date__ ="$8.11.2011 20:19:00$"

if __name__ == "__main__":
    print "Hello World";
    from math import sqrt

    for n in range(99, 0, -1):
        root = sqrt(n)
        if root == int(root):
            print n
            break
