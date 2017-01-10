from Queue import *
import random
import sys
sys.setrecursionlimit(500000)
global noo
noo=0
#loop=0
def u(mapdata):
    tmpmapdata=[row[:] for row in mapdata]
    for i in range(N):    # which is 0~3
        for j in range(N):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i-1][j] = tmpmapdata[i-1][j], tmpmapdata[i][j]
                return tmpmapdata
    #return tmpmapdata
def d(mapdata):
    tmpmapdata= [row[:] for row in mapdata]
    for i in range(N):    # which is 0~3
        for j in range(N):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i+1][j] = tmpmapdata[i+1][j], tmpmapdata[i][j]
                return tmpmapdata
def l(mapdata):
    #tmpmapdata=copy.deepcopy(mapdata)
    tmpmapdata = [row[:] for row in mapdata]
    for i in range(N):    # which is 0~3
        for j in range(N):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i][j-1] = tmpmapdata[i][j-1], tmpmapdata[i][j]
                return tmpmapdata
    #return tmpmapdata
def r(mapdata):
    tmpmapdata = [row[:] for row in mapdata]
    #tmpmapdata=copy.deepcopy(mapdata)
    for i in range(N):    # which is 0~3
        for j in range(N):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i][j+1] = tmpmapdata[i][j+1], tmpmapdata[i][j]
                return tmpmapdata
    #return tmpmapdata
def get_agent(mapdata):
    for i in range(N):
        for j in range(N):
            if mapdata[i][j]==4:
                return i,j
def check(mapdata):
    row_agent=get_agent(mapdata)[0]
    col_agent=get_agent(mapdata)[1]
    if (row_agent -1 >=0):
        check_up=True
    else:check_up=False
    if row_agent +1 <=N-1:
        check_down=True
    else:check_down=False
    if col_agent -1 >=0:
        check_left=True
    else: check_left=False
    if col_agent +1 <=N-1:
        check_right=True
    else: check_right=False
    return check_up,check_down,check_left,check_right
def goal(mapdata):
    if mapdata[1][1]==1 and mapdata[2][1]==2 and mapdata[3][1]==3:
        return True
def neighbour(mapdata):
    rtn_data =[]
    reader= check(mapdata)
    if reader[0]:
        rtn_data.append(u(mapdata))
    if reader[1]:
        rtn_data.append(d(mapdata))
    if reader[2]:
        rtn_data.append(l(mapdata))
    if reader[3]:
        rtn_data.append(r(mapdata))
    return rtn_data
def start_node(N):
    row=[]
    grid=[]
    line=[1,2,3,4]
    for i in range(N):
        row.append(0)
    for j in range(N-1):
        grid.append(row)
    for k in range(N-4):
        line.append(0)
    grid.append(line)
    return grid
def bfs():
    ##sorted_maze = sorted(maze.tree)
    #for n in sorted_maze:
    #    depth_dict[n] = -1
    #    parent_dict[n] = -1
    #root=sorted_maze[0]
    root=start_node(N)
    depth_dict={}
    parent_dict={}
    #index=G_map.index(root)
    depth_dict[repr(root)] = 0
    parent_dict[repr(root)] = 'God'
    Q = Queue()
    Q.put(root)
    global loop,usedmaps
    loop=0
    usedmaps=0
    while Q.qsize():
            #print usedmaps
            loop = loop +1
            current = Q.get()
            if not goal(current):
                for n in neighbour(current):
                    if repr(n) not in depth_dict:
                        depth_dict[repr(n)] = depth_dict[repr(current)]+ 1
                        parent_dict[repr(n)] = repr(current)
                        Q.put(n)
                        usedmaps=usedmaps+2
            else: return trace(current,parent_dict)
def trace(node,parent_dict):
    #print 'Loop:',loop,'Map:',usedmaps
    #n=['Goal',node]
    m=repr(node)
    n = ['Goal', node]
    while n[-1]!='God':
        n.append(parent_dict[m])
        m=parent_dict[m]
    for r in n:
        print r
    return n
def re_dfs(mapdata,depth,ll):
    #depth=0
    v_rnd = random.SystemRandom().randint(0, 3)
    if goal(mapdata):
        print 'Solution found! \n',mapdata,'\nsteps token:',depth,' ',ll
        return
    if depth >= 4175:
        print 'Die <3'
    else:
        while check(mapdata)[v_rnd]!=True:
                v_rnd = random.SystemRandom().randint(0, 3)
                #v_rnd=random.randint(0,3)
        ll = ll+ len(check(mapdata))
        if v_rnd==0:
            depth+=1
            #print 'Up'
            re_dfs(u(mapdata),depth,ll)
            return
        if v_rnd==1:
            depth += 1
            #print 'Down'
            re_dfs(d(mapdata),depth,ll)
            return
        if v_rnd==2:
            depth += 1
            #print 'Left'
            re_dfs(l(mapdata),depth,ll)
            return
        if v_rnd==3:
            depth += 1
            #print 'Right'
            re_dfs(r(mapdata),depth,ll)
            return

def IDDFS(root):
            # found = root
            for depth in range(12, 90):
                found = DLS(root, depth)
                #print found
                if found != None:
                    return found

def DLS(node, depth):
            if depth <= 0 or goal(node):
                return node
            if depth > 0:
                # child_set = check_and_move(node)
                for child in neighbour(node):
                    global noo
                    noo = noo+len(neighbour(node))
                    # print child
                    found = DLS(child, depth - 1)
                   # print ll
                    if found != None and goal(found):
                        #print child
                        return found
#print start_node(4)
#loop=0
#inner_nodes = 0
#global noo
#noo=0
for N in range(4,9):
    bfs()
    #re_dfs(start_node(N),0,1)
    #IDDFS(start_node(N))
    #print noo
