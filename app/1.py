N = 3
M = 3
A = [ [0]*M for i in range(N) ]
A[2][0]=1
A[2][2]=1
print(A)
str1 = 0
stolb = 0
coord = [0,0]
#север + 1 stolb (0,1)
#Юг -1 stolb(0,-1)
#запад -1 str1 (-1,0)
#восток ++1 str1 (1,0)
nord = '0,1'

south = '0,-1'
west = '-1,0'
east = '1,0'
def calc(coord,side):
    side = side.split(',')
    for i in range(len(coord)):
        coord[i] += int(side[i])
    return coord
coord = calc(coord,nord)
coord = calc(coord,nord)
coord = calc(coord,west)
print(coord)