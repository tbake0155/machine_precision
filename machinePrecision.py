#!/usr/bin/env python3
#
# machinePrecision will find the minimum float value that can be 
# represented in the machine running this code
#
# the program will take a command line argument to allow double or 
# single precision floating point numbers to be used.  if double
# precision is desired, pass "double" as the first command line
# argument.  all other arguments, including none,  defaults to 
# single precision.
#
# Author: Timothy Baker
# Date  : September 2017
# Class : CS 517
# Assg  : Machine Assignment 1, Problem 2

import struct

def emulate32(real64) :
    real32 = struct.unpack('f', struct.pack('f', real64))[0]
    return real32

def determinePrecision(precision) :
    if precision == "double" :
        a = float(4.0) / float(3.0)
        b = float(a) - float(1.0)
        c = float(b) + float(b) + float(b)
        machinePrecision = float(abs(float(c) - float(1.0)))
    else :
        try :
            a = emulate32(4.0) / emulate32(3.0)
            b = emulate32(a) - emulate32(1.0)
            c = emulate32(b) + emulate32(b) + emulate32(b)
            machinePrecision = abs(emulate32(c) -emulate32(1.0))
        except :
            return False
    return emulate32(machinePrecision)

def main() :
    singlePrecision = determinePrecision("single")
    doublePrecision = determinePrecision("double")
    if type(singlePrecision) == bool or type(doublePrecision) == bool :
        print("error: couldn't detect precision")
    else :
        print ("\n\n", "  Machine Precision", "\n")
        print ("    single : ", singlePrecision)
        print ("    double : ", doublePrecision, "\n\n")
        
if __name__ == "__main__":
    main()

#end of file 

