# 作业

---

## 实现省市联动效果

页面给大家：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>省市联动选择器</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            width: 100%;
            max-width: 500px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            padding: 30px;
            animation: fadeIn 0.5s ease-out;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        h1 {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 30px;
            font-weight: 500;
        }
        
        .form-group {
            margin-bottom: 25px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
            color: #2c3e50;
        }
        
        select {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 16px;
            background-color: #fff;
            transition: border 0.3s;
            appearance: none;
            background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
            background-repeat: no-repeat;
            background-position: right 10px center;
            background-size: 1em;
        }
        
        select:focus {
            outline: none;
            border-color: #3498db;
            box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.2);
        }
        
        select:disabled {
            background-color: #f9f9f9;
            color: #999;
        }
        
        .result {
            margin-top: 25px;
            padding: 15px;
            background-color: #e8f4fd;
            border-radius: 6px;
            color: #2980b9;
            text-align: center;
            display: none;
        }
        
        .loading {
            display: none;
            text-align: center;
            margin: 10px 0;
            color: #7f8c8d;
        }
        
        .loading:after {
            content: "...";
            animation: dots 1.5s steps(5, end) infinite;
        }
        
        @keyframes dots {
            0%, 20% { content: "."; }
            40% { content: ".."; }
            60%, 100% { content: "..."; }
        }
        
        .footer {
            margin-top: 30px;
            text-align: center;
            font-size: 14px;
            color: #95a5a6;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>省市联动选择器</h1>
        
        <div class="form-group">
            <label for="province">选择省份</label>
            <select id="province">
                <option value="">请选择省份</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="city">选择城市</label>
            <select id="city" disabled>
                <option value="">请先选择省份</option>
            </select>
        </div>
        
        <div class="loading" id="loading">加载中</div>
        
        <div class="result" id="result"></div>
        
        <div class="footer">
            <p>基于原生JavaScript实现的省市联动效果</p>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const provinceSelect = document.getElementById('province');
            const citySelect = document.getElementById('city');
            const resultDiv = document.getElementById('result');
            const loadingDiv = document.getElementById('loading');
            
            // 模拟获取省份数据
            fetchProvinces();
            
            // 省份选择变化时获取城市数据
            provinceSelect.addEventListener('change', function() {
                const provinceId = this.value;
                
                // 重置城市选择
                citySelect.innerHTML = '<option value="">请选择城市</option>';
                citySelect.disabled = !provinceId;
                resultDiv.style.display = 'none';
                
                if (provinceId) {
                    fetchCities(provinceId);
                }
            });
            
            // 城市选择变化时显示结果
            citySelect.addEventListener('change', function() {
                if (this.value) {
                    const provinceText = provinceSelect.options[provinceSelect.selectedIndex].text;
                    const cityText = this.options[this.selectedIndex].text;
                    
                    resultDiv.innerHTML = `您选择了: <strong>${provinceText} - ${cityText}</strong>`;
                    resultDiv.style.display = 'block';
                } else {
                    resultDiv.style.display = 'none';
                }
            });
            
            // 模拟获取省份数据函数
            function fetchProvinces() {
                showLoading();
                
                // 这里应该是axios请求，我们模拟一下
                setTimeout(() => {
                    // 模拟API返回的省份数据
                    const provinces = [
                        { id: '1', name: '北京市' },
                        { id: '2', name: '上海市' },
                        { id: '3', name: '广东省' },
                        { id: '4', name: '江苏省' },
                        { id: '5', name: '浙江省' },
                        { id: '6', name: '四川省' },
                        { id: '7', name: '湖北省' }
                    ];
                    
                    // 填充省份下拉框
                    provinces.forEach(province => {
                        const option = document.createElement('option');
                        option.value = province.id;
                        option.textContent = province.name;
                        provinceSelect.appendChild(option);
                    });
                    
                    hideLoading();
                }, 800);
            }
            
            // 模拟获取城市数据函数
            function fetchCities(provinceId) {
                showLoading();
                citySelect.disabled = true;
                
                // 这里应该是axios请求，我们模拟一下
                setTimeout(() => {
                    // 清空现有城市选项（保留第一个提示选项）
                    citySelect.innerHTML = '<option value="">请选择城市</option>';
                    
                    // 模拟不同省份的城市数据
                    const citiesData = {
                        '1': [ // 北京
                            { id: '101', name: '东城区' },
                            { id: '102', name: '西城区' },
                            { id: '103', name: '朝阳区' },
                            { id: '104', name: '海淀区' },
                            { id: '105', name: '丰台区' }
                        ],
                        '2': [ // 上海
                            { id: '201', name: '黄浦区' },
                            { id: '202', name: '徐汇区' },
                            { id: '203', name: '长宁区' },
                            { id: '204', name: '静安区' },
                            { id: '205', name: '浦东新区' }
                        ],
                        '3': [ // 广东
                            { id: '301', name: '广州市' },
                            { id: '302', name: '深圳市' },
                            { id: '303', name: '珠海市' },
                            { id: '304', name: '东莞市' },
                            { id: '305', name: '佛山市' }
                        ],
                        '4': [ // 江苏
                            { id: '401', name: '南京市' },
                            { id: '402', name: '苏州市' },
                            { id: '403', name: '无锡市' },
                            { id: '404', name: '常州市' },
                            { id: '405', name: '扬州市' }
                        ],
                        '5': [ // 浙江
                            { id: '501', name: '杭州市' },
                            { id: '502', name: '宁波市' },
                            { id: '503', name: '温州市' },
                            { id: '504', name: '嘉兴市' },
                            { id: '505', name: '绍兴市' }
                        ],
                        '6': [ // 四川
                            { id: '601', name: '成都市' },
                            { id: '602', name: '绵阳市' },
                            { id: '603', name: '德阳市' },
                            { id: '604', name: '宜宾市' },
                            { id: '605', name: '泸州市' }
                        ],
                        '7': [ // 湖北
                            { id: '701', name: '武汉市' },
                            { id: '702', name: '宜昌市' },
                            { id: '703', name: '襄阳市' },
                            { id: '704', name: '荆州市' },
                            { id: '705', name: '黄石市' }
                        ]
                    };
                    
                    // 填充城市下拉框
                    const cities = citiesData[provinceId] || [];
                    cities.forEach(city => {
                        const option = document.createElement('option');
                        option.value = city.id;
                        option.textContent = city.name;
                        citySelect.appendChild(option);
                    });
                    
                    citySelect.disabled = false;
                    hideLoading();
                }, 1000);
            }
            
            function showLoading() {
                loadingDiv.style.display = 'block';
            }
            
            function hideLoading() {
                loadingDiv.style.display = 'none';
            }
        });
    </script>
</body>
</html>
```

最终效果如下：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1750389964707-b6d8b7ef-21cd-4881-bc85-808b9e7cdca2.png)

---

## 实现搜索联想自动补全效果

前端页面给大家：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>自动补全输入框</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            width: 100%;
            max-width: 500px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 30px;
        }
        
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
            font-weight: 500;
        }
        
        .autocomplete {
            position: relative;
            width: 100%;
        }
        
        #autocomplete-input {
            width: 100%;
            padding: 12px 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            outline: none;
            transition: border 0.3s;
        }
        
        #autocomplete-input:focus {
            border-color: #4285f4;
        }
        
        .suggestions {
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            border: 1px solid #ddd;
            border-top: none;
            border-radius: 0 0 4px 4px;
            max-height: 200px;
            overflow-y: auto;
            z-index: 100;
            display: none;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .suggestion-item {
            padding: 10px 15px;
            cursor: pointer;
            transition: background 0.2s;
        }
        
        .suggestion-item:hover {
            background-color: #f5f5f5;
        }
        
        .suggestion-item.highlighted {
            background-color: #e8f0fe;
            color: #4285f4;
        }
        
        .loading {
            padding: 10px 15px;
            color: #777;
            font-size: 14px;
            text-align: center;
            display: none;
        }
        
        .no-suggestions {
            padding: 10px 15px;
            color: #777;
            font-size: 14px;
            text-align: center;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>自动补全输入框</h1>
        
        <div class="autocomplete">
            <input type="text" id="autocomplete-input" placeholder="请输入内容..." autocomplete="off">
            <div class="suggestions" id="suggestions">
                <div class="loading" id="loading">加载中...</div>
                <div class="no-suggestions" id="no-suggestions">无匹配项</div>
                <div id="suggestions-list"></div>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const input = document.getElementById('autocomplete-input');
            const suggestionsContainer = document.getElementById('suggestions');
            const suggestionsList = document.getElementById('suggestions-list');
            const loadingElement = document.getElementById('loading');
            const noSuggestionsElement = document.getElementById('no-suggestions');
            
            let debounceTimer;
            let currentSuggestions = [];
            let highlightedIndex = -1;
            
            // 输入事件处理
            input.addEventListener('input', function() {
                const value = this.value.trim();
                
                clearTimeout(debounceTimer);
                
                if (value.length === 0) {
                    hideSuggestions();
                    return;
                }
                
                // 显示加载状态
                showLoading();
                hideNoSuggestions();
                suggestionsList.innerHTML = '';
                
                // 防抖处理
                debounceTimer = setTimeout(() => {
                    fetchSuggestions(value);
                }, 300);
            });
            
            // 键盘事件处理
            input.addEventListener('keydown', function(e) {
                // 向下箭头
                if (e.key === 'ArrowDown') {
                    e.preventDefault();
                    navigateSuggestions(1);
                }
                // 向上箭头
                else if (e.key === 'ArrowUp') {
                    e.preventDefault();
                    navigateSuggestions(-1);
                }
                // 回车键
                else if (e.key === 'Enter') {
                    if (highlightedIndex >= 0 && highlightedIndex < currentSuggestions.length) {
                        selectSuggestion(currentSuggestions[highlightedIndex]);
                    }
                }
                // ESC键
                else if (e.key === 'Escape') {
                    hideSuggestions();
                }
            });
            
            // 输入框聚焦事件
            input.addEventListener('focus', function() {
                const value = this.value.trim();
                if (value.length > 0) {
                    fetchSuggestions(value);
                }
            });
            
            // 点击文档其他区域隐藏建议框
            document.addEventListener('click', function(e) {
                if (!input.contains(e.target) && !suggestionsContainer.contains(e.target)) {
                    hideSuggestions();
                }
            });
            
            // 获取建议
            function fetchSuggestions(query) {
                // 模拟API请求
                setTimeout(() => {
                    // 模拟数据 - 实际项目中替换为真实数据
                    const mockData = ['JavaScript指南', 'JavaScript教程', 'Java程序员'];
                    
                    // 过滤匹配项
                    currentSuggestions = mockData.filter(item => 
                        item.toLowerCase().includes(query.toLowerCase())
                    );
                    
                    renderSuggestions();
                    
                    // 隐藏加载状态
                    hideLoading();
                    
                    // 显示或隐藏建议框
                    if (currentSuggestions.length > 0) {
                        showSuggestions();
                        hideNoSuggestions();
                    } else {
                        showNoSuggestions();
                    }
                }, 500);
            }
            
            // 渲染建议列表
            function renderSuggestions() {
                suggestionsList.innerHTML = '';
                highlightedIndex = -1;
                
                currentSuggestions.forEach((item, index) => {
                    const div = document.createElement('div');
                    div.className = 'suggestion-item';
                    div.textContent = item;
                    div.addEventListener('click', () => selectSuggestion(item));
                    suggestionsList.appendChild(div);
                });
            }
            
            // 导航建议项
            function navigateSuggestions(direction) {
                if (currentSuggestions.length === 0) return;
                
                // 移除之前的高亮
                if (highlightedIndex >= 0) {
                    suggestionsList.children[highlightedIndex].classList.remove('highlighted');
                }
                
                // 计算新的高亮索引
                highlightedIndex += direction;
                
                // 循环处理
                if (highlightedIndex < 0) {
                    highlightedIndex = currentSuggestions.length - 1;
                } else if (highlightedIndex >= currentSuggestions.length) {
                    highlightedIndex = 0;
                }
                
                // 添加新的高亮
                suggestionsList.children[highlightedIndex].classList.add('highlighted');
                
                // 滚动到可见区域
                suggestionsList.children[highlightedIndex].scrollIntoView({
                    block: 'nearest'
                });
            }
            
            // 选择建议项
            function selectSuggestion(value) {
                input.value = value;
                hideSuggestions();
                input.focus();
            }
            
            // 显示建议框
            function showSuggestions() {
                suggestionsContainer.style.display = 'block';
            }
            
            // 隐藏建议框
            function hideSuggestions() {
                suggestionsContainer.style.display = 'none';
                highlightedIndex = -1;
            }
            
            // 显示加载状态
            function showLoading() {
                loadingElement.style.display = 'block';
            }
            
            // 隐藏加载状态
            function hideLoading() {
                loadingElement.style.display = 'none';
            }
            
            // 显示无建议提示
            function showNoSuggestions() {
                noSuggestionsElement.style.display = 'block';
                suggestionsList.style.display = 'none';
                showSuggestions();
            }
            
            // 隐藏无建议提示
            function hideNoSuggestions() {
                noSuggestionsElement.style.display = 'none';
                suggestionsList.style.display = 'block';
            }
        });
    </script>
</body>
</html>
```

最终效果：

![](https://cdn.nlark.com/yuque/0/2025/png/21376908/1750390450511-b06da9a2-d4d4-4573-8aee-78d49256b14a.png)
