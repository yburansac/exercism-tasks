import math
def point_distance(x,y):
    # calculate point distance from the center (0,0)

    r = math.pow(x,2) + math.pow(y,2)
    return math.sqrt(r)
    

def score(x, y):

    dist = point_distance(x,y)

    if dist <= 1:
        return 10
    if dist <= 5:
        return 5
    if dist <= 10:
        return 1
    return 0

    
