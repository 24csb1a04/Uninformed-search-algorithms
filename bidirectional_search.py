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
    def bidirectional_search(self , root = 0 , target = 0):
        if(root not in self.vertex_name.values()): return []
        if(target not in self.vertex_name.values()): return []
        root = [x for x  in self.vertex_name.keys() if self.vertex_name[x] == root][0]
        target=[x for x  in self.vertex_name.keys() if self.vertex_name[x] ==target][0]
        q = []
        q.append([[root] , [target]])
        ans = []
        front_traversal = []
        back_traversal = []
        front_vis = [0]*self.n
        back_vis = [0]*self.n
        while(len(q)>0):
            front = q[0][0]
            back = q[0][1]
            q.pop(0)
            if(front_vis[front[-1]]==1 and back_vis[back[-1]]==1): continue
            front_vis[front[-1]] = 1
            back_vis[back[-1]] = 1
            if(front[-1]==back[-1]):
                ans = front+back[::-1][1:]
                front_traversal = front
                back_traversal = back
                break  
            front_candidates = []
            back_candidates = []
            for i in range(self.n):
                if(self.adj[front[-1]][i]==1 and front_vis[i]==0):
                    if(i==target):
                        ans = front + [i]
                        break
                    front_candidates.append(i)
            for j in range(self.n):
                if(self.adj[back[-1]][j]==1 and back_vis[j]==0):
                    if(j==target):
                        ans = [j]+back[::-1]
                        break
                    back_candidates.append(j)
            if(len(front_candidates)==0):
                if(len(back_candidates)==0): continue
                for c in back_candidates:
                    q.append([front , back+[c]])
            elif(len(back_candidates)==0):
                for c in front_candidates:
                    q.append([front+[c] , back])
            else:
                for c1 in front_candidates:
                    for c2 in back_candidates:
                        q.append([front+[c1] , back+[c2]])
        return [self.vertex_name[x] for x in ans] , [self.vertex_name[x] for x in front_traversal] , [self.vertex_name[x] for x in back_traversal] 
        
def main():        
    g = Graph(['A' , 'B' , 'C' ,'D' , 'E' , 'F'] , False , ('A','B') , ('B','D') , ('B','E') , ('B','F'), ('A','C'))
    ans = g.bidirectional_search(root = 'A' , target = 'E') 
    if(len(ans)==0): print("No path found")
    else: print("Traversal order: " , ans[0] , " front: " , ans[1] , " back: " , ans[2])
main()