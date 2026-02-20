class Graph:
    def __init__(self , vertices , directed , *edges):
        self.n = len(vertices)
        self.vertex_name ={}
        idx = 0
        for vertex in vertices:
            self.vertex_name[idx] = vertex
            idx+=1
        self.directed = directed
        self.adj = []
        self.weights = {}
        for edge in edges:
            self.weights[edge[:2]] = edge[2]
        for i in range(self.n):
            l = []
            for j in range(self.n):
                if((self.vertex_name[i],self.vertex_name[j]) in self.weights.keys()): l.append(self.weights[(self.vertex_name[i],self.vertex_name[j])])
                elif(self.directed == False and (self.vertex_name[j],self.vertex_name[i]) 
                     in self.weights.keys()): 
                    l.append(self.weights[(self.vertex_name[j],self.vertex_name[i])])
                else : l.append(0)
            self.adj.append(l)
    def uniform_cost_search(self , root = 0 , target = 0):
       if(root not in self.vertex_name.values()): return -1
       if(target not in self.vertex_name.values()): return -1
       root = [x for x  in self.vertex_name.keys() if self.vertex_name[x] == root][0]
       target=[x for x  in self.vertex_name.keys() if self.vertex_name[x] ==target][0]
       q = []
       q.append([0 , root , [root]])
       self.vis = [0]*self.n
       while(len(q)>0):
           q.sort()
           top= q[0]
           q.pop(0)
           if(top[1]==target): return top[0] , [self.vertex_name[x] for x in top[2]]
           if(self.vis[top[1]] == 1): continue
           self.vis[top[1]] = 1
           for j in range(self.n):
                if(self.adj[top[1]][j]>0 and self.vis[j]==0): q.append([top[0]+self.adj[top[1]][j] , j , top[2]+[j]])
       return -1 , -1
            
def main():        
    g = Graph(['A' , 'B' , 'C' ,'D' , 'E' , 'F'] , False , ('A','B' , 1) , ('B','D' , 5) , ('B','E' , 3) , ('B','F' , 2), ('A','C' , 4))
    ans = g.uniform_cost_search(root = 'A' , target = 'F') 
    if(ans[0]==-1): print("No path found")
    else: print("Cost: " , ans[0] , "Path: " , ans[1])
main()