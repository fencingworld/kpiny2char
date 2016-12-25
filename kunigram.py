# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 20:35:22 2016

@author: hihi
"""
import os
import codecs
import chardet
import re
import copy
import kmatch
import kstr2int
import kwordpre
import math
import cPickle as pickle
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


fp = open(os.path.join(path,pre_materials,'mid_forw.txtid'),"rb")
words = fp.read()
fp.close()
words=kstr2int.str2int(words)
fp = codecs.open(os.path.join(path,lexicon_txt),"r",'utf-16')
lexicon = fp.readlines()
fp.close()

word_cnt ={}
word_id = {}
piy2cha = {}

word_cnt,word_id,pin2cha,pin2word = kwordpre.kwordpre(os.path.join(path,lexicon_txt))
#for lex in lexicon:
#    w = lex.split('\t')
#    word_cnt[w[0]] = 0
#    word_id[w[0]] = i
#    
#    i = i + 1 
#special_mark = [u'N']
#for sc in special_mark:
#    word_cnt[sc] = 0
#    word_id[sc] = i
#    i = i + 1
#id_uni_cnt = [0 for i in range(65535) ]
id_uni_cnt = {}
#id_uni_next = [-1 for i in range(65535) ]
id_bin_cnt = {}
print "-------------"
len_words = len(words)/1
k = 0
while k < len_words - 1:
    if k%1000000==0:
        print k
    #print k
    w_id = words[k]
    if  not(w_id ==0 or w_id ==65535):
        item = "%05d" % w_id
        #id_uni_cnt[w_id] = id_uni_cnt[w_id] + 1
        if id_uni_cnt.has_key(item):
            id_uni_cnt[item] = id_uni_cnt[item] + 1
        else:
            id_uni_cnt[item] = 1

        n_id =words[k+1]
        if not(n_id==0 or n_id ==65535):
#            if id_uni_next[w_id]==-1:
#                dic = {}
#                dic[n_id] = 1
#                id_bin_cnt.append(dic)
#                id_uni_next[w_id] = len(id_bin_cnt)-1
#            else:
#                id_bin_cnt.append(0)
            #item = str(w_id)+'-'+str(n_id)
            item = "%05d%05d" % (w_id,n_id)
            #print item
            if id_bin_cnt.has_key(item):
                id_bin_cnt[item] = id_bin_cnt[item] + 1
            else:
                id_bin_cnt[item] = 1
    k = k + 1
uni_cnt = 0
for k,v in id_uni_cnt.items():
    uni_cnt = uni_cnt + v
    id_uni_cnt[k] = math.log(v+1)
uni_cnt = math.log(uni_cnt + len(id_uni_cnt))
bin_cnt = 0
for k,v in id_bin_cnt.items():
    bin_cnt = bin_cnt + v
    id_bin_cnt[k] = math.log(v+1)
bin_cnt = math.log(bin_cnt + len(id_bin_cnt))
#for k,v in id_bin_cnt.items():
#    id_bin_cnt[k] = (1.0*v)/bin_cnt
st = u"机器"
item = "%05d" % word_id[st]
print id_uni_cnt[item]
f1 = file('temp.pkl', 'wb')
pickle.dump(uni_cnt, f1, True)
pickle.dump(bin_cnt, f1, True)
pickle.dump(id_uni_cnt, f1, True)
pickle.dump(id_bin_cnt, f1, True)
pickle.dump(word_id, f1, True)
pickle.dump(pin2cha, f1, True)
pickle.dump(pin2word, f1, True)
f1.close()

    
    
    
    
    
    
    

