# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 18:52:43 2016

@author: hihi
"""
import kwordpre
import os
import kmatch
import kgene
import cPickle as pickle
import kheap
#import kpymap
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
kheap_size = 100
kscope_max = 1000*1000
f1 = file('temp.pkl', 'rb')
uni_cnt=pickle.load(f1)
bin_cnt=pickle.load(f1)
id_uni_cnt=pickle.load(f1)
id_bin_cnt=pickle.load(f1)
word_id=pickle.load(f1)
pin2cha=pickle.load(f1)
pin2word=pickle.load(f1)
f1.close()

        
print "start."

letters = 'wo ai bei jing tian an men'
#letters = 'yi zhi mei li de xiao hua'
#letters = 'ji qi xue xi ji qi ying yong '#ji qi le ren men ji qi nong hou de xing qu'
#letters += 'ji qi le ren men '#ji qi nong hou de xing qu'
#letters += 'ji qi nong hou de xing qu'
#letters = 'ji'
letters = letters.replace("\n","").replace("\r","").replace(" ","")

piny_solutions = kgene.kpinysolution(letters,pin2word)
#print h

#piny_sol = kmatch.kmatch_grid(letters,pin2word)
#print piny_sol
word_solutions = []
ws_num = 0

for piny_sol in piny_solutions:
    scope = 1
    print piny_sol
    word_map = []
    for yin in piny_sol:
        scope *=len(pin2word[yin])
        word_map.append(pin2word[yin])
#        for i in pin2word[yin]:
#            print i,#id_uni_cnt[word_id[i]]
#        print ""
    print scope ,
    if scope > kscope_max:
        print "X"
        continue
    else:
        print ""

    word_solutions += kgene.kgene(word_map)
#word_solutions = 
word_solutions.reverse()
#print len(word_solutions)
#
min_value = 0
score_list =[]
#obj = []
j = -1
for word_sol in word_solutions:
    j = j+1
    #print j
    
    #print cl
    ##############################################
    id_list =  []
    for word in word_sol:
        if word_id.has_key(word):
            t = "%05d" % word_id[word]
            id_list.append(t)
    #print id_list
    ##############################################
    bin_list = []
    #print l, 
    l = len(id_list)-1
    for i in range(l):
        bin_list.append(id_list[i]+id_list[i+1])
    #print bin_list
    #print l 
    ##############################################
    t_score =   - l*bin_cnt - uni_cnt 
    #print s,
    if id_uni_cnt.has_key(id_list[0]):
        t_score += id_uni_cnt[id_list[0]]
    for  i in bin_list:
        if id_bin_cnt.has_key(i):
            t_score += id_bin_cnt[i]
    #score_list.append(s)
    ##############################################
    if len(score_list)<kheap_size:
        score_list.append((word_sol,t_score))
        score_list = sorted(score_list, key=lambda st: st[1],reverse=True)
        min_score = score_list[-1][1]
    else :
        if t_score > min_score:
            score_list.append((word_sol,t_score))
            score_list = sorted(score_list, key=lambda st: st[1],reverse=True)
            score_list.pop()  
    ###################################################
    #score_list,min_value =kheap.kheap(score_list,100,min_value,(word_solutions[j],s))
    #print s
print len(score_list)
for s in score_list:
    print s[1],
    for w in s[0]:
        print w,
    print ""
    
    









