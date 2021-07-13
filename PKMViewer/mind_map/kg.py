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

def change_to_pair(data,kind="Echart"):
	# kind = "Xmind", "Echart"
	# 测试功能
	##连接neo4j数据库，输入地址、用户名、密码
	graph = Graph(
		"http://localhost:7474", 
		username="neo4j", 
		password="123"
	)
	# 保存为结点-联系-结点的结构
	print(data)
	main_node = Node("Stucture",name = data["name"])
	graph.create(main_node)
	if "children" in data:
		for item in data["children"]:
			print(item)
			item_node = change_to_pair(item)
			item_rela = Relationship(main_node,'Branch',item_node)
			graph.create(item_rela)
	return main_node


