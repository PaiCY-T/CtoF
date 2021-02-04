import random as rnd 
x = rnd.randint(1,100)
print(x)
while True:
	y = int(input('猜數字吧'))
	if x > y:
		print('大一點')
	elif x < y:
		print('小一點')
	else:
		print('猜對了')
		break
