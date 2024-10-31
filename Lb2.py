#! /usr/bin/env python3
import sys
def with_file(arg: list[str]):
    sys.stderr=open('errors.txt','w')
    with open(arg[1],"r") as f:
        for line in f:
            string=line.strip()
            if not string:
                continue
            if string[0].islower():
                sys.stderr.write(f"Error! Name {string} with a small first letter\n")
            elif not string.isalpha():
                sys.stderr.write(f"Error! Name {string} does not consist only of letters\n")
            else:
                print(f"Hi, {string}!")
def without_file():
   try:
       while True:
           A=input("Hello! What is your name? ")
           if A[0].islower():
               print(f"Name {A} with a small first letter")
           elif not A.isalpha():
               print(f"Name {A} does not consist only of letters")
           else:
               print(f"Nice to see you, {A}!")
   except KeyboardInterrupt:
        print("\nGoodbye!")
if len(sys.argv)>1:
    namefile=sys.argv
    with_file(namefile)
else:
    without_file()