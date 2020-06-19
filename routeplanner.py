# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 03:15:17 2020

@author: Zixia Xu
"""

import math
from queue import PriorityQueue
#bulit path class,contains:value[],past cost:g,estimeted distance h and total cost:f
#built a PriorityQueue, each element contains:total cost f and path
#Using PriorityQueue can get smallest path

def cal_dist(cur_pos, next_pos):
    return math.sqrt((next_pos[0]-cur_pos[0])**2+(next_pos[1]-cur_pos[1])**2)

class Path:
    def __init__(self, start,goal):
        self.goal = goal
        self.value=[start]
        self.frontier = None        
        self.g = 0 #past cost
        self.h = None #estimeted distance
        self.f = 0 #total cost
        self.completed = False
    def add_pos(self,new_pos):
        self.value.append(new_pos)
        self.frontier = self.value[-1]        
        return
    def set_value(self,value):
        self.value = value.copy()
    def update_g(self,M,g):
        cur_pos = self.value[-2]
        next_pos = self.value[-1]
        self.g = g+cal_dist(M.intersections[cur_pos], M.intersections[next_pos])
        return
    def update_h(self,M):
        next_pos = self.value[-1]
        self.h = cal_dist(M.intersections[next_pos], M.intersections[self.goal])
        return
    def update_f(self):
        self.f = self.g+self.h
    def is_reachgoal(self):
        if self.frontier == self.goal:
            self.completed = True

def shortest_path(M, start, goal):
    #initialize a PriorityQueue
    if start == goal:
        return [start]
    mincost = float('inf')
    explored = set()
    explored.add(start)
    est_paths = PriorityQueue()
    completed_paths = PriorityQueue()
    mincost = float('inf')
    #put neighbors of start into PriorityQueue to initialize primordial path queue
    first_next_pos = M.roads[start]
    for pos in first_next_pos:
        explored.add(pos)
        path = Path(start,goal)
        path.add_pos(pos)
        path.update_g(M,0)
        path.update_h(M)
        path.update_f()
        path.is_reachgoal()
        est_paths.put((path.f,path))
    def Update_est_paths(mincost):
        #print(explored)
        for pos in next_pos:
            #print("iter1:"+str(pos))
            if pos not in explored:
                new_path = Path(start,goal)
                new_path.set_value(short_path.value)
                #print("iter2:"+str(pos))
                new_path.add_pos(pos)
                new_path.update_g(M,short_path.g)
                new_path.update_h(M)
                new_path.update_f()
                new_path.is_reachgoal()               
                if not new_path.completed:
                    #print(new_path.value,new_path.f)
                    est_paths.put((new_path.f,new_path))
                else:
                    completed_paths.put((new_path.f,new_path.value))                   
                    if new_path.f<mincost:                    
                        mincost=new_path.f 
        return mincost
    #continue generating possible paths 
    #if the remainder total cost are all larger than current mincost
    #break early
    cur_f = -float('inf')
    while cur_f < mincost:
        #i+=1
        #if i==8:
            #return est_paths
        cur_f,short_path = est_paths.get()  
        #print(short_path.value)
        explored.add(short_path.frontier)
        #print(short_path.frontier)
        next_pos = M.roads[short_path.frontier]
        mincost = Update_est_paths(mincost)  
    #return est_paths           
    return completed_paths.get()[1]