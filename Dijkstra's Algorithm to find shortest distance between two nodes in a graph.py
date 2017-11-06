#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 02:02:29 2017

@author: naga
"""

# https://www.youtube.com/watch?v=gdmfOwyQlcI
from collections import defaultdict
from numpy import inf


#Nodes = ('1','2','3','4','5','6','7','8')
Nodes = ('A','B','C','D','E','F')

NeighborNodes = defaultdict(lambda: [])

def AddNode(StartNode,EndNode,Distance,Directed = False):
    NeighborNodes[StartNode].append((EndNode,Distance))
    if not Directed:
        NeighborNodes[EndNode].append((StartNode,Distance))
    

def Dijkstra(initialnode, goalnode):
    
    tempvalues= defaultdict(lambda: inf)
    tempvalues[initialnode]=0
    
    parentnodes = {}
    

    visitednodes = []
    unvisitednodes=list(Nodes)
    currentnode = initialnode
    parentnodes[currentnode] = currentnode
    
    
    while (currentnode not in visitednodes):
        
        for neighbor,edgedistance in NeighborNodes[currentnode]:
            if tempvalues[neighbor] > tempvalues[currentnode]+edgedistance:
                tempvalues[neighbor] = tempvalues[currentnode]+edgedistance
                parentnodes[neighbor] = currentnode
            
        visitednodes.append(currentnode)
        unvisitednodes.remove(currentnode)
    
        keyslist=[]
        valueslist=[]
    
        for node in unvisitednodes:
            keyslist.append(node) 
            valueslist.append(tempvalues[node])
        
        
        if len(unvisitednodes) !=0:
            currentnode = keyslist[valueslist.index(min(valueslist))]  
            
    

    #get the path
    start_path = initialnode
    end_path = goalnode
    path = [end_path]
    loopinitiation = True
    
    while (loopinitiation):
        if parentnodes[end_path] != start_path:
            path.append(parentnodes[end_path])
            end_path = parentnodes[end_path]
        else:
            loopinitiation = False
            path.append(start_path)
            path.reverse()
        
        
    print("Shortest distance between ",
          initialnode," and " ,goalnode," is ",tempvalues[goalnode])
    print("Path is: ",path)
    #print(tempvalues)
    #print(parentnodes)
    
    
# example showing usage of this code

AddNode('A','B',4)
AddNode('A','C',3)
AddNode('A','E',7)
AddNode('B','C',6)
AddNode('B','D',5)
AddNode('C','D',11)
AddNode('C','E',8)
AddNode('D','E',2)
AddNode('D','F',2)
AddNode('D','G',10)
AddNode('E','G',5)
AddNode('F','G',3)
    
# To obatain shortest distance between nodes A and F use:

Dijkstra('A','F')
  
# There is an optional fourth argument to AddNode function 
# to change the connection to Directed or Undirected. 


# If the nodes are labelled with numbers use the format below.

#AddNode('6','1',7)
#AddNode('6','3',3)
#AddNode('1','3',4)
#AddNode('1','2',3)
#AddNode('1','4',7)
#AddNode('1','7',8)
#AddNode('2','3',4)
#AddNode('2','4',1)
#AddNode('2','5',8)
#AddNode('2','7',3)
#AddNode('3','4',6)
#AddNode('4','5',2)
#AddNode('5','7',4)
#AddNode('5','8',6)
#AddNode('4','7',5)
#AddNode('7','8',9)
  


#AddNode('1','6',7)
#AddNode('3','6',3)
#AddNode('3','1',4) 
#AddNode('2','1',3)
#AddNode('4','1',7)
#AddNode('7','1',8)
#AddNode('3','2',4)
#AddNode('4','2',1)
#AddNode('5','2',8)
#AddNode('7','2',3)
#AddNode('4','3',6)
#AddNode('5','4',2)
#AddNode('7','5',4)
#AddNode('8','5',6)
#AddNode('7','4',5)
#AddNode('8','7',9)

