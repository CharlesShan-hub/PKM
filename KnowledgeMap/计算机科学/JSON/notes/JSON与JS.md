# JSON与JS

2022.6.16

[toc]

### 字符串与对象转化

1. `eval`：目前很少使用，有安全风险

   eval使用方法：

   ```js
   var str = "console.log('hello')"
   eval(str)
   ```

   eval进行json解析：注意加括号

   ```js
   var str = '{"name":"Charles","age":22}'
   var obj = eval("(" + str + ")")
   console.log(obj)
   ```

2. `JSON.parse()`：推荐使用

   ```js
   var str = '{"name":"Charles","age":22}'
   var obj = JSON.prase(str)
   console.log(obj)
   ```

   JSON.parse进行默认处理

   ```js
   function fun(name, value){
     console.log(name + ":" + value)
     return value;
   }
   var str = '{"name":"Charles","age":22}'
   var obj = JSON.prase(str, fun)
   ```

3. `JSON.stringify(value[, replacer[, space]])`

   * value: 必须参数，被转换的js值
   * replacer: 可以省略，可以是函数或数组
     * 函数：每一组名称/值都会调用次函数，该函数返回一个值，作为名称的值变换到结果字符串中，如果返回undefined，该成员会被忽略
     * 数组：只有数组中存在的名称才会被转换，转换后顺序与数组中的值一致
   * space：可以省略，为了排版、方便阅读。可以在JSON字符串中添加空白或制表符

   ```js
   var obj = {
     "name": "Charles Shan",
     "age": 22,
     "a": undefined,
     "b": function(){},
     "c": [function(){}]
   }
   
   var jsonStr = JSON.stringify(obj)
   console.log(jsonStr)
   // Print: {"name":"Charles","age":22,"c":[null]}
   ```

   replacer用法（函数）

   ```js
   var obj = {
     "name": "Charles Shan",
     "age": -1
   }
   
   function fun(name,value){
     if(name=="age" && value<0)
       value = 0
     return value
   }
   var jsonStr = JSON.stringify(obj,fun)
   ```

   replace用法（数组）

   ```js
   var obj = {
     "a":1,
     "c":3,
     "b":2,
     "d":4
   }
   
   var jsonStr = JSON.stringify(obj,["a","b","c"])
   console.log(jsonStr)
   // Print: {"a":1,"b":2,"c":3}
   ```

   space用法

   ```js
   var obj = {
     "a":1,
     "c":3,
     "b":2,
     "d":4
   }
   
   var jsonStr = JSON.stringify(obj,["a","b","c"], "--")
   console.log(jsonStr)
   // Print: {--"a":1,--"b":2,--"c":3}
   // 常用方法，添加制表符
   var jsonStr = JSON.stringify(obj,["a","b","c"], "\t")
   console.log(jsonStr)
   //{
   //	"a":1,
   //	"b":2,
   //	"c":3
   //}
   ```

### Ajax与JSON

1. 网页端，创建对象

```js
function CreatXHR(){
  if(window.XMLHttpRequest){
    // IE7++, Chrome, Firefox
    return new XMLHttpRequest()
    
  }else{
    // IE6, IE5
    return new ActiveXObject("Microsoft.XMLHTTP")
  }
}

var xmlhttp = CreatXHR()
```

2. 网页端，请求并解析json文件

```js
xmlhttp.open("GET","test.json",true)//true代表异步请求
xmlhttp.send()
xmlhttp.onreadystatechange = function(){
  if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
    var jsonStr = xmlhttp.responseTest
    console.log(jsonStr)
    var obj = JSON.parse(jsonStr)
  }
}
```

readyState：

* 0:请求未初始化
* 1:服务器连接已建立
* 2:请求已接受
* 3:请求处理中
* 4:请求已完成，且相应已就绪

status：是响应码