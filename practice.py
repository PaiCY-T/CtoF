password = 'a123456'
i = 0
while i <3:
	mode = input('請輸入密碼，最多三次')
	if mode == password:
		print('密碼正確')
		break 
	else:
		print('還剩%d次機會'%(2 - i))
		i += 1

