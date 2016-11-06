class mapinfo:
    def __init__(self, x1, x2):
        self.parent = x1
        self.data = x2
pos=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

node=[mapinfo(0,pos) for n in range(0,999999)]
node[645].parent,node[75742].data=node[75742].data,node[645].parent
print node[645].parent
print node[75742].data
