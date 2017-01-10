#A star
def u(mapdata):
    tmpmapdata=[row[:] for row in mapdata]
    for i in range(4):    # which is 0~3
        for j in range(4):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i-1][j] = tmpmapdata[i-1][j], tmpmapdata[i][j]
                return tmpmapdata
def d(mapdata):
    tmpmapdata= [row[:] for row in mapdata]
    for i in range(4):    # which is 0~3
        for j in range(4):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i+1][j] = tmpmapdata[i+1][j], tmpmapdata[i][j]
                return tmpmapdata
def l(mapdata):
    tmpmapdata = [row[:] for row in mapdata]
    for i in range(4):    # which is 0~3
        for j in range(4):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i][j-1] = tmpmapdata[i][j-1], tmpmapdata[i][j]
                return tmpmapdata
def r(mapdata):
    tmpmapdata = [row[:] for row in mapdata]
    for i in range(4):    # which is 0~3
        for j in range(4):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i][j+1] = tmpmapdata[i][j+1], tmpmapdata[i][j]
                return tmpmapdata
def get_agent(mapdata):
    for i in range(4):
        for j in range(4):
            if mapdata[i][j]==4:
                return i,j
def get_ABC(mapdata):
    A=[]
    B=[]
    C=[]
    for i in range(4):
        for j in range(4):
            if mapdata[i][j]==1:
                A = [i,j]
            if mapdata[i][j]==2:
                B = [i,j]
            if mapdata[i][j]==3:
                C = [i,j]
    return A,B,C
def check(mapdata):
    row_agent=get_agent(mapdata)[0]
    col_agent=get_agent(mapdata)[1]
    if (row_agent -1 >=0):
        check_up=True
    else:check_up=False
    if row_agent +1 <=3:
        check_down=True
    else:check_down=False
    if col_agent -1 >=0:
        check_left=True
    else: check_left=False
    if col_agent +1 <=3:
        check_right=True
    else: check_right=False
    return check_up,check_down,check_left,check_right
def goal(mapdata):
    if mapdata[1][1]==1 and mapdata[2][1]==2 and mapdata[3][1]==3:
        return True
def check_and_move(map):
    g=map.g+1
    rtn_data =[]
    reader= check(map.data)
    if reader[0]:
        udata=u(map.data)
        h=h_cost(udata)
        rtn_data.append(mapinfo(h+g,g ,h,udata,map))
    if reader[1]:
        ddata=d(map.data)
        h=h_cost(ddata)
        rtn_data.append(mapinfo(h+g,g ,h,ddata,map))
    if reader[2]:
        ldata=l(map.data)
        h=h_cost(ldata)
        rtn_data.append(mapinfo(h+g,g ,h,ldata,map))
    if reader[3]:
        rdata=r(map.data)
        h=h_cost(rdata)
        rtn_data.append(mapinfo(h+g,g ,h,rdata,map))
    return rtn_data
def man_dis(list1,list2):
    return abs(list1[0]-list2[0])+abs(list1[1]-list2[1])
def h_cost(mapdata):
    pos=get_ABC(mapdata)
    pos_agent=get_agent(mapdata)
    h_cost = (man_dis(pos_agent,pos[0])+2*man_dis(pos[0],[1,1]) if pos[0]!=[1,1] else 0) + (man_dis(pos_agent,pos[1])+2*man_dis(pos[0],[2,1]) if pos[1]!=[2,1] else 0) +(man_dis(pos_agent,pos[2])+2*man_dis(pos[0],[3,1]) if pos[2]!=[3,1] else 0)
    return h_cost
def h_cost2(map):
    pass

class mapinfo:
    def __init__(self,x0, x1, x2, x3,x4):
        self.f = x0
        self.g = x1
        self.h = x2
        self.data = x3
        self.came_from=x4
pos=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,2,3,4]]
my_map=mapinfo(0,0,0,pos,False)
#my_map[0].data=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,2,3,4]]
my_map.h=h_cost(pos)
my_map.f=my_map.h
def get_f(nodes):
    return nodes.f
def min_f(nodes):
    return sorted(nodes, key=get_f)[0]
def A_star(start):
    closedset = []
    openset = [start]
    while openset:
        x = min_f(openset)
        if goal(x.data):
            #return True
            for n in x.data:
                print n
            print ''
            return trace(x)
        openset.remove(x)
        closedset.append(x)
        for y in check_and_move(x):
            if y in closedset:
                continue
            tentative_g = x.g + 1

            if y not in openset:
                openset.append(y)
                tentative_better=True
            else:
                if tentative_g < y.g:
                    tentative_better = True
                else:
                    tentative_better = False
            if tentative_better:
                y.came_from=x
                y.g=tentative_g
                y.h=h_cost(y.data)
                y.f=y.g+y.h
    return False

def trace(current_node):
     if current_node.came_from:
         for n in current_node.came_from.data:
             print n
         #
         print ''
         #s=s+1
         trace(current_node.came_from)
     else:
         return

#print h_cost(pos)
A_star(my_map)
#    print 'Done'


