# -*- coding: utf-8 -*-
# @Author: dshj
# @Date  :  2020/04/26

import sys
import os
import time
from shutil import copyfile
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon

 
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('Knowledge Map Viewer')
        # 设置窗口大小900*600
        self.resize(1300, 700)
        self.show()
        self.setWindowIcon(QIcon('xianhua.gif'))


        #####创建tabwidget
        self.tabWidget = QTabWidget()
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.tabCloseRequested.connect(self.close_Tab)
        self.setCentralWidget(self.tabWidget)
 
        #自定义浏览器右键菜单
        self.web_menu = WebMenu()
 
        ####第一个tab
        self.webview = QWebEngineView(self)   #将主窗口作为参数，传给浏览器
        
        """关键代码"""
        self.webview.setContextMenuPolicy(Qt.CustomContextMenu)     #将浏览器右键菜单设置为用户自定义菜单
        self.webview.customContextMenuRequested.connect(self.MyBrowser_Menu)#将菜单的信号链接到自定义菜单槽函数
        """关键代码"""
 
        self.webview.load(QUrl("file://"+os.getcwd()+"/render.html"))
        self.create_tab(self.webview)
 
 
    #创建tab
    def create_tab(self,webview):
        self.tab = QWidget()
        self.tabWidget.addTab(self.tab,"PKM")
        self.tabWidget.setCurrentWidget(self.tab)
        #####
        self.Layout = QHBoxLayout(self.tab)
        self.Layout.setContentsMargins(0, 0, 0, 0)
        self.Layout.addWidget(webview)
 
 
    #关闭标签
    def close_Tab(self,index):
        if self.tabWidget.count()>1:
            self.tabWidget.removeTab(index)
        else:
            QCoreApplication.quit()
            
 
 
    #创建自定义浏览器右键菜单
    def MyBrowser_Menu(self,pos):
        action = self.web_menu.exec_(self.webview.mapToGlobal(pos))
        if action == self.web_menu.rebuild_act:
            self.rebuild_slot()
        elif action == self.web_menu.reload_act:
            self.reload_slot()
 

    def rebuild_slot(self):
        os.popen("open "+os.getcwd()+"/PKM-BUILD.command;");
        import time
        time.sleep(1)
        
        self.webview.load(QUrl("file://"+os.getcwd()+"/render.html"))

        #CREATE_NO_WINDOW = 0x08000000 ->only for windows
        #subprocess.call("open "+os.getcwd()+"/PKM-BUILD.command", creationflags=CREATE_NO_WINDOW)

        #这是一个失败的方法
        """
        source = 'run.py'
        target = "run_temp.py"
        with open(source) as f:
            con = f.read();
        tag1 = con.rfind("##<TAG-STAST>")
        tag2 = con.rfind("##<TAG-END>")
        con = con[:tag1]+'\n'+con[tag2+13:]
        #print(con)
        with open(target, "w") as f:
            f.write(con)
        import run_temp
        run_temp.run(Build_Only=True)
        time.sleep(1)
        self.webview.load(QUrl("file://"+os.getcwd()+"/render.html"))
        con = " ""def run():
    print("It's fake run")" ""
        with open(target, "w") as f:
            f.write(con)
        del run_temp
        print("Deleted last run_temp")
        """
        
    def reload_slot(self):
        self.webview.load(QUrl("file://"+os.getcwd()+"/render.html"))


#自定义的一个菜单类
class WebMenu(QMenu):
    def __init__(self):
        super(WebMenu, self).__init__()
        # 定义一个浏览器右键菜单
        self.rebuild_act = QAction("Rebuild")
        self.reload_act = QAction("Reload")
        self.addAction(self.rebuild_act)
        self.addAction(self.reload_act)
 

# 程序入口

def run():
    app = QApplication(sys.argv)
    the_mainwindow = MainWindow()
    the_mainwindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
