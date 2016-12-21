# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 22:52:44 2016

@author: hihi
"""
import copy
def kmatch_forward(content,word_cnt):
    word_cnt_forw       = copy.deepcopy(word_cnt)
    print type(word_cnt_forw)
    word_cnt_forw_mis   ={}
    for con in content:
        l_con = len(con)-1
        j = l_con
        i =0 
        while i< l_con :
            tw = con[i:j]
            ti = i
            tj = j
            if word_cnt_forw.has_key(tw):
                word_cnt_forw[tw] = word_cnt_forw[tw] + 1
                i = j 
                j = l_con
            else:
                j = j - 1
                if (j <= i):
                    i = i+1
                    j = l_con
                    #print con[:-1]   
                    tw_mis = con[ti:tj]
                    #print tw_mis
                    if word_cnt_forw_mis.has_key(tw_mis):
                        word_cnt_forw_mis[tw_mis] = word_cnt_forw_mis[tw_mis] + 1
                    else:
                         word_cnt_forw_mis[tw_mis] = 1
    #word_cnt_forw = sorted(word_cnt_forw.iteritems(), key=lambda d:d[1], reverse = True)

    return word_cnt_forw,word_cnt_forw_mis;
def kmatch_backward(content,word_cnt):
    word_cnt_back       = copy.deepcopy(word_cnt)
    word_cnt_back_mis   ={}
    for con in content:
        l_con = len(con)-1
        j = l_con-1
        i = 0 
        while  j > 0 :
            tw = con[i:j]
            ti = i
            tj = j
            if word_cnt_back.has_key(tw):
                word_cnt_back[tw] = word_cnt_back[tw] + 1
                j = i
                i = 0 
            else:
                i = i + 1
                if ( i >= j):
                    j = j - 1
                    i = 0
                    print con   
                    tw_mis = con[ti:tj]
                    print tw_mis
                    if word_cnt_back_mis.has_key(tw_mis):
                        word_cnt_back_mis[tw_mis] = word_cnt_back_mis[tw_mis] + 1
                    else:
                         word_cnt_back_mis[tw_mis] = 1
    #word_cnt_back = sorted(word_cnt_back.iteritems(), key=lambda d:d[1], reverse = True)
    return word_cnt_back,word_cnt_back_mis;
