import os
import shutil

FROM_PATH='../..'
TO_PATH='../../../CharlesShan-hub.github.io'

ignore_path=[
	#'/KnowledgeMap/计算机科学/计算机网络',
	#'/KnowledgeMap/计算机科学/计算机组成原理',
	#'/KnowledgeMap/计算机科学/操作系统',
	#'/KnowledgeMap/计算机科学/数据结构',
	#'/KnowledgeMap/计算机科学/以太坊',
	#'/KnowledgeMap/计算机科学/密码学',
	#'/KnowledgeMap/计算机科学/JSON',
	#'/KnowledgeMap/计算机科学/YAML',
	'/KnowledgeMap/文史哲',
	'/.git',
	'/PKMViewer',
	'/PKM-plug-in',
	'/KnowledgeMap/读书'
	] # 都是忽略文件夹！

CSS_SRC = '''<link rel="stylesheet" type="text/css" href="style.css">
<link rel="stylesheet" type="text/css" href="../style.css">
<link rel="stylesheet" type="text/css" href="../../style.css">
<link rel="stylesheet" type="text/css" href="../../../style.css">
<link rel="stylesheet" type="text/css" href="../../../../style.css">
<link rel="stylesheet" type="text/css" href="../../../../../style.css">'''

for i in range(len(ignore_path)):
	ignore_path[i]=FROM_PATH+ignore_path[i]


def get_all_file(path):
	''' 获取某路径下的所有html文件路径名
	'''
	temp=[]
	for item in os.listdir(path):
		if os.path.splitext(item)[-1][1:] == "html":
			temp.append(path+'/'+item)
		elif path+'/'+item in ignore_path:
			print("ignor "+path+'/'+item)
		elif os.path.isdir(path+'/'+item) == True:
			if item=='resources':
				pass
			else:
				temp.extend(get_all_file(path+'/'+item))
	return temp


def get_all_resources(path):
	''' 获取某路径下的所有resources(不含其中的extension文件夹)文件
	'''
	temp=[]
	for item in os.listdir(path):
		if path+'/'+item in ignore_path or item=='.DS_Store':
			print("ignor "+path+'/'+item)
		elif os.path.isdir(path+'/'+item) == False:
			temp.append(path+'/'+item)
		elif os.path.isdir(path+'/'+item) == True:
			if item=='extension':
				pass
			else:
				temp.extend(get_all_file(path+'/'+item))
	return temp


def main():
	'''
	'''
	## README.md
	with open(FROM_PATH+'/index.md','r') as f:
		temp = f.read()
		with open(TO_PATH+'/README.md','w') as to_f:
			to_f.write(temp.replace(".md'>",".html'>"))
		with open(FROM_PATH+'/README.md','w') as to_f:
			to_f.write(temp.replace(".md'>",".html'>"))


	## notes
	if not os.path.exists(FROM_PATH):
		os.makedirs(FROM_PATH)

	files=get_all_file(FROM_PATH)

	ignore_resources=[]
	
	print("Number of files",len(files))
	for file in files:
		resources_file_base_path=os.path.dirname(file)+'/resources'
		print('check',resources_file_base_path)
		if os.path.exists(resources_file_base_path):
			if resources_file_base_path not in ignore_resources:
				ignore_resources.append(resources_file_base_path)
				if os.path.exists(resources_file_base_path.replace(FROM_PATH,TO_PATH))==False:
					os.makedirs(resources_file_base_path.replace(FROM_PATH,TO_PATH))
				res_files=get_all_resources(resources_file_base_path)
				print(res_files)
		for res_file in res_files:
			shutil.copyfile(res_file, res_file.replace(FROM_PATH,TO_PATH))
		to_file=file.replace(FROM_PATH,TO_PATH)
		print("Building "+to_file)
		with open(file,'r') as f:
			temp = f.read()
			style_index_l = temp.find('<style ')
			style_index_r = temp.find('</style>')
			temp = temp[:style_index_l]+CSS_SRC+temp[style_index_r+8:]
			#print(temp[:style_index_l]+CSS_SRC+temp[style_index_r+8:])
			#print(temp[style_index_l],
			#	temp[style_index_r+7])
			#temp = 
			with open(to_file,'w') as to_f:
				to_f.write(temp.replace(".md'>",".html'>"))

if __name__ == '__main__':
	main()