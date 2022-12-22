#Finding the shortest route using Prims and Kruskals
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

#Prims Algorithm
def prims(v,g):
    V = v
    G = g
    selected = [0] * v
    no_edge = 0
    selected[0] = True
    Output = nx.Graph()
    while (no_edge < V - 1):
        minimum = float('inf')
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if ((not selected[j]) and G[i][j]):
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        Output.add_edge(x,y,weight=G[x][y])
        selected[y] = True
        no_edge += 1
    pos=nx.spring_layout(Output) 
    nx.draw_networkx(Output,pos)
    labels = nx.get_edge_attributes(Output,'weight')
    nx.draw_networkx_edge_labels(Output,pos,edge_labels=labels)
    plt.title("Best short path using Prims's Algorithm")
    plt.show()
    plt.close()

#Kruskal Algorithm
#Minimum cost using Kruskal's Algorithm
def kruskal(v,g):
    parent = [i for i in range(v)]
    V = v
    def find(i):
        while parent[i] != i:
            i = parent[i]
        return i
    def union(i, j):
        a = find(i)
        b = find(j)
        parent[a] = b
    def kruskalmst(cost):
        Output = nx.Graph()
        mincost = 0
        for i in range(V):
            parent[i] = i
        edge_count = 0
        while edge_count < V - 1:
            min = float('inf')
            a = -1
            b = -1
            for i in range(V):
                for j in range(V):
                    if find(i) != find(j) and (cost[i][j]!=0) and cost[i][j] < min:
                        min = cost[i][j]
                        a = i
                        b = j
            union(a, b)
            edge_count += 1
            mincost += min
            #Adding edge to the graph
            Output.add_edge(a,b,weight=cost[a][b])
        pos=nx.spring_layout(Output) 
        nx.draw_networkx(Output,pos)
        labels = nx.get_edge_attributes(Output,'weight')
        nx.draw_networkx_edge_labels(Output,pos,edge_labels=labels)
        plt.title("Best short path using Kruskal Algorithm")
        plt.show()
        plt.close()
        return mincost
    return kruskalmst(g)

#Input Graph
def inputgraph(matrix):
    Graph = nx.from_numpy_matrix(matrix)
    pos=nx.spring_layout(Graph) 
    nx.draw_networkx(Graph,pos)
    labels = nx.get_edge_attributes(Graph,'weight')
    nx.draw_networkx_edge_labels(Graph,pos,edge_labels=labels)
    plt.title("Input Graph")
    plt.show()
    plt.close()

cost = 0
#Input number of nodes
n = int(input("Enter the number of nodes : "))
arr=[]
#Adjacency Matrix
print("Enter the Adjacency Matrix : ")
for i in range(n):  
    row = list(map(int, input().split()))  
    arr.append(row)  
arr = np.array(arr)
#Calculating the total cost
for i in range(1,n+1):
    for j in range(1,n+1):
            cost += arr[i-1][j-1]
cost /= 2
print("Actual Cost : ", cost)
inputgraph(arr)
prims(n,arr) #Prims Algorithm
minicost = kruskal(n,arr) #Minimum cost obtained from Kruskal's Algorithm
print("Minimum cost obtained from Kruskal/Prim Algorithm : ", minicost)
print("Total distance saved using the above approach : ", cost-minicost)   

"""
Sample Input-1
4
0 4 5 6
4 0 3 2
5 3 0 5
6 2 5 0
"""
