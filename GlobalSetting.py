#!/usr/bin/env python
#encoding:utf-8

import os

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
APKTOOL =   ROOT_PATH+'/tools/apktool/apktool.jar'
DEX2JAR  =  ROOT_PATH+'/tools/dex2jar/dex2jar.sh'
JD_GUI   =  ROOT_PATH+'/tools/jd_gui/jd.jar'
KEYS  =     ROOT_PATH+'/tools/signapk/keys/tinymin.keystore'
SIGNCMD  =  "jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore %s" % KEYS
BAKSMALI =  ROOT_PATH+'/tools/baksmali/baksmali.jar'
SMALI    =  ROOT_PATH+'/tools/smali/smali.jar'