#else if 練習
age = int(input('請輸入年紀：'))
if age < 13:
	print('國小')
elif age >= 13 and age < 15:
	print('國中')
elif age >= 15 and age < 18:
	print('高中')
elif age >= 18 and age < 22:
	print('大學')
else :
	print('社會人士')