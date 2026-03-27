# Axios 实现 AJAX

第三方库，底层基于 Promise+XHR 封装，并不是对 Fetch API 的封装，比 Fetch API 好用。使用它需要引入 `axios.js`库文件。使用国内 CDN 加速引入：

```html
<script src="https://cdn.bootcdn.net/ajax/libs/axios/1.6.7/axios.min.js"></script>
```

---

## 发送 GET 请求

```javascript
axios.get('check', {
  // 这个参数将被自动追加到url后面，格式为 url?name=value
  params: {username : username},
  // 发送请求时这个将被自动放到请求头中
  headers: {a:"b"}
}).then(response => {
  if(response.data.success) {
    showFeedback('success', '恭喜你，您的用户名可以使用')
  }else{
    showFeedback('error', '非常遗憾，您的用户名太受欢迎，请重新选一个')
  }
}).catch(error => {
  showFeedback('error', `${error.code}: ${error.message}`);
})
```

提示：

1. `params`用于将数据拼接到 URL 后面，主要应用于 get 请求，post 请求不采用这种方式提交数据。
2. `headers`用户设置请求头。

**关于 axios 库的 then() 中回调函数的 response 参数：**

**当请求成功（HTTP 状态码为 2xx）时，**`****response****`**包含以下属性：**

| ****属性**** | ****说明**** |
| --- | --- |
| `****data****` | **服务器返回的响应体（自动解析为 JSON 对象或字符串）。** |
| `****status****` | **HTTP 状态码（如**`****200****`**）。** |
| `****statusText****` | **HTTP 状态描述（如**`****"OK"****`**）。** |
| `****headers****` | **响应头（是一个对象，如**`****{ 'content-type': 'application/json' }****`**）。** |
| `****config****` | **本次请求的 Axios 配置（包括 URL、方法、参数等）。** |
| `****request****` | **浏览器中的**`****XMLHttpRequest****`**实例** |

**关于 axios 库的 catch() 中回调函数的 error 参数：**

**当请求失败（网络错误、超时或状态码非 2xx）时，**`****error****`**是**`****AxiosError****`**类型的对象，包含以下关键属性：**

| ****属性**** | ****说明**** |
| --- | --- |
| `****response****` | **如果服务器有响应（如 404、500），此属性会包含完整的**`****response****`**对象。** |
| `****request****` | **浏览器中为**`****XMLHttpRequest****`**实例** |
| `****config****` | **本次请求的 Axios 配置。** |
| `****message****` | **错误描述（如网络错误时的**`****"Network Error"****`**）。** |
| `****code****` | **错误代码（如**`****"ECONNABORTED"****`**表示超时）。** |

---

## 发送 POST 请求

### 以表单方式提交数据

```javascript
axios.post('check', `username=${username}`, {
  headers: {
    // 对于axios来说，这不是必须的，可以省略。它可以根据第二个参数是name=value对儿来自动决定采用表单方式提交数据。
    'content-type': 'application/x-www-form-urlencoded'
  }
}).then(response => {
  if(response.data.success) {
    showFeedback('success', '恭喜你，您的用户名可以使用')
  }else{
    showFeedback('error', '非常遗憾，您的用户名太受欢迎，请重新选一个')
  }
}).catch(error => {
  showFeedback('error', `${error.code}: ${error.message}`);
})
```

或者更加优雅的方式：

```javascript
const params = new URLSearchParams();
params.append('username', username);

axios.post('check', params, {
  headers: {
    // 可以省略。
    'content-type': 'application/x-www-form-urlencoded'
  }
}).then(response => {
  if(response.data.success) {
    showFeedback('success', '恭喜你，您的用户名可以使用')
  }else{
    showFeedback('error', '非常遗憾，您的用户名太受欢迎，请重新选一个')
  }
}).catch(error => {
  showFeedback('error', `${error.code}: ${error.message}`);
})
```

### 以 json 方式提交数据

如果后端接受 JSON 数据

```javascript
axios.post('check', {username: username}, {
  headers: {
    // 对于axios来说，这不是必须的，可以省略。它可以自动通过第二个参数是JS对象，会自动按照JSON格式提交数据。
    'content-type': 'application/json'
  }
}).then(response => {
  if(response.data.success) {
    showFeedback('success', '恭喜你，您的用户名可以使用')
  }else{
    showFeedback('error', '非常遗憾，您的用户名太受欢迎，请重新选一个')
  }
}).catch(error => {
  showFeedback('error', `${error.code}: ${error.message}`);
})
```

### 提交图片数据

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>文件上传</title>
    <script src="https://cdn.bootcdn.net/ajax/libs/axios/1.6.7/axios.min.js"></script>
</head>
<body>
    <input type="file" id="file-upload">
    <button id="upload-btn">上传</button>
    <div id="feedback"></div>

    <script>
        document.getElementById('upload-btn').addEventListener('click', function() {
            const file = document.getElementById('file-upload').files[0];
            if (!file) return;

            const formData = new FormData();
            formData.append('file', file);

            axios.post('/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then(function(response) {
                document.getElementById('feedback').textContent = '上传成功';
            })
            .catch(function(error) {
                document.getElementById('feedback').textContent = '上传失败';
            });
        });
    </script>
</body>
</html>
```

目前后端的 Servlet 没有编写，因此以上代码会出现 404 的错误!

---

## Axios+async/await

终极建议方案：

```javascript
async function checkUsername(username){
  const params = new URLSearchParams();
  params.append('username', username);
  try{
    const response = await axios.post('check', params);
    if(response.data.success){
      showFeedback('success', '恭喜你，您的用户名可以使用')
    }else{
      showFeedback('error', '非常遗憾，您的用户名太受欢迎，请重新选一个')
    }
  }catch(error){
    showFeedback('error', `${error.code}: ${error.message}`);
  }
}

checkUsername(username);
```
