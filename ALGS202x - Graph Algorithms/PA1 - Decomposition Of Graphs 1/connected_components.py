# python3
# Input: An integer (vert) for vertices
#        An integer (edge) for edges
#        Next lines (edges) are the vertices that are connected
# Output: The number of connected components

import sys

# Recursively search
def explore(AdjacentList, x, VisitedList):
    for i in AdjacentList[x]:
        if not VisitedList[i]:
            VisitedList[i] = True
            explore(AdjacentList, i, VisitedList)
    return VisitedList

def number_of_components(AdjacentList):
    # Initialize VistiedList and count
    VisitedList = [False]*len(AdjacentList)
    count = 0
    
    for i in range(len(AdjacentList)):
        if not VisitedList[i]:
            count += 1
            explore(AdjacentList, i, VisitedList)   
    return count

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    vert, edge = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 *edge):2], data[1:(2 *edge):2]))
    AdjacentList = [[] for _ in range(vert)]
    for (a, b) in edges:
        AdjacentList[a - 1].append(b - 1)
        AdjacentList[b - 1].append(a - 1)
    print(number_of_components(AdjacentList))
