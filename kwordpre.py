# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 18:11:34 2016

@author: hihi
"""
import os
import codecs
import chardet
import re
import copy
import kmatch
import kstr2int
#import sys
#path = r'G:\workspace\nlp\materials'
#raw_materials = r'raw_materials'
#utf_materials = r'utf_materials'
#uni_materials = r'uni_materials'
#pre_materials = r'pre_materials'
#txt = r'960101.TXT'
#pre_txt = r'precess_word.TXT'
##pre_txt = txt
#mid_forw_txt = r'mid_forw.txt'
#mid_back_txt = r'mid_back.txt'
#
#lexicon_txt = 'lexicon.txt'
def kwordpre(file_path):
    fp = codecs.open(file_path,"r",'utf-16')
    #fp = codecs.open(os.path.join(path,lexicon_txt),"r",'utf-16')

    lexicon = fp.readlines()
    fp.close()
    c = 1
    pin2cha = {}
    pin2word = {}
    word_cnt= {}
    word_id = {}
    for lex in lexicon:
        w = lex.split('\t')
        word_cnt[w[0]] = 0
        word_id[w[0]] = c
        c = c + 1 
        chars = w[0]
#        piny_ds = w[1].replace("\n","").replace("\r","")
#        piny_ds = piny_ds.replace("1","").replace("2","")
#        piny_ds = piny_ds.replace("3","").replace("4","").replace("5","")
#        print piny_ds
#        if pin2word.has_key(piny_ds):
#            if chars not in pin2word[piny_ds]:
#                pin2word[piny_ds].append(chars)
#        else:
#            pin2cha[piny_ds] = [chars]        
        piny_ds = w[1].replace("\n","").replace("\r","").split(' ')
        #piny_ds= piny_ds.split(' ')
        pinys = []
        for p in piny_ds:
            pinys.append(p[:-1])
        l = len(pinys)
        for i in range(l):
            #print pinys[i]
            if pin2cha.has_key(pinys[i]):
                if chars[i] not in pin2cha[pinys[i]]:
                    pin2cha[pinys[i]].append(chars[i])
            else:
                pin2cha[pinys[i]] = [chars[i]]
        piny_ds = ''.join(pinys)
        #print piny_ds
        if pin2word.has_key(piny_ds):
            if chars not in pin2word[piny_ds]:
                pin2word[piny_ds].append(chars)
        else:
            pin2word[piny_ds] = [chars] 
        
    special_mark = [u'N']
    for sc in special_mark:
        word_cnt[sc] = 0
        word_id[sc] = c
        c = c + 1
    return word_cnt,word_id,pin2cha,pin2word
