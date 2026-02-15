# brew

---
## Introduction

* 官网: https://brew.sh/
* 简介: Homebrew是一款Mac OS平台下的软件包管理工具
* 安装
	* 需要 Xcode
	* 运行命令
		```bash
		/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
		```

---

## Brew管理

* brew版本
	```shell
	brew -v
	brew --version
	```
* brew更新
	```shell
	brew update
	```
* brew本身的目录
	```shell
	/usr/local/Homebrew
	```
* 包的安装文件目录
	```shell
	/usr/local/Cellar
	```
* 包的配置文件目录
	```shell
	/usr/local/etc
	```
* 包的二进制可执行程序的软连接目录
	```shell
	/usr/local/bin
	```
* 查看brew设置
	```shell
	brew config
	```
* 查看环境是否“健康”
	```shell
	brew doctor
	```
* 清理缓存
	```shell
	brew cleanup
	```
* 查看可清理内容（不实际执行）
	```shell
	brew cleanup -n
	```
* 列出所有可用的命令
	```shell
	brew commands
	```
* 帮助
	```shell
	brew help
	```

---

## 包管理

* 搜寻软件包的信息，支持正则表达式
	```shell
	brew search TEXT|/REGEX/
	```
* 显示软件包的详细信息（显示某一个包的信息）
	```shell
	brew info [FORMULA|CASK...]
	```
* 显示软件包的详细信息（json格式）
	```shell
	brew info --json [FORMULA|CASK...]
	```
* 安装软件包
	```shell
	brew install FORMULA|CASK...
	```
* 安装软件包（空运行）
	```shell
	brew install FORMULA|CASK... --dry-run
	```
* 安装软件包并输出错误信息
	```shell
	brew install --verbose --debug FORMULA|CASK
	```
* 卸载软件包
	```shell
	brew uninstall FORMULA|CASK...
	```
* 卸载软件包（空运行）
	```shell
	brew install FORMULA|CASK... --dry-run
	```
* 查看所有安装的包
	```shell
	brew list [FORMULA|CASK...]
	```
* 查看过时的软件包
	```shell
	brew outdated
	```
* 更新所有过时的软件包
	```shell
	brew upgrade
	```
* 更新某个软件包
	```shell
	brew upgrade [FORMULA|CASK...]
	```
* 显示依赖关系
	```shell
	brew deps <formula>
	```
* 显示哪些软件依赖它
	```shell
	brew uses <formula>
	```

---

## 服务管理

* 查看有什么服务
	```shell
	brew services list
	```
* 启动服务
	```shell
	brew services run 服务名称
	```
* 启动服务
	```shell
	brew services start 服务名称
	```
* 停止服务
	```shell
	brew services stop 服务名称
	```
* 重启服务
	```shell
	brew services restart 服务名称
	```
* 清除已卸载应用的无用配置
	```shell
	brew services cleanup
	```

---

## 提交包

* 根据URL构建一个框架
	```shell
	brew create URL [--no-fetch]
	```
* 编辑生成的公式
	```shell
	brew edit [FORMULA|CASK...]
	```
* 测试安装
	```shell
	brew install --build-from-source <package-name>
	```
