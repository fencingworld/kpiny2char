# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 12:54:32 2016

@author: hihi
"""
import os
import codecs
import chardet
import re
import copy
import kmatch
#import sys
path = r'G:\workspace\nlp\materials'
raw_materials = r'raw_materials'
utf_materials = r'utf_materials'
uni_materials = r'uni_materials'
pre_materials = r'pre_materials'
txt = r'960101.TXT'
pre_txt = r'precess_word.TXT'
#pre_txt = txt
mid_forw_txt = r'mid_forw.txt'
mid_back_txt = r'mid_back.txt'

lexicon_txt = 'lexicon.txt'


fp = codecs.open(os.path.join(path,pre_materials,pre_txt),"r",'utf-16')
content = fp.readlines()
fp.close()
fp = codecs.open(os.path.join(path,lexicon_txt),"r",'utf-16')
lexicon = fp.readlines()
fp.close()

word_cnt={}
word_id = {}
i = 1
for lex in lexicon:
    w = lex.split('\t')
    word_cnt[w[0]] = 0
    word_id[w[0]] = i
    i = i + 1 
special_mark = [u'N']
for sc in special_mark:
    word_cnt[sc] = 0
    word_id[sc] = i
    i = i + 1
word = word_cnt.keys()

tw = '脑出血'.decode('utf-8')

word_cnt_forw,word_cnt_forw_mis = \
    kmatch.kmatch_forward(content,word_cnt,word_id,os.path.join(path,pre_materials,mid_forw_txt))
#word_cnt_back,word_cnt_back_mis = \
#    kmatch.kmatch_backward(content,word_cnt,word_id,os.path.join(path,pre_materials,mid_back_txt))
#print type(word_cnt_forw)
#word_sort_forw = sorted(word_cnt_forw.iteritems(), key=lambda d:d[1], reverse = True)
#
#word_sort_back = sorted(word_cnt_back.iteritems(), key=lambda d:d[1], reverse = True)
id_cnt_uni = {}
for w,i in word_cnt_forw.items():
    id_cnt_uni[ word_id[w] ] = i




