#import pygame

p1pos = [0,0]
p1dir = "D"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def renderboard(tile):
    for i in range(len(tile)):
        row = tile[i]
        for j in row:
            print(f"{j} ", end = "")
        print()

def boardinit():
    #inits
    x100 = [] #row of length 64
    xy64 = [] # 64x64 tile

    #establishments

    for i in range(64):
        x64 = []  # row of length 64
        for i in range(64):
            x64.append("█")
        xy64.append(x64)

    #retarr construction
    retarr = []
    retarr.append(x64)
    retarr.append(x100)
    retarr.append(xy64)

    return retarr


def updatetile(pos,val,tile):
    x = pos[0]
    y = pos[1]
    row = tile[y]
    row[x] = val
    tile[y] = row
    return tile

def activatered(type,tier,dir,coord):
    x = coord[0]
    y = coord[1]
    if type == "M":
        if dir ==  "D":
            for i in range(tier):
                #print
                print(">")

        print("red move")
    if type == "A":
        #attack
        print("red attack")

    if type == "T":
        #turn
        print("red turn")

def activatecard(cardname,tier,dir,coord):
    if cardname[0] == "R":
        activatered(cardname[1],tier,dir,coord)

def clear8x8(x,y,xy64): #FUNCTION IS CURRENTLY BROKEN GRR
    for i in range(8):
        x64 = xy64[i+y]  # row of length 64
        for j in range(8+x):
            x64[j] = "O"
        xy64[i] = x64
    return x64

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x8,x64,xy64 = boardinit()
    renderboard(xy64)
    xy64 = clear8x8(0,0,xy64)

    print("ZZ")
    p1pos = [3,4]

    #xy88 = updatetile(p1pos,"V",xy64)
    #renderboard(xy64)
    activatecard("RM",2,p1dir,p1pos)
