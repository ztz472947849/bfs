# iterative Deepening
def u(mapdata):
    tmpmapdata=[row[:] for row in mapdata]
    for i in range(4):    # which is 0~3
        for j in range(4):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i-1][j] = tmpmapdata[i-1][j], tmpmapdata[i][j]
                return tmpmapdata
    #return tmpmapdata
def d(mapdata):
    tmpmapdata= [row[:] for row in mapdata]
    for i in range(4):    # which is 0~3
        for j in range(4):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i+1][j] = tmpmapdata[i+1][j], tmpmapdata[i][j]
                return tmpmapdata
def l(mapdata):
    #tmpmapdata=copy.deepcopy(mapdata)
    tmpmapdata = [row[:] for row in mapdata]
    for i in range(4):    # which is 0~3
        for j in range(4):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i][j-1] = tmpmapdata[i][j-1], tmpmapdata[i][j]
                return tmpmapdata
    #return tmpmapdata
def r(mapdata):
    tmpmapdata = [row[:] for row in mapdata]
    #tmpmapdata=copy.deepcopy(mapdata)
    for i in range(4):    # which is 0~3
        for j in range(4):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i][j+1] = tmpmapdata[i][j+1], tmpmapdata[i][j]
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
def check_and_move(mapdata):
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

#root = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,2,3,4]]
#found = root


def IDDFS(root):
    #found = root
    for depth in range(12,16):
        found = DLS(root, depth)
        if found!=None:
            return found
def DLS(node, depth):
    if depth <= 0 or goal(node):
        return node
    if depth > 0:
            #child_set = check_and_move(node)
            for child in check_and_move(node):
                #print child
                found = DLS(child, depth-1)
                #print found
                if found!=None and goal(found):
                    print child
                    return found
root = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,2,3,4]]
found = root
IDDFS(root)
print root
#for cc in check_and_move(root):
#    print cc