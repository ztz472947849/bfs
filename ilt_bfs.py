#recurisive DFS with limit
import random
import sys
sys.setrecursionlimit(500000)
depth=0
solu=[]
def u(mapdata):
    tmpmapdata=[row[:] for row in mapdata]
    for i in range(4):    # which is 0~3
        for j in range(4):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i-1][j] = tmpmapdata[i-1][j], tmpmapdata[i][j]
                solu.append('u')
                return tmpmapdata
    #return tmpmapdata
def d(mapdata):
    tmpmapdata= [row[:] for row in mapdata]
    for i in range(4):    # which is 0~3
        for j in range(4):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i+1][j] = tmpmapdata[i+1][j], tmpmapdata[i][j]
                solu.append('d')
                return tmpmapdata
def l(mapdata):
    #tmpmapdata=copy.deepcopy(mapdata)
    tmpmapdata = [row[:] for row in mapdata]
    for i in range(4):    # which is 0~3
        for j in range(4):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i][j-1] = tmpmapdata[i][j-1], tmpmapdata[i][j]
                solu.append('l')
                return tmpmapdata
    #return tmpmapdata
def r(mapdata):
    tmpmapdata = [row[:] for row in mapdata]
    #tmpmapdata=copy.deepcopy(mapdata)
    for i in range(4):    # which is 0~3
        for j in range(4):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i][j+1] = tmpmapdata[i][j+1], tmpmapdata[i][j]
                solu.append('r')
                return tmpmapdata
    #return tmpmapdata
def get_agent(mapdata):
    for i in range(4):
        for j in range(4):
            if mapdata[i][j]==4:
                return i,j
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
def find(mapdata,depth):
    #depth=0
    v_rnd = random.SystemRandom().randint(0, 3)
    if goal(mapdata):
        print 'Solution found! \n',mapdata,'\nsteps token:',depth,solu
        return
    if depth >= 4175:
        print 'Die <3'
    else:
        while check(mapdata)[v_rnd]!=True:
                v_rnd = random.SystemRandom().randint(0, 3)
                #v_rnd=random.randint(0,3)
        if v_rnd==0:
            depth+=1
            #print 'Up'
            find(u(mapdata),depth)
            return
        if v_rnd==1:
            depth += 1
            #print 'Down'
            find(d(mapdata),depth)
            return
        if v_rnd==2:
            depth += 1
            #print 'Left'
            find(l(mapdata),depth)
            return
        if v_rnd==3:
            depth += 1
            #print 'Right'
            find(r(mapdata),depth)
            return
mapdata_test=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,2,3,4]]
#depth=0
find(mapdata_test,depth)