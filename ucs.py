# -*- coding: utf-8 -*-
import common_methods as common
import heapq
import itertools

def  ucs(max_height, current_state, goal):
    #parse the state and goal to a separate matrix
    current_state_matrix = common.saveMatrix(current_state)
    goal_matrix = common.saveMatrix(goal)
    
    visited = []
    path = []
    cost = 0
    
    priority_queue = [(cost, path, current_state_matrix)]
    
    while priority_queue:
        
        cost, path, current_state = heapq.heappop(priority_queue)
        
        if common.equal(current_state, goal_matrix):
            print(cost)
            for i in path:
                if i != path[-1]:
                    print(i, end="")
                    print("; ", end="")
                else:
                    print(i)
            return path
        else:
            movements = list(itertools.permutations(range(0, len(current_state)), 2))
            
            if current_state not in visited:
                child = common.children(cost, current_state, movements, path, max_height)
                
                for x in child:
                    heapq.heappush(priority_queue, x)
                    
                visited.append(current_state)
    print("No solution found")
        

if __name__== "__main__":
    
# =============================================================================
#     #Local tests
#     lines = ['3','(A); (B); (C); ()','(); (A); (B); (C)']
#     lines = ['1','(A); (B); ()','(A, B); (); ()']
#     lines = ['2','(A); (B); ()','(A, B); X; X']
#     lines = []
#     
#     #Parse lines of the input
#     for line in fileinput.input():
#         lines.append(line)
#     
#     max_height = int(lines[0])
#     current_state = lines[1]
#     goal = lines[2]
# =============================================================================
    
    max_height = int(input())
    current_state = input()
    goal = input()
    
    #Call UCS method
    ucs(max_height, current_state, goal)