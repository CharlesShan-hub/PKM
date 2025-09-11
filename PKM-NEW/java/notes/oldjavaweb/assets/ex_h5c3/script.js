import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'

createApp({
    data() {
        return {
            formData: {
                name: '',
                gender: '',
                job: ''
            },
            users: [
                // {
                //     name: '令狐冲',
                //     gender: '男',
                //     image: 'https://web-framework.oss-cn-hangzhou.aliyuncs.com/2023/1.jpg',
                //     job: '1',
                //     entrydate: '2020-05-15',
                //     updatetime: '2023-06-10 14:30'
                // },
                // {
                //     name: '任盈盈',
                //     gender: '女',
                //     image: 'https://web-framework.oss-cn-hangzhou.aliyuncs.com/2023/2.jpg',
                //     job: '2',
                //     entrydate: '2019-08-20',
                //     updatetime: '2023-06-08 09:45'
                // },
                // {
                //     name: '岳不群',
                //     gender: '男',
                //     image: 'https://web-framework.oss-cn-hangzhou.aliyuncs.com/2023/3.jpg',
                //     job: '3',
                //     entrydate: '2018-03-10',
                //     updatetime: '2023-06-05 16:20'
                // }
            ]
        }
    },
    methods: {
        editUser(index) {
            const user = this.users[index]
            console.log('编辑用户:', user)
            // 这里可以添加编辑逻辑
            alert(`正在编辑用户: ${user.name}`)
        },
        deleteUser(index) {
            if (confirm('确定要删除这个用户吗？')) {
                this.users.splice(index, 1)
                alert('用户已删除')
            }
        },
        clearForm() {
            this.formData = {
                name: '',
                gender: '',
                job: ''
            };
            this.search();
        },
        // 异步
        // search() {
        //     axios.get(`https://web-server.itheima.net/emps/list?name=${this.formData.name}&gender=${this.formData.gender}&job=${this.formData.job}`)
        //         .then(response => {
        //             this.users = response.data.data
        //         })
        //         .catch(error => {
        //             console.error('搜索失败:', error)   
        //         })
        // }
        // 同步
        async search() {
            let result = await axios.get(`https://web-server.itheima.net/emps/list?name=${this.formData.name}&gender=${this.formData.gender}&job=${this.formData.job}`);
            this.users = result.data.data;
        }
    },
    mounted() { // 页面加载完成后执行，钩子函数
        // 设置当前年份
        document.getElementById('currentYear').textContent = new Date().getFullYear()
        // 初始化用户列表
        this.search();
    }
}).mount('#app')