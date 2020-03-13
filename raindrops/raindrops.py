def convert(number):
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return f"{number}"
    else: 
        str = ""
        if number % 3 == 0:
            str+= "Pling"
        if number % 5 == 0:
            str+= "Plang"
        if number % 7 == 0:
            str+= "Plong"
    return str
