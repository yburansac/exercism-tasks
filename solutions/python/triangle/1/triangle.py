def is_triangle(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False

    if not (a+b >= c) or not (b+c >= a) or not (a+c >= b):
        return False

    return True





def equilateral(sides):
    if not is_triangle(sides):
        return False

    if sides[0] == sides[1] and sides[1] == sides[2] and sides[0] == sides[2]: 
        return True
    return False
   
  

def isosceles(sides):
    if not is_triangle(sides):
        return False
    
    if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
        return True
    return False
   


def scalene(sides):   
    if is_triangle(sides):
        if not equilateral(sides) and not isosceles(sides):
            return True

    return False


