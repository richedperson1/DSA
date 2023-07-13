def twoOddNum( Arr, N):
    bitCheck = 0
    
    for data in Arr:
        bitCheck =bitCheck ^ data

    newBit = bitCheck & (bitCheck+1)
    x = 0
    y = 0
    for data in Arr:
        if data & newBit:
            x =x^data
        else:
            y =y^data
    
    return x,y

def printTwoOdd(arr, size):
     
    xor2 = arr[0]
     
    set_bit_no = 0 
    x, y = 0, 0

    for i in range(1, size):
        xor2 = xor2 ^ arr[i]
 
    # set_bit_no = xor2 & ~(xor2 - 1)
    ind = 1
    while ind<=xor2:
        if ind&xor2!=0:
            break
        ind<<=1
    
    set_bit_no = ind
    for i in range(size):

        if(arr[i] & set_bit_no):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
 
    print("The two ODD elements are", x, "&", y)
    return
arr = [2,2,3,1,4,4]
arr_size = len(arr)
print(twoOddNum(arr, arr_size))
(printTwoOdd(arr, arr_size))

