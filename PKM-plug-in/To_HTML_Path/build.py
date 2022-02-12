import os

WORK_PATH='../../../CharlesShan-hub.github.io'

flist = []



def get_all_file(path):
	''' 获取某路径下的所有html文件路径名
	'''
	temp=[]
	for item in os.listdir(path):
		if os.path.splitext(item)[-1][1:] == "html":
			temp.append(path+'/'+item)
		elif os.path.isdir(path+'/'+item) == True:
			if item=='resources':
				pass
			else:
				temp.extend(get_all_file(path+'/'+item))
	return temp


def main():
	'''
	'''
	if not os.path.exists(WORK_PATH):
		os.makedirs(WORK_PATH)

	files=get_all_file(WORK_PATH)
	
	for file in files:
		print("Building "+file)
		with open(file,'r+') as f:
			temp = f.read()
			temp.replace(".md'>",".html'>")
			f.seek(0)
			f.truncate()
			f.write(temp.replace(".md'>",".html'>"))

if __name__ == '__main__':
	main()