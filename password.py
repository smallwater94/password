x = 0
while True:
	password = input('請輸入密碼: ')
	if password != '123':
		x = x + 1
		print('密碼錯誤 你還有',3 - x,'次機會')
		if x == 3:
			print('登入失敗')
			break
	else:
		input('登入成功')
		break