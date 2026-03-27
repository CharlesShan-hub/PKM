# pushState()+AJAX 实现无刷新路由

---

## 什么是路由

路由（Routing） 的本质是 根据 URL 的变化，匹配对应的内容或逻辑。可以简单理解为：“网址（URL） ➔ 该显示什么（内容/功能）” 的映射规则。

---

## 单纯只用 AJAX 存在的问题

问题 1：AJAX 局部刷新后，URL 不会变化

现象：用户通过 AJAX 加载了新内容（比如从“首页”切换到“个人中心”），但浏览器的 URL 仍然是旧的（例如 [https://example.com](https://example.com)），地址栏不会更新。

后果：用户无法直接复制当前页面的链接分享给他人（因为 URL 未变，分享出去的链接永远是首页）。用户点击浏览器后退按钮会直接退出网站，而不是返回上一个 AJAX 加载的状态。

问题 2：浏览器历史记录无法管理

现象：每次 AJAX 加载内容后，浏览器历史记录中不会新增记录。

后果：用户无法通过前进/后退按钮导航到之前浏览的 AJAX 内容。用户体验断裂，违背用户对浏览器行为的预期（比如点击后退按钮期望回到上一屏内容，但实际却跳出了网站）。

---

## BOM 编程中的 history.pushState()

BOM 编程中的 history.pushState()方法可以模拟历史记录，并且修改浏览器地址栏上的 URL，并且保证不会刷新**整个**页面。

例如以下代码：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>

<button id="home">Home</button>
<button id="about">About</button>
<button id="concat">Contact</button>
<button id="replace">Replace</button>

<script>
    document.addEventListener("DOMContentLoaded", function (){

        // history.pushState({name: value}, "", url)
        // 作用：压栈
        document.getElementById("home").addEventListener("click", function (){
            // 第一个参数是对象，对象的属性名和属性值业务需要怎么定义就怎么定义。未来可以通过popstate事件的回调函数的event参数的state属性来获取该对象。
            // 第二个参数通常是网页标题，但大部分浏览器不支持，一般给一个空字符串。
            // 第三个参数是在浏览器地址栏上变化的url。
            history.pushState({myState: "主页"}, "", "/home"); // 压栈
        });
        document.getElementById("about").addEventListener("click", function (){
            history.pushState({myState: "关于"}, "", "/about"); // 压栈
        });
        document.getElementById("concat").addEventListener("click", function (){
            history.pushState({myState: "联系我们"}, "", "/concat"); // 压栈
        });

        // history.replaceState({name: value}, "", url);
        // 作用：将当前位置的历史记录替换成新的历史记录。
        document.getElementById("replace").addEventListener("click", function (){
            history.replaceState({myState: "我是最新的历史记录"}, "", "/newHistory");
        });

        // 给当前浏览器窗口添加 popstate 事件监听
        // 当用户点击浏览器的前进和后退按钮时 popstate 事件被触发
        // 回调函数的event参数有state属性，通过state属性可以取出压栈时的对象。
        window.addEventListener("popstate", function (event){
            console.log(event.state.myState)
        });
    });
</script>

</body>
</html>

```

其中涉及到三部分重点内容：

1. history.pushState(state, '页面标题', url)
    1. 第一个参数 state 是一个状态对象 `{}`，该对象的属性和数据自行组织，业务需要怎么组织就怎么组织。该状态对象 state 可以在 popstate 事件发生时的回调函数的 event 参数的 state 属性来获取。
    2. 第二个参数是页面标题，这个页面表达大部分浏览器是不支持的，你还是需要通过 `document.title`来修改页面的标题，因此这个参数一般给一个空字符串。
    3. 第三个参数是 url，这个 url 将会被修改到地址栏上。
    4. 这个方法相当于是一个压栈的动作，将最近一次的历史记录放到栈顶部。后退的时候它将会被第一个弹出（取出但栈元素并不会删除）。这样就可以模拟出历史记录的效果了。
2. history.replaceState(state, '页面标题', url)
    1. 将当前的历史记录替换成新的历史记录。
3. window 对象的 popstate 事件
    1. 当用户点击浏览器上的前进和后退按钮时，注册的 popstate 事件会发生。该事件发生时的回调函数 event 参数的 state 属性就可以获取到 pushState 方法的第一个参数。

---

## 实现无刷新路由

### 前端代码

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>pushState + AJAX</title>
    <script src="https://cdn.bootcdn.net/ajax/libs/axios/1.6.7/axios.min.js"></script>
</head>
<body>

<button id="home">Home</button>
<button id="about">About</button>
<button id="concat">Contact</button>

<div id="content"></div>

<script>
    document.addEventListener("DOMContentLoaded", function (){

        // 初始化加载页面
        loadPage("/ajax/home");

        document.getElementById("home").addEventListener("click", function (){
            let url = "/ajax/home";
            history.pushState({}, "", url);
            loadPage(url);
        });
        document.getElementById("about").addEventListener("click", function (){
            let url = "/ajax/about";
            history.pushState({}, "", url);
            loadPage(url);
        });
        document.getElementById("concat").addEventListener("click", function (){
            let url = "/ajax/contact";
            history.pushState({}, "", url);
            loadPage(url);
        });

        window.addEventListener("popstate", function (event){
            // 假设路径是：http://localhost:8080/ajax/contact
            // document.location.pathname：获取的是 /ajax/contact
            loadPage(document.location.pathname);
        });
    });

    async function loadPage(url){
        let response = await axios.get(url);
        document.getElementById("content").innerHTML = response.data;
    }
</script>

</body>
</html>

```

### 后端代码

```java
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;

@WebServlet(name = "PageServlet", urlPatterns = {"/home", "/about", "/contact"})
public class PageServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        response.setContentType("text/html");
        PrintWriter out = response.getWriter();

        String path = request.getServletPath();

        switch (path) {
            case "/home":
                out.println("<h1>Welcome to Home</h1><p>This is the home page.</p>");
                break;
            case "/about":
                out.println("<h1>About Us</h1><p>This is the about page.</p>");
                break;
            case "/contact":
                out.println("<h1>Contact</h1><p>Email: test@example.com</p>");
                break;
            default:
                out.println("<h1>404 Not Found</h1>");
        }
    }
}
```

注意：后面的 Vue 框架中已经将无刷新路由实现了，以上所讲是它的实现原理。
