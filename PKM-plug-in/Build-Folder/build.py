import os
import sys

# 生成的文件夹的根目录
FOLDER_BASE_PATH = './notes/'
#FOLDER_BASE_PATH = './'

# 设置缩进的空个数
blank_number = 2

# 设置暂存生成超链接的文本名称
TEMP_FILE = './temp.md'


def main():
	'''
	'''
	# 检查输入合法性
	if len(sys.argv) == 1:
		print("未指定文件, 请这样输入: python3 build.py example.md")
		return
	if len(sys.argv) > 2:
		print("参数过多, 只支持一个文件, 请这样输入: python3 build.py example.md")
		return


	# 初始化变量
	DRAFT_PATH = sys.argv[1]
	print("生成文件夹结构, 并重新构造文件",DRAFT_PATH)
	MD_PATH_LIST=[]


	# 构建文件夹结构
	with open(DRAFT_PATH,'r') as f:
		deep=[]
		deep_number=-1
		for line in f.readlines():
			line=line.strip('\n')
			deep_number=int(line.find('* ')/blank_number)
			while(len(deep)>deep_number):
				deep.pop()
			deep.append(line[line.find('* ')+2:])
			
			# 创建文件夹目录信息(后边会分辨哪些是真的哪些只是信息)
			PATH = FOLDER_BASE_PATH
			for item in deep:
				PATH=PATH+item+'/'
			PATH = PATH[:-1]

			# 创建文件夹中的.md文件信息(后边会分辨哪些是真的md哪些只是路径)
			MD_PATH = PATH+'.md'
			MD_PATH_LIST.append([deep_number,MD_PATH,deep[-1]])


	# 对.md列表进行标识后创建.md文件
	if len(MD_PATH_LIST)==1:
		MD_PATH_LIST[0].append(True)
	else:
		line_depth=-1
		for i in range(len(MD_PATH_LIST)):
			if(MD_PATH_LIST[i][0]>line_depth and i!=0):
				MD_PATH_LIST[i-1].append(False)
			else:
				MD_PATH_LIST[i-1].append(True)
			line_depth=MD_PATH_LIST[i][0]

	with open(TEMP_FILE,'w') as temp_f:
		for item in MD_PATH_LIST:
			if item[3]==True:
				if not os.path.exists(os.path.dirname(item[1])):
					os.makedirs(os.path.dirname(item[1]))
				if not os.path.exists(os.path.dirname(item[1])+'/resources'):
					os.makedirs(os.path.dirname(item[1])+'/resources')
				print("file: ",item[1])
				with open(item[1],'w') as f:
					f.write('# '+item[-2])
				temp_f.write(blank_number*item[0]*' '+'* ['+item[2]+']('+item[1]+')\n')
			else:
				temp_f.write(blank_number*item[0]*' '+'* '+item[2]+'\n')


if __name__ == '__main__':
	main()
