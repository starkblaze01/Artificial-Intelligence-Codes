from copy import deepcopy
import time
import sys

class State:
    shore = None                        
    boat = 0                            
    depth = 0                           
    path = None                         
    
    def __init__(self, s=[], b=0):
        self.shore = s
        self.boat = b
        self.depth = 0
        self.path = []
        
    def f(self):                        
        return self.depth + GoalTest(self)     
    
def handw(current):
    for i in range(0,noCouples):
        if current.shore[i] != current.shore[noCouples+i]:          
            for j in range(noCouples, noCouples*2): 
                    if(current.shore[j] == current.shore[i]):       
                        return 1
    return 0

def changePos(p):                                                  
    return abs(p - 1)

def isSameSide(state):
    people = deepcopy(state.shore)
    for i in range(0, len(state.shore)):
        if(state.shore[i] == state.boat):
            people[i] = 1
            
    return people   

def GoalTest(state):                                                       
    result = len(state.shore)
    for i in state.shore:
        result = result - i
    return result

def isVisited(state, searched):                                       
    for k in range(0, len(searched)):
        if state.shore == searched[k].shore and state.boat == searched[k].boat:
            return True
    return False
           
def moveGen(cap, state, movement, result, start):                     
    for i in range(start, len(state.shore)):
        if isSameSide(state)[i] == 1:                                   
            movement.append(i)                                      
            if cap > 1:                                             
                moveGen(cap-1, state, movement, result,i)              
            if cap == 1:                                           
                result.append(deepcopy(movement))                   
            movement.pop()                                          
    return result 

def expand(state): 
    following = deepcopy(state)
    result = [] 
    possible_moves = moveGen(boat_capacity, state, [], result,0)       
    for i in possible_moves:                                        
        following = deepcopy(state)
        for j in i:
            following.shore[j]  = changePos(state.shore[j])          
        following.boat = changePos(state.boat)                       
        if isVisited(following, searched):                            
            True
        elif handw(following):                                   
            searched.append(following)
        elif True:
            following.depth = following.depth + 1                   
            following.path.append(state)                            
            frontier.append(following)                              

def DFS(noStates):
    while True:
        noStates = noStates + 1
        print("Number of visited states: ", noStates)
        
        current = frontier.pop()                                
        
        if GoalTest(current) == 0:                                     
            return current                                      
        
        expand(current)                                         
        searched.append(current)                                                                        

if __name__ == '__main__':
    noCouples = 3
    boat_capacity = 2
 
    couple = [0,0]
    initial = State([], 0)
    goal = State([], 0)
    path = []
    frontier = []                                       
    searched = []                                       
    noStates = 0
    
    for i in range(0,noCouples):                        
        initial.shore.extend(couple)                    
    
    frontier.append(initial) 
    
    goal = DFS(noStates)
    
    print("\nSuccess: ", goal.shore, " reached")
    print("Depth: ", goal.depth)
    for i in goal.path:
        path.append(i.shore)
    print("Path: ", path)    
