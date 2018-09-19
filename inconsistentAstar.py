# -*- coding: utf-8 -*-

# =============================================================================
# Juan Carlos Estebes González
# Salomón Olivera Abud
# =============================================================================
import common_methods as common
import heapq
import itertools
import fileinput
import random
import copy


def inconsistentHeuristic(current, goal):
    v = 0

    for index, i in enumerate(goal):
        if i != ['X']:
            if current[index] != goal[index]:
                v = v + 1

    return v + random.randrange(0,10)

def children(cost, current_state, movements, path, max_height, goal) :

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
        extracost = inconsistentHeuristic(new_state, goal)
        cost2 = cost2 + extracost
        path2.append(i)

        children.append((cost2, path2, new_state))

    return children


def inconsistentAStar(max_height, current, goal):

    #parse the state and goal to a separet matrix
    current_matrix = common.saveMatrix(current)
    goal_matrix = common.saveMatrix(goal)

    visited = []
    path = []
    cost = 0

    priority_queue = [(cost, path, current_matrix)]

    while priority_queue:

        cost, path, current_state= heapq.heappop(priority_queue)
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
                child = children(cost, current_state, movements, path, max_height, goal_matrix)
                for var in child:
                    heapq.heappush(priority_queue, var)

                visited.append(current_state)

    print("No solution found")

if __name__ == "__main__":

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
    current = input()
    goal = input()
    random.seed(max_height)

    #Call A* method
    inconsistentAStar(max_height, current, goal)
