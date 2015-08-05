#-*- coding:UTF-8 -*-
'''
Created on 2015��8��4��

@author: Lei shixian
'''
from ClusterBase import ClusterBase
import random

class LinkedCluter(ClusterBase):
    '''
    Kmeans Algorithm
    '''
    __content=[]
    __keyWords=[]
    __KCluster=2
    __ClusterCenters=[]

    def __init__(self, k,content,keyWords):
        '''
        Constructor
        '''
        self.__content=content
        self.__keyWords=keyWords
        self.__KCluster=k
    
    def buildCluster(self):
        ClusterBase.buildCluster(self)
        min_max_per_word = [ [min([row[i] for row in self.__content]), max([row[i] for row in self.__content])]  for i in range(len(self.__content[0]))]
        
        # generate k clusters randomly
        __ClusterCenters = []
        for i in range(self.__KCluster) :
            cluster = []
            for min_, max_ in min_max_per_word :
                cluster.append(random.random() * (max_ - min_) + min_)
            __ClusterCenters.append(cluster)
        
        lables = []
        matchs = [ [] for i in range(self.__KCluster)]
        lastmatchs = [ [] for i in range(self.__KCluster)]
        rounds = 100
        while rounds > 0 :
            matchs = [ [] for i in range(self.__KCluster)]
            print('round \t', rounds)
            for i in range(len(self.__content)) :
                bestmatch_cluster = None
                min_distance = 2.1
                for j in range(self.__KCluster) :
                    dis = ClusterBase.pearson_distance(__ClusterCenters[j], self.__content[i])
                    if dis < min_distance :
                        min_distance = dis
                        bestmatch_cluster = j
                matchs[bestmatch_cluster].append(i)
            self.printCluster(matchs)
            self.printCluster(lastmatchs)
            if matchs == lastmatchs : break
            lastmatchs = [[ item for item in matchs[i] ] for i in range(self.__KCluster)]
            
            # move the centroids to the average of their members
            for j in range(self.__KCluster) :
                avg = [0.0 for i in range(len(self.__content[0])) ]
                for m in matchs[j] :
                    vec = self.__content[m]
                    for i in range(len(self.__content[0])) :
                        avg[i] += vec[i]
                avg = [ item / len(self.__content[0]) for item in avg]
                __ClusterCenters[j] = avg
            rounds -= 1
    
    def printCluster(self,matchs):
        for i in range(len(matchs)) :
            print(i , '---->',)
            for item in matchs[i] :
                print(item)
            print("\n")
        print('-'*20)

