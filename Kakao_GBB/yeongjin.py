import math
import random

gawi_theta = math.pi / 6 # 30degree
gawi_offset_x = math.cos(gawi_theta)
gawi_offset_y = math.sin(gawi_theta)
bawi_theta = math.pi * 5 / 6 # 150 degree
bawi_offset_x = math.cos(bawi_theta)
bawi_offset_y = math.sin(bawi.theta)
bo_theta = math.pi * 3 /2 # 270 degree
bo_offset_x = math.cos(bo_theta)
bo_offset_y = math.sin(bo_theta)
def show_me_the_hand(records) :
    cur_x = 0
    cur_y = 0
    for record in records :
        if(record[0] == 'gawi') :
            cur_x += gawi_offset_x
            cur_y += gawi_offset_y
        elif(record[0] == 'bawi') :
            cur_x += gawi_offset_x
            cur_y += gawi_offset_y
        else :
            cur_x += bo_offset_x
            cur_y += bo_offset_y
    if cur_x == 0 : cur_theta = 0
    else : cur_theta = math.atan(cur_y/cur_x)
    if cur_x < 0 : cur_theta += math.pi
    cur_theta += math.pi / 2
    if(math.pi / 6 <= cur_theta <= math.pi / 2) : # expect 'gawi'
        return 'bawi'
    elif(math.pi / 2 <= cur_theta <= math.pi * 7 / 6) : #expect 'bawi'
        return 'bo'
    else :
        return 'gawi'
    

