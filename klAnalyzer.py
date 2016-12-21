# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:52:24 2016

@author: keli
"""
import os
import codecs
import chardet
import re
#import sys
#print sys.getdefaultencoding()
def is_chinese(uchar):
        """判断一个unicode是否是汉字"""
        if u'\u4e00' <= uchar <= u'\u9fff':
                return True
        else:
                return False

path = r'G:\workspace\nlp\materials'
raw_materials = r'raw_materials'
utf_materials = r'utf_materials'
uni_materials = r'uni_materials'
pre_materials = r'pre_materials'
txt = r'960101.TXT'
charSetDel = [u'　',u'＊',u'■',u'\n',u'\r',u'\t',u'|',u' ',
           #   u'0',u'',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'[',u']'
              ]
for i in range(128):
    #print i,chr(i),type(chr(i))
    charSetDel.append(chr(i).decode('utf-8'))

print os.path.getsize(os.path.join(path,uni_materials,txt))
fp = codecs.open(os.path.join(path,uni_materials,txt),"r",'utf-16')
fp_r = codecs.open(os.path.join(path,pre_materials,txt),"w+",'utf-16')


content = fp.read()
#content = content.decode('utf-8')
for c in charSetDel:
    #print len(content)
    content = content.replace(c,'')

##content = content.decode('utf-8')
#print len(content)
#for c in content:
#    print ord(c)
#    h =chardet.detect(c)
#    if  h['encoding']!='windows-1252'and  h['encoding']!=None:
#        print c.encode(h['encoding']),h['encoding']
        
#print chardet.detect(content)
print len(content)#,type(content)
#c = []
#c.append( content[10])
#for i in range(len(content)):
#    if not ('\u4e00'<=content[i] and content[i]<='\u9fa5'):
#        print content[i],type(content[i])
#print content[9],content[10],content[11]
fp_r.write(content)
#h=fp.read()
#h  = h.decode('utf-8', 'ignore')
#p = re.compile(ur'[^\u4e00-\u9fa5]') 
#x = p.split(h)

#fp_r.write(x)
#while (h):
    #print h
#    line_coding =  chardet.detect(h)
#    if line_coding['encoding']!='windows-1252' and line_coding['encoding']!='ascii':
#        print line_coding,line_coding['encoding']
#        print h
#    h = fp.read(1)
#for line in fp:
##    #line =line[0:-1]
##    for c in charSetDel:
##        line = line.replace(c,'')
#    line_coding =  chardet.detect(line)
#    
#    if line_coding['encoding'] !='utf-8':
#        print line_coding['encoding']
##        line  = line.decode(line_coding['encoding'], 'ignore')
##        line  = line.encode('utf-8')
#        print line
#    else:
#        print line,len(line)
##    for ch in line:
##        print is_chinese(line[0:1])
#    
#
#    
#    fp_r.write(line)
#    x = chardet.detect(line)
#    if x['encoding']!='utf-8':
#        print line,len(line)
#    #print chardet.detect(line)
#    #fp_r.write(line.lstrip())
#    #break 
#    #print line
fp.close()
fp_r.close()
#print os.path.getsize(os.path.join(path,pre_materials,txt))
#
#fp = codecs.open(os.path.join(path,pre_materials,txt),"r")
#lines = fp.readlines()
#i = 0
#for line in lines:
#    i= i+1
#    line_coding =  chardet.detect(line) 
#    if line_coding['encoding']!='utf-8':
#        print line,line_coding['encoding'],i
#    
#fp.close()
