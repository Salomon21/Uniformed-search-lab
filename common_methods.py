# -*- coding: utf-8 -*-
import copy

def saveMatrix(string):
	matrix = []
	for i in string.split(';'):
		i = i.replace(' ', '')
		i = i.replace(')', '')
		i = i.replace('(', '')
		list = []
		for newVar in i.split(','):
			if newVar == '':
				continue
			else:
				list.append(newVar)

		matrix.append(list)
	return matrix


def equal(current_state, goal):
	counter = 0
	for index, i in enumerate(goal):
		if i != ['X']:
			if current_state[index] == goal[index]:
				counter += 1
	if counter == len(goal) - goal.count(['X']):
		return True
	return False

def children(cost, current_state, movements, path, max_height):
    children = []
    for i in movements:
        
        new_state = copy.deepcopy(current_state)
        cost2 = cost + 1 + abs(i[0] - i[1])
        path2 = copy.deepcopy(path)
        
        if not new_state[i[0]]:
            continue
        if len(new_state[i[1]]) >= max_height:
            continue
        
        value = (new_state[i[0]]).pop()
		
        new_state[i[1]].append(value)
        path2.append(i)
        
        children.append((cost2, path2, new_state))
    
    return children