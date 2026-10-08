mapping = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]



def value(colors):
    first_string, second_string = colors[0], colors[1]
    return int(str(mapping.index(first_string)) + str(mapping.index(second_string)))
    
    

    
