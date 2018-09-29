#import warnings
#warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim
import os
import nltk
import sys

#nltk.download('averaged_perceptron_tagger')
#nltk.download('stopwords')
#nltk.download('punkt')


from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import pymysql
# from checkwindow import Ui_checkwindow
# from checkwindow import *

# import checkwindow
studentcopy=""

#from checkwindow import Ui_checkwindow
#from checkwindow import Ui_checkwindow

class gensim2class(object):
#     def anssheet(self):
#         global answersheet
#         answersheet=Ui_checkwindow.Browseanswersheet(checkwindow)
# #        print("anssheet foldername:",answersheet[0])
# #        print("anssheet file name",answersheet[1])
#     def stdcopy(self):
#         global studentcopy
#         studentcopy=Ui_checkwindow.Browsestudentcopy(checkwindow)
        
#        print("student foldername:",studentcopy[0])
#        print("student file name",studentcopy[1])
        
    
    def __init__():
        print("inside gensim2 fle")
        student="students/stdanswer1.txt"
        answersheet="teacher/answersheet1.txt"
        print("inside gensim2",answersheet)
        
        
        stop_words = set(stopwords.words("english"))
        
        lookup = "what is computer?"
        lookup2= "where are you taking the show?"
        lookup3= "what is pc?"
        
        
        with open(answersheet, 'r') as myFile:
            print("file open")
            for num, line in enumerate(myFile, 0):
                if lookup in line:
                    print('found at line:', num)
                    a=num
                    l=a+1
                if lookup2 in line:
                    print('found at line:', num)
                    b=num
                    m=b+1
                if lookup3 in line:
                    print('found at line:', num)
                    d=num
            e=num
            #print(num)
            c=answersheet                
            with open(c,'r') as myfile:
                raw_documents=myfile.readlines()[l:b]
                print(raw_documents)
                print("Number of documents:",len(raw_documents))
                raw_documents = [''.join(a for a in s if a not in string.punctuation) for s in raw_documents]
                print(raw_documents)
        
        
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
                print(ResultList)
                
                gen_docs = [[w.lower() for w in word_tokenize(word) if w not in stop_words] 
                              for word in ResultList]
                
                print(gen_docs)
                dictionary1 = gensim.corpora.Dictionary(gen_docs)
                #print(dictionary[2])
        #print(dictionary.token2id['road'])
                print("Number of words in dictionary1:",len(dictionary1))
                for i in range(len(dictionary1)):
                      print(i, dictionary1[i])
                      corpus1 = [dictionary1.doc2bow(gen_doc) for gen_doc in gen_docs]
                print(corpus1)
        
                tf_idf1 = gensim.models.TfidfModel(corpus1)
                print(tf_idf1)
                s = 0
                for i in corpus1:
                    s += len(i)
                print(s)
                sims1 = gensim.similarities.Similarity(answersheet,tf_idf1[corpus1],
                                                      num_features=len(dictionary1))
                print(sims1)
            
            stop_words = set(stopwords.words("english"))
        
            c= answersheet                
            with open(c,'r') as myfile:
                raw_documents=myfile.readlines()[m:d]
                print(len(raw_documents))
                print("Number of documents:",len(raw_documents))
                gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stop_words] 
                              for text in raw_documents]
                print(gen_docs)
                dictionary2 = gensim.corpora.Dictionary(gen_docs)
                #print(dictionary[2])
        #print(dictionary.token2id['road'])
                print("Number of words in dictionary2:",len(dictionary2))
                for i in range(len(dictionary2)):
                      print(i, dictionary2[i])
                      corpus2 = [dictionary2.doc2bow(gen_doc) for gen_doc in gen_docs]
                print(corpus2)
        
                tf_idf2 = gensim.models.TfidfModel(corpus2)
                print(tf_idf2)
                s = 0
                for i in corpus2:
                    s += len(i)
                print(s)
                sims2 = gensim.similarities.Similarity(answersheet,tf_idf2[corpus2],
                                                      num_features=len(dictionary2))
                print(sims2)
            c= answersheet               
            with open(c,'r') as myfile:
                raw_documents=myfile.readlines()[d+1:e]
                print(raw_documents)
                gen_docs = [[w.lower() for w in word_tokenize(text) if w not in stop_words] 
                               for text in raw_documents]
                print(gen_docs)
                dictionary3 = gensim.corpora.Dictionary(gen_docs)
                #print(dictionary[2])
        #print(dictionary.token2id['road'])
                print("Number of words in dictionary3:",len(dictionary3))
                
                for i in range(len(dictionary3)):
                      print(i, dictionary3[i])
                      corpus3 = [dictionary3.doc2bow(gen_doc) for gen_doc in gen_docs]
                print(corpus3)
                tf_idf3 = gensim.models.TfidfModel(corpus3)
                print(tf_idf3)
                s = 0
                for i in corpus3:
                    s += len(i)
                print(s)
                sims3 = gensim.similarities.Similarity(answersheet,tf_idf3[corpus3],
                                                          num_features=len(dictionary3))
                print(sims3)
                    
        
        
        
        
        lookup = "what is computer?"
        lookup2= "where are you taking the show?"
        lookup3= "what is pc?"
        inputdir = "students/"
        AllWords = list()      #create new list
        ResultList = list()   
        filelist = os.listdir(inputdir)
        for i in filelist:
            with open(inputdir + i, 'r') as myFile:
                for num, line in enumerate(myFile, 0):
                    if lookup in line:
                        print('found at line:', num)
                        a=num
                        l=a+1
                    if lookup2 in line:
                        print('found at line:', num)
                        b=num
                        m=b+1
                    if lookup3 in line:
                        print('found at line:', num)
                        d=num
                        e=num+1
                if a+1==b-1:
                    c= student                
                    with open(c,'r') as myfile:
                        line=myfile.readlines()[l]
                        #query_doc = [w.lower() for w in word_tokenize(line)]
                        query_doc = [w.lower() for w in word_tokenize(line) if w not in stop_words]
                        #print(query_doc)
                        query_doc_bow = dictionary1.doc2bow(query_doc)
                        #print(query_doc_bow)
                        query_doc_tf_idf = tf_idf1[query_doc_bow]
                        #query_doc_tf_idf+=query_doc_tf_idf
                        #print(query_doc_tf_idf)
                        a=sims1[query_doc_tf_idf]
                        a= a.round()                
                        print([a[i] for i, e in enumerate(a) if e != 0])                     
                        b+=[a[i] for i, e in enumerate(a) if e != 0]                  
        
                else:
                    c= student                
                    with open(c,'r') as myfile:
                         lines=myfile.readlines()[l:b]
                         lines = [''.join(a for a in s if a not in string.punctuation) for s in lines]
                         q=[]
                         AllWords = list()      #create new list
                         ResultList = list()
                         for line in lines:
                             line.rstrip()   #strip white space
                             words = line.split()    #split lines of words and make list
                             AllWords.extend(words)   #make the list from 4 lists to 1 list
        
                         AllWords.sort()  #sort list
        
                         for word in AllWords:   #for each word in line.split()
                               if word not in ResultList:    #if a word isn't in line.split            
                                     ResultList.append(word)   #append it.
                         #print(ResultList)
                             #query_doc = [w.lower() for w in word_tokenize(line) if w not in stop_words]
                             #print(query_doc)
                         query_doc = [w.lower() for w in ResultList if w not in stop_words]
        
                
        
                         print(query_doc)
                         query_doc_bow = dictionary1.doc2bow(query_doc)
                        #print(query_doc_bow)
                         query_doc_tf_idf = tf_idf1[query_doc_bow]
                         #print(query_doc_tf_idf)
                         #q= q+sims1[query_doc_tf_idf]
                         a=sims1[query_doc_tf_idf]
                         #print(sims1[query_doc_tf_idf])
        
                                #a= a.round()
                         #print([a[i] for i, e in enumerate(a) if a[i] !=0])                     
                         q=[a[i] for i, e in enumerate(a) if e != 0]  
                         print(sum(q)) 
                         
                        
                           
                         #print(q)    
                if b+1==d-1:
                    c= student                 
                    with open(c,'r') as myfile:
                        line=myfile.readlines()[m]
                        query_doc = [w.lower() for w in word_tokenize(line) if w not in stop_words]
                        #print(query_doc)
                        query_doc_bow = dictionary2.doc2bow(query_doc)
                        #print(query_doc_bow)
                        query_doc_tf_idf = tf_idf2[query_doc_bow]
                        #print(query_doc_tf_idf)
                        a=sims2[query_doc_tf_idf]
                        a= a.round()
                        print([a[i] for i, e in enumerate(a) if e != 0])                     
                             
                else:
                    c= student                 
                    with open(c,'r') as myfile:
                         lines=myfile.readlines()[m:d]
                         #r=[0,0]
                         for line in lines:
                             query_doc = [w.lower() for w in word_tokenize(line) if w not in stop_words]
                        #print(query_doc)
                             query_doc_bow = dictionary2.doc2bow(query_doc)
                        #print(query_doc_bow)
                             query_doc_tf_idf = tf_idf2[query_doc_bow]
                        #print(query_doc_tf_idf)
                             #r+=sims[query_doc_tf_idf]                
                             print(sims2[query_doc_tf_idf])
                             a=sims2[query_doc_tf_idf]
                             a= a.round()
                             print([a[i] for i, e in enumerate(a) if e != 0])                     
                             #print(r)
                if d<=e:
                    c= student                 
                    with open(c,'r') as myfile:
                        line=myfile.readlines()[e]
                        query_doc = [w.lower() for w in word_tokenize(line) if w not in stop_words]
                        #print(query_doc)
                        query_doc_bow = dictionary3.doc2bow(query_doc)
                        #print(query_doc_bow)
                        query_doc_tf_idf = tf_idf3[query_doc_bow]
                        #print(query_doc_tf_idf)
                        a=sims3[query_doc_tf_idf]
                        a= a.round()
                        print([a[i] for i, e in enumerate(a) if e != 0])                     
                        print("db journey started")   
                        print("hello world")             
        # conn=pymysql.connect(host="localhost",user="root" ,passwd="",db="test")
        # myCursor=conn.cursor()
        # myCursor.execute("INSERT INTO userinfo(Username,Password) Values('sana1','sanapasssword1');")
        # print("data inserted")
        # conn.commit()
        # conn.close()
                    
                           
        
      
    __init__()      
    print("function done")
    
