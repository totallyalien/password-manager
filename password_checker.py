x = (input("enter pasword in comma seprated form example: ee22?22,djdj^&@#882,.....   ")).split(",")
for y in x:
    temp = []
    for z in y:
        temp.append(z)

    capital_alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    small_alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
    sym = ["!", "@", "#", "$", "^", "&", "*", "(", ")", "_"]
    num = ["1", "2","3", "4", "5" , "6" , "7", "8", "9", "0"]



    is_capital = False
    is_small = False
    is_symbol = False
    is_number = False

    for a in temp:
        if a in capital_alp:
            is_capital = True
        elif a in small_alp:
            is_small = True
        elif a in sym:
            is_symbol = True
        elif a in num:
            is_number = True

    if (is_symbol == True) and (is_small==True) and (is_number == True) and (is_capital == True):
        print(y)
