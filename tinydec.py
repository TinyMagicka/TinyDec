#!/usr/bin/env python
#encoding:utf-8

import os
import sys
from GlobalSetting import *

USAGE = '''
USAGE: 
disassemble:
python tinydec.py d  xxx.apk [dir]

rebuild:
python tinydec.py b  dir  [xxx.apk]

sign:
python tinydec.py s xxx.apk
'''

def build(src, dst):
    dst = dst if len(dst) else src+'.apk'
    cmd = "java -jar %s b %s -o %s" % (APKTOOL, src, dst)
    os.system(cmd)
    cmd = SIGNCMD+" %s tinymin"%dst
    os.system(cmd)

def disassemble(src, dst):
    dst = dst if len(dst) else src[:src.find('.')]
    dst_tmp = dst + "/.tmp"
    cmd = "java -jar %s d -f %s -o %s" % (APKTOOL, src, dst)
    os.system(cmd)
    #cmd = "mkdir %s" % dst_tmp
    #os.system(cmd)
    cmd = "java -jar %s d -s %s -o %s" % (APKTOOL, src, dst_tmp)
    os.system(cmd)
    cmd = "mv %s/classes.dex %s/classes.dex ; rm -r %s" % (dst_tmp, dst, dst_tmp)
    os.system(cmd)
    cmd = "dex2jar %s/classes.dex"%(dst)
    os.system(cmd)
    cmd = "java -jar %s %s/classes_dex2jar.jar" % (JD_GUI, dst)
    os.system(cmd)

def sign(src, dst):
    cmd = SIGNCMD+" %s tinymin"%src
    os.system(cmd)

def main():
    args = sys.argv
    if len(args) < 3:
        print USAGE
        exit()
    func = {'b': build, 'd': disassemble, 's': sign }[args[1]]
    src = args[2]
    dst = "" if len(args) < 4 else args[3]
    func(src, dst)


if __name__ == '__main__':
    main()


