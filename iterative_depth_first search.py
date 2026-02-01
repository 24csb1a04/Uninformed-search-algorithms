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
    def dfs_traversal(self , root, target , curr , depth_limit):
        if(curr>depth_limit): return False
        if(self.vis[root]==1): return False
        self.vis[root] = 1
        self.dfs_order.append(root)
        if(self.vertex_name[root] == target): return True
        for j in range(self.n):
            if(self.adj[root][j]==1 and self.vis[j] == False):
                if(self.dfs_traversal(j , target , curr+1 , depth_limit)): return True
        return False
    def iterative_depth_first_search(self , root = 0 , target = 0):
        self.dfs_order = []
        self.vis = [0]*self.n
        if(root not in self.vertex_name.values()): return []
        root = [x for x  in self.vertex_name.keys() if self.vertex_name[x] == root][0]
        for i in range(self.n+1):
            k = self.dfs_traversal(root , target , 0, i)
            if(k==True): return ([self.vertex_name[x] for x in self.dfs_order] , i)
            else: 
                self.dfs_order =[]
                self.vis = [0]*self.n
        return []
def main():        
    g = Graph(['A' , 'B' , 'C' ,'D' , 'E' , 'F'] , False , ('A','B') , ('B','D') , ('B','E') , ('B','F'), ('A','C'))
    ans = g.iterative_depth_first_search(root = 'A' , target = 'C') 
    if(len(ans)==0): print("No path found")
    else: print("Traversal order: " , ans[0] , " depth: " , ans[1])
main()