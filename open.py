import os
import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

if "chrome" in str(sys.argv):
    print("chrome is there")
    os.system("google-chrome-stable")
