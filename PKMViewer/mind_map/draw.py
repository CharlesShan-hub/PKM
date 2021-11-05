from pyecharts import options as opts
from pyecharts.charts import Tree


def make_height_auto_content(html):
	""" In JS:
		chart_f0487771e16b49a4b7f46e2302533471.on("click", chart_click);	
		function chart_click(){
			alert(111);
			auto_change_height();
		}
		function auto_change_height(){
			var container = document.getElementById("f0487771e16b49a4b7f46e2302533471");
		    var allNode=0;
		    var nodes=chart_f0487771e16b49a4b7f46e2302533471._chartsViews[0]._data._graphicEls;
		    for(var i=0,count =nodes.length;i<count;i++){
		       var node=nodes[i];
		       if(node===undefined)
		           continue;
		       allNode++;
		    }
		    var height=window.innerHeight;
		    var currentHeight=45*allNode;
		    var newWidth=Math.max(currentHeight,height);
		    container.style.width = window.innerWidth + 'px';
		    container.style.height = newWidth + 'px';
		    chart_f0487771e16b49a4b7f46e2302533471.resize();
		}
	"""
	"""
	param.name：X轴的值
	param.data：Y轴的值
	param.value：Y轴的值
	param.type：点击事件均为click
	param.seriesName：legend的名称
	param.seriesIndex：系列序号（series中当前图形是第几个图形第几个）
	param.dataIndex：数值序列（X轴上当前点是第几个点）

	alert(param.data.name)节点名称，经过测试，param.data.xxx就是每个节点的某种属性！！
	"""
	content1 = """.on("click", chart_click);
	function chart_click(param){
		//alert(param.data.name);
		auto_change_height();
	}
	function auto_change_height(param){
		var container = document.getElementById(\'"""
	content2 = """');
	    var allNode=0;
	    var nodes="""
	content3 = """._chartsViews[0]._data._graphicEls;
	    for(var i=0,count =nodes.length;i<count;i++){
	       var node=nodes[i];
	       if(node===undefined)
	           continue;
	       allNode++;
	    }
	    var height=window.innerHeight;
	    var currentHeight=40*allNode;
	    var newWidth=Math.max(currentHeight,height);
	    container.style.width = window.innerWidth + 'px';
	    container.style.height = newWidth + 'px';
	"""
	content4 = """.resize();
	}

	function load(){
		auto_change_height(0)
	}
	"""

	sub_start = html.find("<body>")
	sub_end = html.rfind("</body>")

	sub_div_start = html.find("<div",sub_start,sub_end)
	sub_div_end = html.rfind("</div>",sub_start,sub_end)
	content_div = html[sub_div_start:sub_div_end].split('"')[1]

	sub_script_start = html.find("<script>",sub_start,sub_end)
	sub_script_end = html.rfind("</script>",sub_start,sub_end)
	sub_var = html.find("var",sub_script_start,sub_script_end)
	content_eha = html[sub_var:sub_var+50].split(" ",3)[1]

	return content_eha+content1+content_div+content2+content_eha+content3+content_eha+content4


def make_hover(html):
	""" 鼠标悬停显示备注
	"""
	newcontent = """
	"formatter": function(params){
	    var content = params.data.value;
		if(typeof(content) == "undefined" || content == null)
			return "";
	    function creatArr(str,LEN){
	        var arr = [];//用于保存每次截取后的字符串
	        var index = 0;
	        var flag;
	        while(str.length > LEN){
	            flag=str.substr(0, LEN).indexOf("\\n");
	            if(flag != -1){
	            	newStr = str.substr(0, flag);
	                arr.push(newStr);
	                str = str.substr(flag+1);
	            }else{
	            	newStr = str.substr(0, LEN);
	                arr.push(newStr);
	                str = str.substr(LEN);
	                if(str.length>0){
	                	if(str.substr(0,1)==\'\\n\'){
	                		str = str.substr(1);
	                	}
	                }
	            }
	        }
	        if(str.length > 0){
	            arr.push(str);
	        }
	        return arr.join("<br>");
	    }
	    content = creatArr(content,35);
	    return content.split("\\n").join("<br>");
	},
	"""
	sub = html.find("\"animation\"")
	return html[:sub]+newcontent+html[sub:]

def make_open_file(html):
	""" 双击打开文件---没成功
	"""
	sub_start = html.find("<body>")
	sub_end = html.rfind("</body>")

	sub_div_start = html.find("<div",sub_start,sub_end)
	sub_div_end = html.rfind("</div>",sub_start,sub_end)
	#content_div = html[sub_div_start:sub_div_end].split('"')[1]

	#sub_script_start = html.find("<script>",sub_start,sub_end)
	#sub_script_end = html.rfind("</script>",sub_start,sub_end)
	#sub_var = html.find("var",sub_script_start,sub_script_end)
	#content_eha = html[sub_var:sub_var+50].split(" ",3)[1]

	return html



def html_add_script(html,content):
    # 测试版, 传入带有script表标签的内容
    sub_start = html.find("<body>")
    sub_end = html.rfind("</body>")
    sub = html.rfind("</script>",sub_start,sub_end)
    return html[:sub-1]+content+html[sub:]

def html_add_param(html,content):
	# 测试版, 将<body>中加入参数
	sub = html.find("<body")
	return html[:sub+5]+content+html[sub+5:]

def draw_html(data, temp=False,name="render.html",\
	symbol_size=13,auto_change_height=True,change_hover=True,\
	open_file=True):
	if type(data)!=list:
		data = [data]
	c = (
	    Tree(init_opts=generat_init_opt())
	    .add(
	    	"", 
	    	data,
	    	symbol_size=symbol_size)#, label_opts=generat_opt()
	    #.set_global_opts(
        #	tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove")
    	#)
	)
	if temp==False:
		c.render(name)

	with open(name,"r") as f:
		html=f.read()

	if auto_change_height==True:
		content = make_height_auto_content(html)
		html = html_add_script(html,content)
		content = """ onload="load()" """
		html = html_add_param(html,content)
	
	if change_hover==True:
		html = make_hover(html)

	if open_file==True:
		html = make_open_file(html)

	with open(name, "w") as f:
		f.write(html)
	


def generat_init_opt():
	return opts.InitOpts(width="1080px", height="100vh")

def generat_opt():
	# 目前为测试版, 没有传入参数
	label_opts=opts.LabelOpts(
		position="top",
		horizontal_align="right",
		vertical_align="middle",
	),
	return label_opts
