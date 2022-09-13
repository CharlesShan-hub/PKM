import os
import time
import shutil

def path_valid(command):
	flag = True
	for item in ['"','/',':','*','<','>','|',',',' ']:
		if item in command:
			print("不能包含字符:"+item)
			flag = False
	return flag

def get_name():
	flag = True
	while flag:
		flag = False
		command = input('🤔 输入创建模块名称，生成readme模板(直接回车退出程序):')
		# 退出
		if command=='':
			print("\n👋 模块构建取消!")
			return False
		# 判断非法字符
		flag = not path_valid(command)
		# 成功返回
		if flag == False:
			return command

def get_time(title):
	content = input('\n😊 是否生成创建日期(Y/N):')
	if content in['Y','']:
		return '# '+title+'\n'+time.strftime("%Y.%m.%d", time.localtime())+'\n'
	else:
		return '# '+title+'\n'

def get_toc():
	content = input('\n🥹 是否生成toc目录(Y/N):')
	if content in['Y','']:
		return '[toc]'+'\n'
	else:
		return ''

def get_photo(title):
	content = input('\n😍 是否隐藏封面语句(Y/N/自定义文件名):')
	if content in['Y','']:
		hide = True
	else:
		hide = False

	content = input('\n😄 生成封面 '+'"./resources/'+title+'.png" (Y/N/自定义文件名):')
	if content in['Y','']:
		if hide:
			return '<!--!['+title+'导图概览](./resources/'+title+'.png)-->\n'
		else:
			return '!['+title+'导图概览](./resources/'+title+'.png)\n'
	elif content=='N':
		return ''
	else:
		if hide:
			return '<!--!['+title+'导图概览](./resources/'+content+'.png)-->\n'
		else:
			return '!['+title+'导图概览](./resources/'+content+'.png)\n'

def get_info():
	content = input('\n😋 是否生成"加粗,链接,斜体"图例说明(Y/N):')
	if content in['Y','']:
		return '图例说明\n**加粗：章标题**\n[链接：笔记超链接]()\n*斜体：题型/主要内容*\n'
	else:
		return ''

def get_ignorPH():
	content = input('\n😪 是否省略目录占位符(Y/N):')
	if content in['Y','']:
		return ''
	else:
		return '* 占位\n\t* 占位\n'

def get_intro():
	content = input('\n😝 是否生成介绍 '+'"本模块按照xxxx进行构建" (Y/N/自定义xxxx内容):')
	if content in['Y','']:
		return '## 介绍\n本模块按照xxxx进行构建\n'
	elif content=='N':
		return ''
	else:
		return '## 介绍\n本模块按照'+content+'进行构建\n'

def get_pan():
	content = input('\n🙂️ 是否生成网盘链接模板(Y/N):')
	if content in['Y','']:
		return '## 资源\n链接:\n如果资源失效请联系我\n'
	else:
		return '## 资源\n'

def get_ver():
	content = input('\n🙂️ 是否生成版本占位符(Y/N):')
	if content in['Y','']:
		return '## 版本\n * **V1 202x.xx.xx**\n按照xxxx进行整理，完成全部知识框架搭建'
	else:
		return '## 版本\n'

def main():
	print("【回答一些问题快速构建一个新模块的README部分】\n")
	# 获取模板名称
	title = get_name()
	if title == False: return False

	print("【以下选项回车默认同意】")
	# 获取时间选项
	content = get_time(title)
	# 获取目录选项
	content += get_toc()
	# 获取封面选项
	content += get_photo(title)
	# 获取图例选项
	content += get_info()
	# 获取介绍选项
	content += get_intro()
	# 获取网盘选项
	content += get_pan()
	# 获取版本选项
	content += get_ver()

	print("\n以下是模板内容\n==================================")
	print(content)
	print("==================================")
	creat = input('\n您是否要继续创建: README.md 以及对应目录 (Y/N):')
	if creat!='Y' and creat !='':
		print("\n👋 模块构建取消!")
		return False
	if(os.path.exists('./'+title+'/resources')):
		replace = input('\n./'+title+'已经存在,您是否要重新创建 (Y/N):')
		if(replace in ['Y','']): 
			shutil.rmtree('./'+title)
		else:creat!='N'
	if creat!='Y' and creat !='':
		print("\n👋 模块构建取消!")
		return False
	os.makedirs('./'+title+'/resources/extension')
	with open('./'+title+'/README.md','w')as f:
		f.write(content)
	print("\n🍺 模块构建完成!")

if __name__ == '__main__':
	main()