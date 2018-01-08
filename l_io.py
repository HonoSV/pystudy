# -*- coding: utf-8 -*-
import os
'''
from datetime import datetime

pwd = os.path.abspath('.')
print('     Size    last Modified Name')
print('------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d %s %s%s' % (fsize, mtime, f, flag))
'''

'''
def findFile(str,path = '.'):
    for x in os.listdir(path):
        f = os.path.join(path,x)
        if os.path.isfile(f) and os.path.splitext(f)[1]== str:
            print(os.path.split(f)[1])
        elif os.path.isdir(f):
            findFile(str,f)

if __name__ == '__main__':
    a = input('pls: ')
    findFile(a,'.')
'''

import os
def search(x,dir):
   for thing in os.scandir(dir):
      newpath=os.path.join(dir,thing.name)
      if os.path.isfile(thing):
         if x in thing.name:
            print(os.path.relpath(newpath,a)) #global
      elif os.path.isdir(thing):
         search(x,newpath)

a=os.getcwd()
b=input('please input what you want to find:')
search(b,a)