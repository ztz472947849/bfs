from copy import deepcopy
def move_left(mapdata):
    tmpmapdata=list(mapdata)
    #new_list = list(old_list)
    for i in range(4):    # which is 0~3
        for j in range(4):
            if (tmpmapdata[i][j]==4):
                tmp=tmpmapdata[i][j]
                tmpmapdata[i][j]=tmpmapdata[i][j-1]
                tmpmapdata[i][j-1]=tmp
    return tmpmapdata
mapdata=[[0,0,0,0],[0,0,0,0],[0,4,0,0],[0,0,0,0]]
print mapdata
#dd = deepcopy(mapdata)
dd = [row[:] for row in mapdata]
print dd
print move_left(mapdata)
print dd
