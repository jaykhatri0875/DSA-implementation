def divide(a,b):
		# add your logic here
		cnt = 0
		while(b<=a):
			cnt += 1
            a = a^b
            ##print(a)
        #return a

print(divide(15,4))