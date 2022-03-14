def ispow(num):
    while(num>1):
        #print(num)
        if(num&1 and num!= 1):
            return 0 
        num = num>>1
    return 1

print(ispow(24))