# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 12:54:32 2016

@author: hihi
"""
import os
import codecs
import chardet
import re
#import sys
path = r'G:\workspace\nlp\materials'
raw_materials = r'raw_materials'
utf_materials = r'utf_materials'
uni_materials = r'uni_materials'
pre_materials = r'pre_materials'
txt = r'960101.TXT'
lexicon_txt = 'lexicon.txt'

def forward_match(content,word_cnt):
    word_cnt_forw=0
    word_cnt_forw_mis=0 
    return word_cnt_forw,word_cnt_forw_mis;

fp = codecs.open(os.path.join(path,pre_materials,txt),"r",'utf-16')
content = fp.readlines()
fp.close()
fp = codecs.open(os.path.join(path,lexicon_txt),"r",'utf-16')
lexicon = fp.readlines()
fp.close()

word_cnt={}
for lex in lexicon:
    word_cnt[lex.split('\t')[0]] = 0
special_mark = [u'N']
for sc in special_mark:
    word_cnt[sc] = 0
word = word_cnt.keys()

tw = '脑出血'.decode('utf-8')
k  = 1
match_false = 0
word_cnt_forw_mis={}
for con in content:
    #con = con [:-1]
#    print len(con)
    #print k
    k = k + 1
    l_con = len(con)-1
    i =0 
    j = l_con
    while i< l_con :
        tw = con[i:j]
        ti = i
        tj = j
        if word_cnt.has_key(tw):
        #if tw in word:
            word_cnt[tw] = word_cnt[tw] + 1
            #print word_cnt[tw] 
            i = j 
            j = l_con
        else:
            j = j - 1
            if (j <= i):
                i = i+1
                j = l_con
                match_false =  match_false + 1
                #print con[:-1]   
                tw_mis = con[ti:tj]
                #print tw_mis
                if word_cnt_forw_mis.has_key(tw_mis):
                    word_cnt_forw_mis[tw_mis] = word_cnt_forw_mis[tw_mis] + 1
                else:
                     word_cnt_forw_mis[tw_mis] = 1
                #print '\n'
        
print match_false
    
word_sort = sorted(word_cnt.iteritems(), key=lambda d:d[1], reverse = True)

if  tw in word:
    word_cnt[tw] = word_cnt[tw] + 1
