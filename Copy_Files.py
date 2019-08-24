import os
from os import path
import shutil

'''
Add source and destination.
Follows the follwing syntax for src and dst: "drive:\\folder1\\folder2"
e.g. "H:\\Bangalore"  "F:\\Photos & Videos\\""
'''

src = ""
dst = ""

files = [i for i in os.listdir(src) if i.endswith(".JPG") and path.isfile(path.join(src, i))]
for f in files:
    shutil.copy(path.join(src, f), dst)
