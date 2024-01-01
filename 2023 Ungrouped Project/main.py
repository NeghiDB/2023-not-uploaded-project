import os, fnmatch

arr = os.listdir('.')
patt = '*.docx'
pbtt = '*.txt'
pett = '*.pdf'
pftt = '*.exe'

valtman = fnmatch.filter(arr, patt)
vbltman = fnmatch.filter(arr, pbtt)
veltman = fnmatch.filter(arr, pett)
vfltman = fnmatch.filter(arr, pftt)

print(valtman+vbltman+veltman+vfltman)
input()
