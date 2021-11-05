DEFAULT_PATH = "../test.html"

def load_html(path=DEFAULT_PATH):
	""" 加载网页文件 --成功
	"""
	with open(path,"r") as f:
		html=f.read()
	return html

CHART_ID = None

def init_chart_id(path=DEFAULT_PATH,html=None):
	""" 获取本次图表的ID --成功
	"""
	if html==None:
		html = load_html(path)
	sub_start = html.find("<body")
	sub_end = html.rfind("</body>")

	sub_div_start = html.find("<div",sub_start,sub_end)
	sub_div_end = html.rfind("</div>",sub_start,sub_end)
	content_div = html[sub_div_start:sub_div_end].split('"')[1]

	sub_script_start = html.find("<script>",sub_start,sub_end)
	sub_script_end = html.rfind("</script>",sub_start,sub_end)
	sub_var = html.find("var",sub_script_start,sub_script_end)
	global CHART_ID
	CHART_ID = html[sub_var:sub_var+50].split(" ",3)[1][6:]

def init_set_tags(path=DEFAULT_PATH):
	""" 初始化时写入一些标签 --成功
		根据需要继续开发
	"""
	#加载网页
	html = load_html(path)

	#设置body标签
	sub_start = html.find("<body")
	html = html[:sub_start+7]+"<!--BODY-TAG-->\n"+html[sub_start+7:]
	with open(path, "w") as f:
		f.write(html)

def init_onload(path=DEFAULT_PATH,html=None):
	""" 设置onload函数 --成功
	"""
	if html==None:
		html = load_html(path)
	sub = html.find("<body")
	html=html[:sub+5]+" onload=\"load()\" "+html[sub+5:]

	content = """
		function load(){
			//ONLOAD_TAG
		}
	"""
	sub = html.rfind("</script>")
	last_content = html[sub+10:]
	html = html[:sub+10]+"\n\t\t<script>"
	for line in content.split("\n"):
		html = html+"\n\t"+line
	html = html+"\n\t\t</script>\n" +last_content

	with open(path, "w") as f:
		f.write(html)


def insert_onload(path=DEFAULT_PATH,html=None,content=None):
	""" 向onlaod函数中加一个函数调用
	"""
	if html==None:
		html = load_html(path)

	sub = html.find("ONLOAD_TAG")
	last_content = html[sub-3:]
	html = html[:sub-3]
	for line in content.split("\n"):
		html = html+"\n\t\t\t\t"+line
	html = html+"\n\t\t\t"+last_content

	with open(path, "w") as f:
		f.write(html)


def insert_js(path=DEFAULT_PATH,html=None,content=None):
	""" 插入js代码（默认查到最后）--成功
	"""
	if html==None:
		html = load_html(path)

	sub = html.rfind("</script>")
	last_content = html[sub+10:]
	html = html[:sub+10]+"\n\t\t<script>"
	for line in content.split("\n"):
		html = html+"\n\t\t\t"+line
	html = html+"\n\t\t</script>\n" +last_content

	with open(path, "w") as f:
		f.write(html)

#set_tags()


# 测试获取chart_id
init_chart_id()
#print(CHART_ID)


# 测试生成onload函数
#init_onload()


# 测试向onload中加入元素
insert_onload(content="alert(1);")
# 测试插入js
#content1 = """
#int a = 1;
#alert(a);
#"""
#insert_js(content = content1)


# 测试打印文档
#print(load_html())