import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'

// v-for示例
createApp({
    data() {
        return {
            items: ['苹果', '香蕉', '橙子'],
            user: {
                name: '张三',
                age: 25,
                gender: '男'
            }
        }
    }
}).mount('#v-for-example');

// v-bind示例
createApp({
    data() {
        return {
            classObject: {
                active: true,
                error: false
            },
            styleObject: {
                color: 'blue',
                fontSize: '20px'
            },
            inputValue: '初始值',
            clickCount: 0
        }
    },
    methods: {
        toggleClass() {
            this.classObject.active = !this.classObject.active;
            // 当active为false时添加error类
            this.classObject.error = !this.classObject.error;
        },
        changeStyle() {
            this.styleObject.color = this.styleObject.color === 'blue' ? 'red' : 'blue';
            this.styleObject.fontSize = parseInt(this.styleObject.fontSize) + 2 + 'px';
        },
        handleClick() {
            this.clickCount++;
            alert(`按钮被点击了 ${this.clickCount} 次`);
        }
    }
}).mount('#v-bind-example');

// v-if和v-show示例
createApp({
    data() {
        return {
            showMessage: true
        }
    },
    methods: {
        toggleMessage() {
            this.showMessage = !this.showMessage;
        }
    }
}).mount('#v-if-example');

