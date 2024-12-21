



#concept

def get_binary_digits(num):
    # input is decimal number
    try:
        #num = 256
        q = int(num/2)
        r = num%2
        b = str(r)



        while q>1:
            num = q
            print(num)
            q = int(num/2)
            r = num%2
            b = str(r)+b
        b = str(1)+b

        return b


    except Exception as e:
        print("Error >>  ", str(e))
        return None



# get the decimal if binary number is given
def get_decimal_number(binary_num):
    l = len(binary_num)
    count = 0 
    decimal_num = 0 

    while l-count>=1:
        bit = binary_num[l-1-count]
        #print("bit >> ", bit)
        decimal_num += int(bit)*(2**count)
        #print("decimal_num >> ", decimal_num)
        count+=1
        #print("count >> ", count)

    return decimal_num


num = 200
binary_num = get_binary_digits(num)
print("binary_num >> ", binary_num)
decimal_num = get_decimal_number(binary_num)
print("decimal_num >> ",decimal_num)
