import mind_map.IO as mind_IO
import json
import os

def print_json(data):
	print(json.dumps(data, indent=4, sort_keys=False, ensure_ascii=False))

def change_key(item): 
	# change title -> name
	item["name"] = item.pop("title")

	# change note -> value
	if "note" in item:
		item["value"] = item.pop("note")

	# change topics -> children
	if "topics" in item:
		#if type(item["topics"])==list:
		temp = []
		for child in item["topics"]:
			temp.append(change_key(child.copy()))
		item["children"] = temp
		item.pop("topics")

	# change topic -> children
	if "topic" in item:
		#if type(item["topic"])==dict:
		item["children"]=[change_key(item["topic"].copy())]
		item.pop("topic")
	return item

def draw_init(data):
	data.pop("structure")
	data = change_key(data)["children"][0]
	return data


# symbol marker identify node type
# Structure - 知识图的框架
SYMBOL_STUCTURE = "c_symbol_exercise"
# Subject - 知识图中可以代表各级学科
SYMBOL_SUBJECT = "symbol-pin"
# Detail - 代表细节
SYMBOL_DETAIL = "symbol-diamond"
# Link - 代表链接节点
SYMBOL_LINK = "symbol-share"

# base path - for xmind joining
BASE_PATH = ''

def symbol_init(SYMBOL_STUCTURE = "c_symbol_exercise",
	SYMBOL_SUBJECT = "symbol-pin",SYMBOL_DETAIL = "symbol-diamond",
	SYMBOL_LINK = "symbol-share"):
	SYMBOL_STUCTURE = SYMBOL_STUCTURE
	SYMBOL_SUBJECT = SYMBOL_SUBJECT
	SYMBOL_DETAIL = SYMBOL_DETAIL
	SYMBOL_LINK = SYMBOL_LINK

def data_filter(item,kind="Structure"):
	# get "Structure" node
	if kind=="Structure":
		flag = SYMBOL_STUCTURE
	temp = []

	#
	for child_item in item["children"]:
		if "makers" in child_item:
			if flag in child_item["makers"]:
				if "children" in child_item:
					temp.append(data_filter(child_item,kind).copy())
				else:
					temp.append(child_item)
	if temp == []:
		item.pop("children")
	else:
		item["children"]=temp.copy()
	return item

def load_dataset(path,auto_join=True):
	data = mind_IO.load_dataset(join_path(path))
	
	if "topic" in data:
		if"topics" in data["topic"]:
			temp = []
			for i in range(len(data["topic"]["topics"])):
				temp.append(add_child_file(data["topic"]["topics"][i]))
			data["topics"]=temp.copy()
	return data

	'''
	for i in range(len(data["children"])):
		add_child_file()
		if ("labels" in data["children"][i]) and ("makers" in data["children"][i]):
			if SYMBOL_LINK in data["children"][i]["makers"]:
				# Get file!
				data["children"][i]["children"] = load_dataset(data["children"][i]["labels"])["children"]
	'''
	#return data

def add_child_file(item):
	# Add new file
	if ("labels" in item) and ("makers" in item):
		if SYMBOL_LINK in item["makers"]:
			item["topics"] = mind_IO.load_dataset(join_path(item["labels"][0]))["topic"]["topics"]
	# Check child item new file
	if "topics" not in item:
		return item
	temp = []
	for i in range(len(item["topics"])):
		temp.append(add_child_file(item["topics"][i]))
	item["topics"]=temp.copy()
	
	return item

def set_base_path(path):
	global BASE_PATH
	BASE_PATH = path

def join_path(path):
    if path[0:2] == './':
        return os.path.join(BASE_PATH,path[2:])
    else:
    	return os.path.join(BASE_PATH,path)
