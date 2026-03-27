# Promise 编程风格

`Promise`的学习可以参考官方文档：[**MDN Web Docs**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)

---

## 什么是 Promise

****Promise 的本质：一种更优雅的异步编程风格。【ES6（ECMAScript 2015）引入的，浏览器内置了 Promise 对象】****

Promise 就像一个"承诺"，表示一个将来会完成（或失败）的操作。它有三种状态：

+ **Pending**：待定
+ **Fulfilled**：兑现
+ **Rejected**：拒绝

---

## 为什么需要 Promise

使用 Promise 可以对"回调地狱"（多层嵌套的回调函数）代码进行封装，对外提供一种优雅的编码风格。（变相解决回调地狱问题）

**回调地狱(******Callback Hell******)**就像是你让一群人帮你做事，但每个人都要等前一个人做完才能开始，结果形成了一连串的"等TA做完后，你再..."的嵌套关系。

**举个生活例子：**

想象你要做一顿饭，步骤是：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1750229406279-59a2f8e6-10a0-4fdc-a74a-d3cac4800902.png)

用回调函数写出来就是这样：

```javascript
买菜(function(买的菜) {
  洗菜(买的菜, function(洗好的菜) {
    切菜(洗好的菜, function(切好的菜) {
      炒菜(切好的菜, function(做好的菜) {
        吃(做好的菜);
      });
    });
  });
});
```

**为什么叫"地狱"？**

1. **代码向右延伸**：每层回调都向右缩进，最终代码会变得非常宽
2. **难以阅读**：大括号和小括号层层嵌套，眼睛都要看花
3. **难以维护**：想调整顺序或添加步骤都很困难
4. **错误处理复杂**：每个回调都要单独处理错误

**对比 Promise 的写法：**

```javascript
买菜()
  .then(洗菜)
  .then(切菜)
  .then(炒菜)
  .then(吃)
  .catch(处理错误);
```

这样代码就像一条直线往下走，清晰多了吧？这就是为什么 Promise 能解决回调地狱问题。

****对于我们之前编写的 XHR 发送 AJAX 请求，大家可以试想一下，如果继续使用这种编码风格，在请求 1 成功响应后继续发送请求 2，在请求 2 成功响应后继续发送请求 3，会不会出现回掉地狱问题！！！！****

---

## Promise 基本代码

```javascript
// 创建并立即返回一个Promise
// new Promise()是调用构造函数
// 构造函数中的参数我们称为：执行器函数
// 构造函数执行时，执行器函数会被立即调用
// 并且执行器函数在调用前，JavaScript引擎为执行器函数提前准备好了两个函数：resolve，reject
// resolve函数会自动传给执行器函数的第一个参数x
// reject函数会自动传给执行器函数的第二个参数y
const myPromise = new Promise((x, y) => {
  const success = true / false;
  if(success){
    // x 指向的是 resolve 函数
    // resolve 函数执行之后的作用是：将Promise对象的状态从“待定”变为“兑现”，并且存储成功的值。
    x("操作成功！");
  }else{
    // y指向的是 reject 函数
    // reject 函数执行之后的作用是：将Promise对象的状态从“待定”变为“拒绝”，并且存储失败的值。
    y(new Error("操作失败！"));
  }
});

// .then() 方法用于处理 Promise 兑现（成功）的情况，then方法的参数是一个回调函数，回调函数会自动接收到当时存储的成功的值。
// .catch() 方法用于处理 Promise 拒绝（失败）的情况，catch方法的参数也是一个回调函数，回调函数会自动接收到当时存储的失败的值。
// 注意：then方法和catch方法中的回调函数执行时机是：会等待执行器中的ajax请求结束之后才会执行。
myPromise
        .then(result => console.log(result))
        .catch(err => console.error(err));
```

---

## 将 XHR 代码封装为 Promise 风格

### 首次封装

将之前实现的用户名是否可用的 AJAX GET 请求封装为 Promise 风格，代码如下：

```javascript
new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `check?username=${encodeURIComponent(username)}&_=${Date.now()}`, true);
    xhr.onload = function(){
        if(xhr.status >= 200 && xhr.status < 300){
            try{
                const result = JSON.parse(xhr.responseText);
                if(result.success){
                    resolve('恭喜你，您的用户名可用');
                }else{
                    reject("您的名字太受欢迎，需要重新填写");
                }
            }catch(e){
                reject("解析响应时出错，请重试");
            }
        }else{
            reject("请求失败，请稍后重试");
        }
    }
    xhr.onerror = function(){
        reject("网络错误，请检查您的连接");
    }
    xhr.send();
})
.then(msg => {
    showFeedback('success', msg)
})
.catch(error => {
    showFeedback('error', error);
})
```

### 升级改进

基于以上代码再次封装，封装属于自己的 Fetch API：定义 fetch 函数发送 AJAX GET 请求：

```javascript
// 自己封装的 fetch 函数（模仿的 Fetch API）
function fetch(url){
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', `${url}&_=${Date.now()}`, true);
        xhr.onload = function(){
            if(xhr.status >= 200 && xhr.status < 300){
                let response;
                try{
                    response = JSON.parse(xhr.responseText);
                    resolve(response);
                }catch(e){
                    reject("解析响应时出错，请重试");
                }
            }else{
                reject("请求失败，请稍后重试");
            }
        }
        xhr.onerror = function(){
            reject("网络错误，请检查您的连接");
        }
        xhr.send();
    })
}
```

调用自定义的 fetch 函数发送 AJAX GET 请求：

```java
// 调用自定义的fetch函数发送ajax get请求
fetch(`check?username=${encodeURIComponent(username)}`)
    .then((response) => {
        if(response.success){
            showFeedback('success', '恭喜你，您的用户名可用')
        }else{
            showFeedback('error', '您的名字太受欢迎，需要重新填写')
        }
    })
    .catch(error => {
        showFeedback('error', error)
    })
```

---

## 用户名可用时执行保存操作

由于用户名可用时才能执行保存操作，因此这两个 AJAX 请求不能异步，必须同步，只能等待校验用户名可用的 AJAX 请求结束之后，才能发送保存的 AJAX 请求。要达到这个效果，目前可以使用的就是****嵌套****，代码如下：

```javascript
// 调用自定义的fetch函数发送ajax get请求
fetch(`check?username=${encodeURIComponent(username)}`)
    .then((response) => {
        if(response.success){
            // 用户名可用时发送ajax请求执行保存操作（嵌套的）
            fetch(`save?username=${encodeURIComponent(username)}`)
                .then((response) => {
                    if(response.success){
                        showFeedback('success', '用户名可用，并且已保存成功')
                    }else{
                        showFeedback('error', '用户名可用，但保存失败');
                    }
                })
                .catch(error => {
                    showFeedback('error', error);
                })
        }else{
            showFeedback('error', '您的名字太受欢迎，需要重新填写')
        }
    })
    .catch(error => {
        showFeedback('error', error)
    })
```

后端 Servlet 程序代码如下：

```java
package com.jkweilai.ajax.servlet;

import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

@WebServlet("/save")
public class UserSaveServlet extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String username = request.getParameter("username");
        Connection conn = null;
        PreparedStatement ps = null;
        int count = 0;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/ajax", "root", "123456");
            String sql = "insert into t_user(username) values(?)";
            ps = conn.prepareStatement(sql);
            ps.setString(1, username);
            count = ps.executeUpdate();
        } catch (Exception e) {
            throw new RuntimeException(e);
        } finally {
            if (ps != null) {
                try {
                    ps.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
            if (conn != null) {
                try {
                    conn.close();
                } catch (SQLException e) {
                    throw new RuntimeException(e);
                }
            }
        }
        response.setContentType("application/json;charset=UTF-8");
        PrintWriter out = response.getWriter();
        out.print("{\"success\" : " + (count == 1) + "}");
    }
}
```

功能虽然实现了，但第二个 AJAX 请求必须等待第一个 AJAX 请求结束之后才能进行，为了达到这个效果，我们只能使用嵌套，提到嵌套，显然又发生了 **Callback Hell 回调地狱**问题。

解决这个问题，可以使用 ES8 新语法：async/await。

---

## ES8 语法 async/await

async 和 await 是 JavaScript 的语法，属于 ECMAScript ****2017**** (ES8) 标准引入的 异步编程语法糖，本质上是基于 Promise 的，可以让异步代码的写法更接近同步代码，提高可读性和可维护性。

### `async` 的作用

**功能：**

+ 用于声明一个 **异步函数**（`async function`）。
+ **返回值**：`async` 函数 **总是返回一个 **`Promise`：
    - 如果函数内返回普通值（如 `return 42`），它会被自动包装成 `Promise.resolve(42)`。
    - 如果函数内抛出错误（如 `throw new Error(...)`），它会被包装成 `Promise.reject(error)`。

**示例：以下两种写法是******等效******的。**

```javascript
let num = 100;

// 第一种写法
let promise = new Promise((resolve, reject) => {
    if(num < 0){
        // 将Promise对象状态从待定变成拒绝，并将错误值保存。
        reject(new Error("数字不能小于0"));
    }else{
        // 将Promise对象状态从待定变成兑现，并将成功的值保存。
        resolve(num);
    }
})

promise.then(result => {
    console.log(result)
});

// 第二种写法
async function fetchData(){
    if(num < 0){
        // 如果函数执行过程中出现了异常，异常将被当做失败的值保存起来。
        throw new Error("数字不能小于0");
    }
    // 返回值被当做成功的值保存起来。
    return num;
}

fetchData().then(result => {
    console.log(result)
});
```

### `await` 的作用

**功能：**

+ `**await**`** 只能在 **`**async**`** 函数内部使用。**
+ `**await**`**出现会****暂停 **`**async**`** 函数的执行**
+ `**await**`**关键字后面通常是一个 **`**Promise**`
+ `**await**`**会等 **`**Promise**`**的完成，只有 **`**await**`**后面的 **`**Promise**`**完成后，**`**async**`**函数才能继续往下执行。**
+ `**await**`**后面的 **`**Promise**`**执行成功后，**`**await**`**会返回成功的值。**
+ `**await**`**后面的 **`**Promise**`**执行抛出错误时，**`**await**`**会抛出错误，可以使用 try/catch 捕获。**

**使用 async/await 改造上面的代码，解决回调地狱问题：**

```javascript
async function checkAndSaveUser(username){
    try{
        let response = await fetch(`check?username=${encodeURIComponent(username)}`)
        if(response.success){
            response = await fetch(`save?username=${encodeURIComponent(username)}`)
            if(response.success){
                showFeedback('success', '用户名可用，并且已保存成功')
            }else{
                showFeedback('error', '用户名可用，但保存失败');
            }
        }else{
            showFeedback('error', '您的名字太受欢迎，需要重新填写')
        }
    }catch(e){
        showFeedback('error', e)
    }
}

checkAndSaveUser(username);
```

### `async/await` 对比 `Promise.then()`

**传统 **`Promise`** 写法（回调风格）**

```javascript
fetch(`check?username=${encodeURIComponent(username)}`)
    .then((response) => {
        if(response.success){
            // 用户名可用时发送ajax请求执行保存操作
            fetch(`save?username=${encodeURIComponent(username)}`)
                .then((response) => {
                    if(response.success){
                        showFeedback('success', '用户名可用，并且已保存成功')
                    }else{
                        showFeedback('error', '用户名可用，但保存失败');
                    }
                })
                .catch(error => {
                    showFeedback('error', error);
                })
        }else{
            showFeedback('error', '您的名字太受欢迎，需要重新填写')
        }
    })
    .catch(error => {
        showFeedback('error', error)
    })
```

**问题：**  

+ 嵌套的 `.then()` 可能导致 **回调地狱**（Callback Hell）。
+ 错误处理依赖 `.catch()`，不够直观。

`async/await`** 写法（更清晰）**

```javascript
async function checkAndSaveUser(username){
    try{
        let response = await fetch(`check?username=${encodeURIComponent(username)}`)
        if(response.success){
            response = await fetch(`save?username=${encodeURIComponent(username)}`)
            if(response.success){
                showFeedback('success', '用户名可用，并且已保存成功')
            }else{
                showFeedback('error', '用户名可用，但保存失败');
            }
        }else{
            showFeedback('error', '您的名字太受欢迎，需要重新填写')
        }
    }catch(e){
        showFeedback('error', e)
    }
}

checkAndSaveUser(username);
```

**优点：**  

+ **代码更扁平**，没有嵌套的回调。
+ **错误处理更直观**（`try/catch` 像同步代码一样）。
+ **调试更方便**（可以在 `await` 处设置断点）。

### 总结

+ `async`：让函数返回 `Promise`，使其支持 `await`。
+ `await`：让 `async` 函数 **等待 **`Promise`** 完成**，避免回调嵌套。
+ `try/catch`：替代 `.catch()`，更直观地处理错误。

`async/await`** 是 JavaScript 异步编程的终极解决方案**，让代码更清晰、更易维护！

到此为止，Promise 编程风格就说完了。
