temp_type = int(input('如果是攝氏，請輸1，如果是華氏請輸入2'))
temp = int(input('輸入幾度'))
if temp_type == 1:
	temp = temp * 9 / 5 + 32
else:
	temp = (temp - 32) * 5 / 9
print(temp)