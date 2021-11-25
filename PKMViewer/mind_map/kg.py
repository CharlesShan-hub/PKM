from py2neo import Graph,Node,Relationship

'''
class Node():
	"""docstring for Node"""
	def __init__(self,name,kind="Structure"):
		# kind: "Structure", "Detail", "Subject"
		self.kind = kind
		self.name = name

class Link():
	"""docstring for Link"""
	def __init__(self,name,kind="Branch"):
		# kind: "Branch", "Relete", "Summary"
		self.kind = kind
		self.name = name
'''

inher_type = 'Undefined'
omit_child = False

##连接neo4j数据库，输入地址、用户名、密码
graph = Graph(
	"http://localhost:7474", 
	username="neo4j", 
	password="123"
)

def creat_node(data):
	# 初始化
	global inher_type
	global omit_child
	node_type = inher_type
	# 标签
	tags = {}
	tags['name'] = data["name"]
	# 标签 - 解析数据
	if 'labels' in data:
		for item in data["labels"]:
			if item[0]=='$':
				# 定义结点标签
				tags[item[1:item.find(":")]]=str(item[item.find(":")+1:])
			elif item[0]=='@':
				# 定义结点类型
				node_type = item[1:]
			elif item[0:2]=='#0':
				# 开启子结点结构(本结点省略)
				inher_type=data["name"]
				return None
			elif item[0:2]=='#1':
				# 开启子结点结构(本结点不省略)
				inher_type=data["name"]
			elif item[0:2]=='#2':
				# 备注结点(完全忽略) --- 没实现
				return None
			elif item[0:2]=='#3':
				# 忽略本结点与后继结点 --- 没实现
				pass
			elif item[0:2]=='#4':
				# 忽略本结点的后继结点
				omit_child = True
	# 构造节点
	node = Node(node_type)
	node.update(tags)
	print(tags['name'])
	return node


def change_to_pair(data,father=None,kind="Echart",depth=0):
	'''
	'''
	# 初始化变量
	global graph
	global omit_child
	# 创建结点
	node = creat_node(data)
	if node!=None:
		graph.create(node)
	elif father==None:
		return False
	else:
		node=father

	# 插入子节点
	if "children" in data and omit_child==False:
		for item in data["children"]:
			child = change_to_pair(item,node)
			if node==child:
				continue
			relation = Relationship(node,'Branch',child)
			graph.create(relation)

	# 恢复现场
	omit_child = False
	# 返回构造好的本级内容
	return node

	'''
	# kind = "Xmind", "Echart"
	# 测试功能
	# 初始化变量
	global graph
	global inher_type
	global last_main_node
	# 保存为结点-联系-结点的结构
	#print("【",data,"】")
	tags = {}
	node_type = inher_type
	# 获取结点名称
	tags['name'] = data["name"]
	# 获取结点标签
	if 'labels' in data:
		for item in data["labels"]:
			if item[0]=='$':
				# 定义结点标签
				tags[item[1:item.find(":")]]=str(item[item.find(":")+1:])
			elif item[0]=='@':
				# 定义结点类型
				node_type = item[1:]
			elif item[0:2]=='#0':
				# 定义遗传结点类型(本结点跳过,直接插入子节点)
				inher_type = data["name"]
				depth = 1

	tags_str = ''
	for item in tags:
		tags_str=tags_str+","+item+"='"+str(tags[item])+"'"
	# 获取结点类型
	if depth==0:
		main_node = Node(node_type)
		last_main_node = main_node
		main_node.update(tags)
		graph.create(main_node)
		print(tags['name'])
	else:
		main_node = last_main_node
		depth = depth+1

	if "children" in data:
		for item in data["children"]:
			item_node = change_to_pair(item)
			if main_node==item_node:
				continue
			item_rela = Relationship(main_node,'Branch',item_node)
			graph.create(item_rela)
		last_main_node = None
	return main_node
	'''

# 命令保存
# 清空数据
# match (n) detach delete n
