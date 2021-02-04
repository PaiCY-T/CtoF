import random as rnd 
x = rnd.randint(1,100)
print(x)
while True:
	y = int(input('猜數字吧'))
	if x != y:
		print('猜錯了')
	else:
		print('猜對了')
		break
