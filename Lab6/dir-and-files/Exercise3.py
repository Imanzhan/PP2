#Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os
p = str(input())
c = os.access(p, os.F_OK)
print("Existance:", c)

if c: 
    print("File Name:", os.path.basename(p))
    print("Dir Name:", os.path.dirname(p))