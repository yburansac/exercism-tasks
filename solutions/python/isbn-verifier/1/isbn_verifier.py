


def is_valid(isbn):
    
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    

    checksum = 0
    d = 0
    
    for i in range(0, 10):
        if i == 9 and isbn[i] == "X":
            d = 10
        elif not isbn[i].isdigit():
            return False
        else:
            d = int(isbn[i])
            
        checksum += d * (10 - i)

    return checksum % 11 == 0  
        


    






    
    
