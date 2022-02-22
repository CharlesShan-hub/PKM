import sys
import os
import json
""" 设置快捷命令方式
	在bashrc中保存命令，alias PKM-Operate="cd xxx;pyhton3 build.py"
"""
BASE_PATH = '../../KnowledgeMap'
PATH = BASE_PATH
hide=[]
block={}

def get_all_file(path,ignore=True):
	''' 获取某路径下的所有html文件路径名
	'''
	global hide
	temp=[]

	for item in os.listdir(path):
		if os.path.splitext(item)[-1][1:] == "html":
			temp.append(path+'/'+item)
		elif (path+'/'+item).replace(PATH,'') in hide and ignore==True:
			print("ignor "+path+'/'+item)
		elif os.path.isdir(path+'/'+item) == True:
			if item=='resources':
				pass
			else:
				temp.extend(get_all_file(path+'/'+item,ignore))
	return temp


def show_tree(command_list):
	''' 展示html目录结构
	'''
	global PATH
	global BASE_PATH
	if '-path' in command_list:
		number = command_list.index('-path')
		if len(command_list)-1 == number:
			PATH = BASE_PATH
		else:
			if os.path.exists(BASE_PATH+command_list[command_list.index('-path')+1])==False:
				print("没有路径:",BASE_PATH+command_list[command_list.index('-path')+1])
			else:PATH = BASE_PATH+command_list[command_list.index('-path')+1]

	if  '-p' in command_list:
		for item in get_all_file(PATH,'-all' not in command_list):
			temp=item.replace(PATH,'')
			print(temp)
	elif ('-p' not in command_list and '-l' not in command_list) or '-l' in command_list:
		first=True
		for item in get_all_file(PATH,'-all' not in command_list):
			temp=item.replace(PATH,'')
			temp=temp.replace('notes/','')
			if first or len(last_list)>len(temp.split('/')):
				first=False
				last_list=temp.split('/')
				print(temp)
			else:
				temp_list=temp.split('/')
				#print(last_list)
				for i in range(len(temp_list)):
					if i>=len(last_list):
						print(temp_list[i],end='')
						if i!=len(temp_list)-1:
							print('/',end='')
					elif temp_list[i]==last_list[i]:
						print('一'*len(temp_list[i])+'/',end='')
					else:
						print(temp_list[i],end='')
						if i!=len(temp_list)-1:
							print('/',end='')
				print()
				last_list=temp.split('/')




def hide_operation(command_list):
	''' 隐藏功能参数
	'''
	global hide
	if len(command_list)<2 or command_list[1]=='list':
		''' 展示隐藏列表
		'''
		for item in hide:
			print(item)
		if len(hide)==0:
			print("并未进行任何隐藏展示的设置")
	elif command_list[1]=='add' and len(command_list)>2:
		ans = input("确认忽略路径: "+PATH+command_list[2]+'  ? [Y/N]:')
		if ans[0]!='Y':
			return
		with open('./setting.json','r') as f:
			data = f.read()
		data = json.loads(data)
		data['hide'].append(command_list[2])
		hide.append(command_list[2])
		data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
		with open('./setting.json','w') as f:
			f.write(data)

	elif command_list[1]=='reduce' and len(command_list)>2:
		ans = input("确认取消忽略路径: "+PATH+command_list[2]+'  ? [Y/N]:')
		if ans[0]!='Y':
			return
		with open('./setting.json','r') as f:
			data = f.read()
		data = json.loads(data)
		if command_list[2] in data['hide']:
			data['hide'].remove(command_list[2])
			hide.remove(command_list[2])
			data = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
			with open('./setting.json','w') as f:
				f.write(data)
		else:
			print(command_list[2]+' 并不在忽略列表中')


def block_operation(command_list):
	'''
	'''
	print("试运行模块")
	if command_list[1]=='add':
		pass
	elif  command_list[1]=='reduce':
		pass
	pass


def init():
	if os.path.exists('./setting.json') == False:
		data = json.dumps({'hide': [],'block':{}}, sort_keys=True, indent=4, separators=(',', ': '))
		with open('./setting.json','w') as f:
			f.write(data)

	with open('./setting.json','r') as f:
		data = f.read()
	data = json.loads(data)
	global hide
	hide=data['hide']
	global block
	block=data['block']


def main():
	'''
	'''
	#print(sys.argv[1:])
	print("PKM Operater\n",end='')
	command_history=[]
	while 1:
		command=input(">>>")
		command_history.append(command)
		command_list=[]
		for item in command.split(" "):
			if item!='':
				command_list.append(item)
		if len(command_list)==0:
			continue
		if command=="exit":
			break
		elif command=="help":
			print("exit: 退出程序\n"\
				"clear: 清空屏幕\n"\
				"show: 检查所有拥有html的目录结构(PKM文件夹)\n"\
				"show -l:按照逻辑结构展示\n"\
				"show -p:按照物理结构展示\n"\
				"show -path: 展示指定目录的结构\n"\
				"show -all: 展示指定目录的结构\n"\
				"hide\n"\
				"hide list:取消展示的目录\n"\
				"hide add: 增加取消展示的目录\n"\
				"hide reduce: 减少某取消展示的目录")
		elif command=='clear':
			os.system("clear")
			print("PKM Operater\n",end='')
		elif command.split(" ")[0]=="show":
			show_tree(command_list)
		elif command_list[0]=="hide":
			hide_operation(command_list)
		elif command_list[0]=="block":
			block_operation(command_list)
		else:
			print("type `help` to see what can do")
		#else:
		#	print(command)


if __name__ == '__main__':
	init()
	main()