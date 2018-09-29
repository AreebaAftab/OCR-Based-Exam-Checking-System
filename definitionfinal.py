# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 00:26:22 2018

@author: Areeba aftab
"""

import gensim
import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.corpus import wordnet as wn 
#from checkwindow import Ui_checkwindow
 
       
stop_words = set(stopwords.words("english"))

lookup = "What is computer?"
lookup2= "What is the difference between Internet and Intranet?"
lookup3= "What is an operating system? Also give some Examples?"


with open("answersheet/answersheet1.txt", 'r') as myFile:
    for num, line in enumerate(myFile, 0):
        if lookup in line:
            print('found at line:', num)
            a=num
        if lookup2 in line:
            print('found at line:', num)
            b=num
        if lookup3 in line:
            print('found at line:', num)
            d=num
    e=num
    #print(num)
    c= "answersheet/answersheet1.txt"                 
    with open(c,'r') as myfile:
        raw_documents=myfile.readlines()[a+1:b]
        #print(raw_documents)
        #print("Number of documents:",len(raw_documents))
        raw_documents = [''.join(a for a in s if a not in string.punctuation) for s in raw_documents]
        #print(raw_documents)
        AllWords = list()      #create new list
        ResultList = list()
        for line in raw_documents:
            line.rstrip()   #strip white space
            words = line.split()    #split lines of words and make list
            AllWords.extend(words)   #make the list from 4 lists to 1 list
    
        AllWords.sort()  #sort list
    
        for word in AllWords:   #for each word in line.split()
            if word not in ResultList:    #if a word isn't in line.split            
                 ResultList.append(word)   #append it.
        #print(ResultList)
        
        gen_docs = [w.lower() for w in ResultList if w not in stop_words]
        a=[]
        for i in gen_docs:
            q=nltk.pos_tag(gen_docs)
            for i in range(len(q)):
                
                if q[i][1]=='RB':
                    for ss in wn.synsets(q[i][0], pos=wn.ADV):
                        #print(ss, ss.definition())
                        a=a+[ss.definition()]
                elif q[i][1]=='NN' or q[i][1]=='NNS' or q[i][1]=='NNP':
                    for ss in wn.synsets(q[i][0], pos=wn.NOUN):
                         
                        #print(ss, ss.definition())
                         a=a+[ss.definition()]
                elif q[i][1]=='JJ':
                    for ss in wn.synsets(q[i][0], pos=wn.ADJ):
                         #print(ss, ss.definition())
                         a=a+[ss.definition()]
                elif q[i][1]=='VB':
                    for ss in wn.synsets(q[i][0], pos=wn.VERB):
                         #print(ss, ss.definition())
                         a=a+[ss.definition()]


        AllWords = list()      #create new list
        ResultList = list()
        for line in a:
            line.rstrip()   #strip white space
            words = line.split()    #split lines of words and make list
            AllWords.extend(words)   #make the list from 4 lists to 1 list

        AllWords.sort()  #sort list

        for word in AllWords:   #for each word in line.split()
            if word not in ResultList:    #if a word isn't in line.split            
                 ResultList.append(word)   #append it.
        #print(ResultList)
        ResultListt=gen_docs+ResultList
        
        gen_docs = [[w.lower() for w in word_tokenize(word) if w not in stop_words] 
                        for word in ResultListt]
        
        #print(gen_docs)
        dictionary1 = gensim.corpora.Dictionary(gen_docs)
        #print(dictionary[2])
#print(dictionary.token2id['road'])
        #print("Number of words in dictionary1:",len(dictionary1))
        for i in range(len(dictionary1)):
              #print(i, dictionary1[i])
              corpus1 = [dictionary1.doc2bow(gen_doc) for gen_doc in gen_docs]
        #print(corpus1)

        tf_idf1 = gensim.models.TfidfModel(corpus1)
        #print(tf_idf1)
        s = 0
        for i in corpus1:
            s += len(i)
        #print(s)
        sims1 = gensim.similarities.Similarity('answersheet/answersheet1.txt',tf_idf1[corpus1],
                                              num_features=len(dictionary1))
        print(sims1)
    
    c= "answersheet/answersheet1.txt"                 
    with open(c,'r') as myfile:
        raw_documents=myfile.readlines()[b+1:d]
        #print(len(raw_documents))
        #print("Number of documents:",len(raw_documents))
        raw_documents = [''.join(a for a in s if a not in string.punctuation) for s in raw_documents]
        #print(raw_documents)
        AllWords = list()      #create new list
        ResultList = list()
        for line in raw_documents:
            line.rstrip()   #strip white space
            words = line.split()    #split lines of words and make list
            AllWords.extend(words)   #make the list from 4 lists to 1 list
    
        AllWords.sort()  #sort list
    
        for word in AllWords:   #for each word in line.split()
            if word not in ResultList:    #if a word isn't in line.split            
                 ResultList.append(word)   #append it.
        #print(ResultList)
        
        gen_docs = [w.lower() for w in ResultList if w not in stop_words]
        a=[]
        for i in gen_docs:
            q=nltk.pos_tag(gen_docs)
            for i in range(len(q)):
                
                if q[i][1]=='RB':
                    for ss in wn.synsets(q[i][0], pos=wn.ADV):
                        #print(ss, ss.definition())
                        a=a+[ss.definition()]
                elif q[i][1]=='NN' or q[i][1]=='NNS' or q[i][1]=='NNP':
                    for ss in wn.synsets(q[i][0], pos=wn.NOUN):
                         
                        #print(ss, ss.definition())
                         a=a+[ss.definition()]
                elif q[i][1]=='JJ':
                    for ss in wn.synsets(q[i][0], pos=wn.ADJ):
                         #print(ss, ss.definition())
                         a=a+[ss.definition()]
                elif q[i][1]=='VB':
                    for ss in wn.synsets(q[i][0], pos=wn.VERB):
                         #print(ss, ss.definition())
                         a=a+[ss.definition()]


        AllWords = list()      #create new list
        ResultList = list()
        for line in a:
            line.rstrip()   #strip white space
            words = line.split()    #split lines of words and make list
            AllWords.extend(words)   #make the list from 4 lists to 1 list

        AllWords.sort()  #sort list

        for word in AllWords:   #for each word in line.split()
            if word not in ResultList:    #if a word isn't in line.split            
                 ResultList.append(word)   #append it.
        #print(ResultList)
        ResultListt=gen_docs+ResultList
        gen_docs = [[w.lower() for w in word_tokenize(word) if w not in stop_words] 
                       for word in ResultListt]
        
        #print(gen_docs2)
        dictionary2 = gensim.corpora.Dictionary(gen_docs)
        #print(dictionary[2])
#print(dictionary.token2id['road'])
        #print("Number of words in dictionary2:",len(dictionary2))
        for i in range(len(dictionary2)):
              print(i, dictionary2[i])
              corpus2 = [dictionary2.doc2bow(gen_doc) for gen_doc in gen_docs]
        #print(corpus2)

        tf_idf2 = gensim.models.TfidfModel(corpus2)
        #print(tf_idf2)
        s = 0
        for i in corpus2:
            s += len(i)
        #print(s)
        sims2 = gensim.similarities.Similarity('answersheet/answersheet1.txt',tf_idf2[corpus2],
                                                  num_features=len(dictionary2))
        print(sims2)
    c= "answersheet/answersheet1.txt"                 
    with open(c,'r') as myfile:
        raw_documents=myfile.readlines()[d+1:e]
        #print(raw_documents)
        raw_documents = [''.join(a for a in s if a not in string.punctuation) for s in raw_documents]
        #print(raw_documents)
        AllWords = list()      #create new list
        ResultList = list()
        for line in raw_documents:
            line.rstrip()   #strip white space
            words = line.split()    #split lines of words and make list
            AllWords.extend(words)   #make the list from 4 lists to 1 list
    
        AllWords.sort()  #sort list
    
        for word in AllWords:   #for each word in line.split()
            if word not in ResultList:    #if a word isn't in line.split            
                 ResultList.append(word)   #append it.
        #print(ResultList)
        
        gen_docs = [w.lower() for w in ResultList if w not in stop_words]
        a=[]
        for i in gen_docs:
            q=nltk.pos_tag(gen_docs)
            for i in range(len(q)):
                
                if q[i][1]=='RB':
                    for ss in wn.synsets(q[i][0], pos=wn.ADV):
                        #print(ss, ss.definition())
                        a=a+[ss.definition()]
                elif q[i][1]=='NN' or q[i][1]=='NNS' or q[i][1]=='NNP':
                    for ss in wn.synsets(q[i][0], pos=wn.NOUN):
                         
                        #print(ss, ss.definition())
                         a=a+[ss.definition()]
                elif q[i][1]=='JJ':
                    for ss in wn.synsets(q[i][0], pos=wn.ADJ):
                         #print(ss, ss.definition())
                         a=a+[ss.definition()]
                elif q[i][1]=='VB':
                    for ss in wn.synsets(q[i][0], pos=wn.VERB):
                         #print(ss, ss.definition())
                         a=a+[ss.definition()]


        AllWords = list()      #create new list
        ResultList = list()
        for line in a:
            line.rstrip()   #strip white space
            words = line.split()    #split lines of words and make list
            AllWords.extend(words)   #make the list from 4 lists to 1 list

        AllWords.sort()  #sort list

        for word in AllWords:   #for each word in line.split()
            if word not in ResultList:    #if a word isn't in line.split            
                 ResultList.append(word)   #append it.
        #print(ResultList)
        ResultListt=gen_docs+ResultList
        gen_docs = [[w.lower() for w in word_tokenize(word) if w not in stop_words] 
                      for word in ResultListt]
        
        print(gen_docs)
        dictionary3 = gensim.corpora.Dictionary(gen_docs)
        
#print(dictionary.token2id['road'])
        #print("Number of words in dictionary3:",len(dictionary3))
        for i in range(len(dictionary3)):
              print(i, dictionary3[i])
              corpus3 = [dictionary3.doc2bow(gen_doc) for gen_doc in gen_docs]
        #print(corpus3)

        tf_idf3 = gensim.models.TfidfModel(corpus3)
        
        #print(tf_idf3)
        s = 0
        for i in corpus3:
            s += len(i)
        #print(s)
        sims3 = gensim.similarities.Similarity('answersheet/answersheet1.txt',tf_idf3[corpus3],
                                                   num_features=len(dictionary3))
        #print(sims3)
            
#MAIN CODE
#a= "answersheet/answersheet1.txt" 
#myfile= open(a, 'r')
#raw_documents=myfile.readlines()
#print(raw_documents)
#print("Number of documents:",len(raw_documents))
#stop_words = set(stopwords.words("english"))
#gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stop_words] 
#                for text in raw_documents]
#dictionary = gensim.corpora.Dictionary(gen_docs)
#print(dictionary[2])
##print(dictionary.token2id['road'])
#print("Number of words in dictionary:",len(dictionary))
#for i in range(len(dictionary)):
#    print(i, dictionary[i])
#    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
#print(corpus)
#
#tf_idf = gensim.models.TfidfModel(corpus)
#print(tf_idf)
#s = 0
#for i in corpus:
#    s += len(i)
#print(s)
#sims = gensim.similarities.Similarity('gensimfile2.txt',tf_idf[corpus],
#                                      num_features=len(dictionary))
#print(sims)
#print(type(sims))
#
#inputdir = "papers/"
#filelist = os.listdir(inputdir)

#ORIGINAL ACCURACIES
marks1=5
marks2=2
marks3=5        
lookup = "What is computer?"
lookup2= "What is the difference between Internet and Intranet?"
lookup3= "What is an operating system? Also give some Examples?"
c= "answersheet/answersheet1.txt"                 
    