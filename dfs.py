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
        for i in range(self.n):
            l = []
            for j in range(self.n):
                if((self.vertex_name[i],self.vertex_name[j]) in edges): l.append(1)
                elif(self.directed == False and (self.vertex_name[j],self.vertex_name[i]) 
                     in edges): 
                    l.append(1)
                else : l.append(0)
            self.adj.append(l)
    def dfs_traversal(self , root = 0):
        if(self.vis[root]==1): return
        self.vis[root] = 1
        self.dfs_order.append(root)
        for j in range(self.n):
            if(self.adj[root][j]==1 and self.vis[j] == False):
                self.dfs_traversal(j)
        return
    def dfs(self , root = 0):
        self.dfs_order = []
        self.vis = [0]*self.n
        self.dfs_traversal(root)
        return [self.vertex_name[x] for x in self.dfs_order]
def main():        
    g = Graph(['A' , 'B' , 'C' ,'D' , 'E' , 'F'] , False , ('A','B') , ('B','D') , ('B','E') , ('B','F'), ('A','C'))
    ans = g.dfs()
    print("Traversal order: " , ans)
main()