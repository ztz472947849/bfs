#import copy
# tz2u16
# 2016.11
# Normal BFS
class mapinfo:
    def __init__(self, x1, x2):
        self.parent = x1
        self.data = x2
#pos=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#my_map = {n: pos for n in range(9999999)}
class level:
    def __init__(self, x3, x4,x5):
        self.start= x3
        self.end= x4
        self.depth=x5

pos=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#my_map=[mapinfo(0,pos) for n in range(999999+1)]
my_map=[mapinfo(0,pos) for n in xrange(9999999)]
my_map[0].data=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,2,3,4]]
#
my_level=[level(0,0,n)for n in range(20)]
#tmpdata=pos

def move_up(mapdata):
    tmpmapdata=[row[:] for row in mapdata]
    for i in range(4):    # which is 0~3
        for j in range(4):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i-1][j] = tmpmapdata[i-1][j], tmpmapdata[i][j]
                return tmpmapdata
    #return tmpmapdata
def move_down(mapdata):
    tmpmapdata= [row[:] for row in mapdata]
    #tmpmapdata=copy.deepcopy(mapdata)
    #print 'tmp', tmpmapdata
    #print 'mapdata', mapdata1
    for i in range(4):    # which is 0~3
        for j in range(4):
            if (tmpmapdata[i][j]==4):
                #print 'i',i
                #print 'j',j
                tmpmapdata[i][j], tmpmapdata[i+1][j] = tmpmapdata[i+1][j], tmpmapdata[i][j]
                #t=tmpmapdata[i][j]
                #tmpmapdata[i][j] = tmpmapdata[i + 1][j]
                #tmpmapdata[i+1][j]=t
                #break
                return tmpmapdata
    #print 'tmp', tmpmapdata
    #print 'mapdata', mapdata1
    #return tmpmapdata
def move_left(mapdata):
    #tmpmapdata=copy.deepcopy(mapdata)
    tmpmapdata = [row[:] for row in mapdata]
    for i in range(4):    # which is 0~3
        for j in range(4):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i][j-1] = tmpmapdata[i][j-1], tmpmapdata[i][j]
                return tmpmapdata
    #return tmpmapdata
def move_right(mapdata):
    tmpmapdata = [row[:] for row in mapdata]
    #tmpmapdata=copy.deepcopy(mapdata)
    for i in range(4):    # which is 0~3
        for j in range(4):
            if (tmpmapdata[i][j]==4):
                tmpmapdata[i][j], tmpmapdata[i][j+1] = tmpmapdata[i][j+1], tmpmapdata[i][j]
                return tmpmapdata
    #return tmpmapdata

def check_move(row_agent,col_agent):
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
def get_agent(mapdata):
    for i in range(4):
        for j in range(4):
            if mapdata[i][j]==4:
                return i,j

#row =3
#col =3
def trace(mapnum):
    pass

flag_goal=False
#end = 0
#tail = 1
my_depth=0
#print my_map[0].data
#temp_check_bits=check_move(3,3)
while my_depth <= 20 and flag_goal!=True:
#while my_depth <= 3 and flag_goal != True:   #300levels 0~299
    #if goal(my_map[]):
     #   break
    already_run=0
    for valid_parent in range(my_level[my_depth].start, my_level[my_depth].end + 1):   #start to end
        #temp_check_bits = check_move(get_agent(my_map[valid_parent].data)[0],get_agent(my_map[valid_parent].data)[1])
        temp_check_bits = check_move(get_agent(my_map[valid_parent].data)[0], get_agent(my_map[valid_parent].data)[1])
        #print get_agent(my_map[valid_parent].data)[0],get_agent(my_map[valid_parent].data)[1]
        #print temp_check_bits
        temp_end = my_level[my_depth].end+1+already_run
        if temp_check_bits[0]: # up
            #print 'level:',my_depth,'map:',temp_end,'data:',my_map[temp_end].data
            my_map[temp_end].data = move_up(my_map[valid_parent].data) # move to temp end
            if goal(my_map[temp_end].data):
                flag_goal=True
                print 'Solution Found'
                print 'level:', my_depth, 'map:', temp_end, 'data:'  # , my_map[temp_end].data
                for row in my_map[temp_end].data:
                    print row
                #trace()
                break
            my_map[temp_end].parent=valid_parent # record parent
            print 'level:', my_depth, 'map:', temp_end#, 'data:', my_map[temp_end].data
            temp_end += 1 # inc. temp_end
            already_run +=1
            #print temp_end
            #print my_map[temp_end-1].data
            #print 'U'

        if temp_check_bits[1]: # down
            #print 'valid p',valid_parent
            #print my_map[valid_parent].data
            #print temp_check_bits
            my_map[temp_end].data = move_down(my_map[valid_parent].data)  # move to temp end
            if goal(my_map[temp_end].data):
                flag_goal=True
                print 'Solution Found'
                print 'level:', my_depth, 'map:', temp_end, 'data:'#, my_map[temp_end].data
                for row in my_map[temp_end].data:
                    print row
                #trace(temp_end)
                break
            my_map[temp_end].parent = valid_parent  # record parent
            print 'level:', my_depth, 'map:', temp_end#, 'data:', my_map[temp_end].data
            temp_end += 1  # inc. temp_end
            already_run += 1
            #print my_map[temp_end-1].data
            #print 'D'

        if temp_check_bits[2]: # left
            #print my_map[0].data
            my_map[temp_end].data = move_left(my_map[valid_parent].data)  # move
            if goal(my_map[temp_end].data):
                flag_goal=True
                print 'Solution Found'
                print 'level:', my_depth, 'map:', temp_end, 'data:'  # , my_map[temp_end].data
                for row in my_map[temp_end].data:
                    print row
                #trace(temp_end)
                break
            my_map[temp_end].parent=valid_parent
            print 'level:', my_depth, 'map:', temp_end#, 'data:', my_map[temp_end].data
            temp_end += 1
            already_run += 1
            #print 'L'
            #print my_map[temp_end-1].data

        if temp_check_bits[3]: # right
            my_map[temp_end].data = move_right(my_map[valid_parent].data)  # move to temp end
            if goal(my_map[temp_end].data):
                flag_goal=True
                print 'Solution Found'
                print 'level:', my_depth, 'map:', temp_end, 'data:'  # , my_map[temp_end].data
                for row in my_map[temp_end].data:
                    print row
                #trace(temp_end)
                break

            my_map[temp_end].parent = valid_parent  # record parent
            print 'level:', my_depth, 'map:', temp_end#, 'data:', my_map[temp_end].data
            temp_end += 1  # inc. temp_end
            already_run += 1
            #print 'R'
            #print my_map[temp_end-1].data

        my_level[my_depth+1].end=temp_end-1
        my_level[my_depth+1].start = my_level[my_depth].end + 1
    my_depth+=1
    #print
print 'test done'