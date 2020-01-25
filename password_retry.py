password = 'a123456'
print('請輸入密碼,最多輸入3次')

count = int(3)
while count > 0:
	pwd = input('請輸入密碼:')
	if pwd != password:
		count -= 1
		print('密碼錯誤! 還有%d次機會' % (count))
	else:
		print('登入成功')
		break