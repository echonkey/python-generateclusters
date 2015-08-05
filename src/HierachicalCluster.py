#-*- coding:UTF-8 -*-
'''
Created on 2015��8��4��

@author: Admin
'''
from ClusterBase import ClusterBase


class HierachicalCluster(ClusterBase):
    '''
    Hierachical Clustering Algorithm
    '''
    

    def __init__(self, vec,left=None,right=None,distance=0.0,id=None):
        '''
        each cluster node contains:
            its id(__id)
            its own data,mainly wordTFIDF(__content)
            distance between itself and the other(__distance)
            left node(__left)
            right node(__right)            
        '''
        self.__left = left
        self.__right = right
        self.__content = vec
        self.__id = id
        self.__distance = distance
        
    
    def buildCluster(self):
        #Initialize each content as a Hierachical Cluster
        hiclusters = [ HierachicalCluster(vec = self.__content[i], id = i ) for i in range(len(self.__content)) ]
        distances = {}
        flag = None;
        currentclusted = -1
        while(len(hiclusters) > 1) :
            min_val = 2;
            hiclusters_len = len(hiclusters)
            
            '''
            calculate distances between each two clusters,
            if d<minval,record the two clusters' id
            '''
            for i in range(hiclusters_len-1) :
                for j in range(i + 1, hiclusters_len) :
                    if distances.get((hiclusters[i].id,hiclusters[j].id)) == None:
                        distances[(hiclusters[i].id,hiclusters[j].id)] = ClusterBase.pearson_distance(hiclusters[i].vec,hiclusters[j].vec)
                    d = distances[(hiclusters[i].id,hiclusters[j].id)] 
                    if d < min_val :
                        min_val = d
                        flag = (i,j)
            bic1,bic2 = flag
            newvec = [(hiclusters[bic1].vec[i] + hiclusters[bic2].vec[i])/2 for i in range(len(hiclusters[bic1].vec))]
            newbic = HierachicalCluster(newvec, left=hiclusters[bic1], right=hiclusters[bic2], distance=min_val, id = currentclusted)
            currentclusted -= 1
            del hiclusters[bic2]
            del hiclusters[bic1]
            hiclusters.append(newbic)
        return hiclusters[0]
    
    def printCluster(self,cluster):
        print(cluster)
        