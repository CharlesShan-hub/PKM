import os
import time

def main():
	command = input('输入创建模块名称，生成readme模板:')
	# 判断非法字符
	if command=='':
		return False
	for item in ['"','/',':','*','<','>','|',',',' ']:
		if item in command:
			return False
	# 确认用户创建
	creat = input('您是否要创建: ['+command+'] (Y/N):')
	if creat!='Y':
		return False
	# 创建模板文件
	content='# '+command+'\n'+time.strftime("%Y.%m.%d", time.localtime())+'\n'
	content+='## 目录\n'
	content+='!['+command+'导图概览](./resources/'+command+'.png)\n'
	content+='* A\n\t* B\n'
	content+='## 介绍\n本模块按照xxxx进行构建\n'
	content+='## 资源\n链接:\n如果资源失效请联系我\n'
	content+='## 版本\n'
	print(content)
	# 
	creat = input('您是否要继续创建: README.md 以及对应目录 (Y/N):')
	if creat!='Y':
		return False
	os.makedirs('./'+command+'/resources/extension')
	with open('./'+command+'/README.md','w')as f:
		f.write(content)


if __name__ == '__main__':
	main()