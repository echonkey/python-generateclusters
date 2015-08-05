#-*- coding:UTF-8 -*-
'''
Created on 2015年8月3日

@author: Shixian Lei
'''

from math import sqrt
import jieba
import jieba.analyse
from optparse import OptionParser
from numpy.core.numeric import zeros

class ClusterBase:
    '''
    Basic Cluster
    '''
    __content={}

    def __init__(self,c):
        '''
        Constructor
        '''
        self.__content=c
    
    def importData(self):
        keyWords=[]
        keyWordList=[]
        for i in range(len(self.__content)):            
            keyWords[i]=list(jieba.analyse.extract_tags(self.__content[i], topK=10,withWeight=True))
            for j in range(len(keyWords)):
                if keyWords[j][0] not in keyWordList:
                    keyWordList.append(keyWords[j][0])
        
        wordTfIdf=zeros([len(keyWords),len(keyWordList)])
        for m in range(len(keyWords)):
            if keyWords[m][0] in keyWordList:
                n=keyWordList.index(keyWords[m][0])
                wordTfIdf[m][n]=keyWords[m][1]
        
        return keyWordList,wordTfIdf
    
    def pearson_distance(self,vector1, vector2) :
    
        sum1 = sum(vector1)
        sum2 = sum(vector2)

        sum1Sq = sum([pow(v,2) for v in vector1])
        sum2Sq = sum([pow(v,2) for v in vector2])

        pSum = sum([vector1[i] * vector2[i] for i in range(len(vector1))])

        num = pSum - (sum1*sum2/len(vector1))
        den = sqrt((sum1Sq - pow(sum1,2)/len(vector1)) * (sum2Sq - pow(sum2,2)/len(vector1)))

        if den == 0 : return 0.0
        return 1.0 - num/den
    
    def buildCluster(self):
        print("buildCluster----->Start")
    
    def printCluster(self):
        print("printCluster")
        

if __name__ == '__main__' :
    CB=ClusterBase({})
    CB.buildCluster()