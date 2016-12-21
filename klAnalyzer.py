# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:52:24 2016

@author: hihi
"""
import os
import codecs
import chardet
import re
#import sys
#print sys.getdefaultencoding()


path = r'G:\workspace\nlp\materials'
raw_materials = r'raw_materials'
utf_materials = r'utf_materials'
uni_materials = r'uni_materials'
pre_materials = r'pre_materials'
txt = r'960101.TXT'
charSetDel = [u'　',u'＊',u'■',u'\n',u'\r',u'\t',u'|',u' ' ]
for i in range(128):
    #print i,chr(i),type(chr(i))
    charSetDel.append(chr(i).decode('utf-8'))

#print os.path.getsize(os.path.join(path,uni_materials,txt))
fp = codecs.open(os.path.join(path,uni_materials,txt),"r",'utf-16')
fp_r = codecs.open(os.path.join(path,pre_materials,txt),"w+",'utf-16')
content = fp.read()
print len(content)
#remove unrelated char and English char
for c in charSetDel:
    content = content.replace(c,'')
print len(content)
#mark chinese numbers
#for example 一九九五年十二,一百二十万,一些,十四大,N亿吨,七五,无一退货,短斤少两
num_ch = '[０-９．％]+'.decode('utf-8')
content = re.sub(num_ch,'N',content)
print len(content)
spt_ch = '[。，、；：（）《》“”！／]+'.decode('utf-8')
content = re.sub(spt_ch,'\n',content)
print len(content)

news_ch ='N第N版'.decode('utf-8')
content = re.sub(news_ch,'\n',content)
print len(content)

news_ch ='国际N短讯'.decode('utf-8')
content = re.sub(news_ch,'\n',content)
print len(content)

fp_r.write(content)
fp.close()
fp_r.close()
