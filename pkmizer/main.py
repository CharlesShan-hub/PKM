import sys
import importlib.util
import os
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QListWidget, QTextEdit,
    QLabel, QSplitter, QFrame, QLineEdit, QFileDialog,
    QGridLayout, QGroupBox, QCheckBox
)
from PySide6.QtCore import Qt, QThread, Signal, QObject
from PySide6.QtGui import QFont, QIcon


import io
import sys
import contextlib

class ScriptRunner(QObject):
    finished = Signal(str)
    error = Signal(str)
    output = Signal(str)  # 新增：用于发送print输出

    def __init__(self, script_path, args=None):
        super().__init__()
        self.script_path = script_path
        self.args = args or {}

    def run(self):
        try:
            spec = importlib.util.spec_from_file_location(
                "script_module", self.script_path
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, 'run'):
                # 创建字符串缓冲区来捕获输出
                output_buffer = io.StringIO()
                
                # 使用contextlib重定向标准输出
                with contextlib.redirect_stdout(output_buffer):
                    with contextlib.redirect_stderr(output_buffer):
                        result = module.run(**self.args)
                
                # 获取捕获的输出
                captured_output = output_buffer.getvalue()
                
                # 发送捕获的输出到GUI
                if captured_output:
                    self.output.emit(captured_output)
                
                # 发送最终结果
                self.finished.emit(str(result))
            else:
                self.error.emit(f"Script {self.script_path} has no 'run' function")
        except Exception as e:
            self.error.emit(f"Error running script: {str(e)}")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scripts_dir = Path(__file__).parent / "scripts"
        self.init_ui()
        self.load_scripts()

    def init_ui(self):
        self.setWindowTitle("PKM Tools")
        self.setGeometry(100, 100, 1000, 700)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(15, 15, 15, 15)

        left_panel = QFrame()
        left_panel.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        left_panel.setMinimumWidth(250)  # 设置最小宽度
        left_layout = QVBoxLayout(left_panel)
        left_layout.setSpacing(10)
        left_layout.setContentsMargins(10, 10, 10, 10)

        title_label = QLabel("PKM Tools")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(title_label)

        left_layout.addWidget(QLabel("Available Tools:"))

        self.script_list = QListWidget()
        self.script_list.itemClicked.connect(self.on_script_selected)
        left_layout.addWidget(self.script_list)

        self.description_label = QLabel("Select a tool to see description")
        self.description_label.setWordWrap(True)
        left_layout.addWidget(self.description_label)

        # 参数输入区域
        self.params_group = QGroupBox("Tool Parameters")
        self.params_group.setVisible(False)
        params_layout = QGridLayout(self.params_group)
        params_layout.setSpacing(8)
        params_layout.setContentsMargins(10, 15, 10, 10)
        params_layout.setColumnStretch(0, 1)  # 第一列可拉伸
        params_layout.setColumnStretch(1, 1)  # 第二列可拉伸
        self.params_group.setMinimumHeight(200)
        self.params_group.setMaximumHeight(300)
        
        self.param_widgets = {}
        self.current_param_prompts = {}
        
        left_layout.addWidget(self.params_group)
        left_layout.addStretch()

        right_panel = QFrame()
        right_panel.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        right_layout = QVBoxLayout(right_panel)
        right_layout.setSpacing(10)
        right_layout.setContentsMargins(10, 10, 10, 10)

        right_layout.addWidget(QLabel("Output:"))

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setFont(QFont("Courier", 10))
        right_layout.addWidget(self.output_text)

        # 创建按钮区域
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        self.run_button = QPushButton("Run Selected Tool")
        self.run_button.clicked.connect(self.run_selected_script)
        self.run_button.setFixedHeight(35)
        self.run_button.setEnabled(False)  # 初始禁用
        
        clear_button = QPushButton("Clear Output")
        clear_button.clicked.connect(self.clear_output)
        clear_button.setFixedHeight(35)
        
        button_layout.addWidget(self.run_button)
        button_layout.addWidget(clear_button)
        button_layout.addStretch()
        
        # 将按钮区域添加到主布局
        right_layout.addLayout(button_layout)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([350, 650])  # 左侧稍微宽一点
        splitter.setHandleWidth(8)
        splitter.setStretchFactor(0, 1)  # 左侧可拉伸
        splitter.setStretchFactor(1, 3)  # 右侧可拉伸更多

        main_layout.addWidget(splitter)

    def load_scripts(self):
        if not self.scripts_dir.exists():
            self.scripts_dir.mkdir(parents=True)
            self.output_text.append("Created scripts directory")
            return

        self.script_list.clear()
        for script_file in self.scripts_dir.glob("*.py"):
            if script_file.name != "__init__.py":
                self.script_list.addItem(script_file.stem)

    def on_script_selected(self, item):
        script_name = item.text()
        script_path = self.scripts_dir / f"{script_name}.py"
        
        try:
            spec = importlib.util.spec_from_file_location(
                "temp_module", script_path
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            description = getattr(module, 'DESCRIPTION', "No description available")
            self.description_label.setText(f"<b>{script_name}:</b><br>{description}")
            
            # 清空之前的参数控件
            self.clear_param_widgets()
            
            # 检查脚本是否有参数提示
            if hasattr(module, 'PARAM_PROMPTS'):
                self.setup_parameters(module.PARAM_PROMPTS)
                self.params_group.setVisible(True)
            else:
                self.params_group.setVisible(False)
            
            self.run_button.setEnabled(True)
            
        except Exception as e:
            self.description_label.setText(f"Error loading script: {str(e)}")
            self.clear_param_widgets()
            self.params_group.setVisible(False)
            self.run_button.setEnabled(False)

    def run_selected_script(self):
        current_item = self.script_list.currentItem()
        if not current_item:
            return

        script_name = current_item.text()
        script_path = self.scripts_dir / f"{script_name}.py"
        
        # 收集参数值
        args = {}
        for param_name, widgets in self.param_widgets.items():
            if 'input' in widgets:
                value = widgets['input'].text().strip()
                if value:
                    args[param_name] = value
            elif 'checkbox' in widgets:
                args[param_name] = widgets['checkbox'].isChecked()
        
        self.output_text.append(f"\n{'='*50}")
        self.output_text.append(f"Running: {script_name}")
        if args:
            self.output_text.append(f"Parameters: {args}")
        self.output_text.append(f"{'='*50}\n")

        self.thread = QThread()
        self.runner = ScriptRunner(script_path, args)
        self.runner.moveToThread(self.thread)
        
        self.thread.started.connect(self.runner.run)
        self.runner.finished.connect(self.on_script_finished)
        self.runner.error.connect(self.on_script_error)
        self.runner.output.connect(self.on_script_output)  # 连接输出信号
        self.runner.finished.connect(self.thread.quit)
        self.runner.error.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater)
        
        self.thread.start()

    def on_script_finished(self, result):
        """处理脚本完成时的最终结果"""
        if result:
            # 添加分隔线
            self.output_text.append("\n" + "=" * 60)
            self.output_text.append("脚本执行完成 - 最终结果:")
            self.output_text.append("=" * 60)
            
            # 按行显示结果，确保格式正确
            lines = result.split('\n')
            for line in lines:
                if line.strip():
                    self.output_text.append(line)
            
            # 添加结束分隔线
            self.output_text.append("=" * 60)
            
            # 确保输出区域滚动到底部
            self.output_text.verticalScrollBar().setValue(
                self.output_text.verticalScrollBar().maximum()
            )

    def on_script_output(self, output_text):
        """处理脚本的print输出"""
        if output_text:
            # 按行分割输出，确保每行都正确显示
            lines = output_text.split('\n')
            for line in lines:
                if line.strip():  # 只显示非空行
                    self.output_text.append(line)
            # 确保输出区域滚动到底部
            self.output_text.verticalScrollBar().setValue(
                self.output_text.verticalScrollBar().maximum()
            )
    
    def on_script_error(self, error_msg):
        self.output_text.append(f"Error: {error_msg}")
        self.output_text.append(f"\n{'='*50}")
        self.output_text.append("Script failed")
        self.output_text.append(f"{'='*50}")

    def setup_parameters(self, param_prompts):
        """根据参数提示设置参数输入控件"""
        # 保存当前的参数提示信息，供browse_path方法使用
        self.current_param_prompts = param_prompts
        
        layout = self.params_group.layout()
        
        row = 0
        for param_name, prompt_info in param_prompts.items():
            label_text = prompt_info.get('label', param_name)
            param_type = prompt_info.get('type', 'str')
            default_value = prompt_info.get('default', '')
            
            # 第一行：参数标签
            label = QLabel(f"{label_text}:")
            label.setStyleSheet("font-weight: bold;")
            layout.addWidget(label, row, 0, 1, 2)  # 跨两列
            row += 1
            
            # 第二行：输入控件
            if param_type == 'bool':
                checkbox = QCheckBox()
                checkbox.setChecked(bool(default_value))
                layout.addWidget(checkbox, row, 0, 1, 2)  # 跨两列
                self.param_widgets[param_name] = {'checkbox': checkbox}
            else:
                input_widget = QLineEdit()
                input_widget.setText(str(default_value))
                
                # 如果是路径或文件参数，添加浏览按钮
                if param_type == 'path' or param_type == 'file':
                    browse_button = QPushButton("Browse...")
                    browse_button.setFixedWidth(80)
                    
                    # 为输入目录添加文本改变事件监听
                    if param_name == 'input_dir':
                        input_widget.textChanged.connect(
                            lambda text, output_widget=self.get_output_widget(): 
                            self.auto_fill_output_dir(text, output_widget)
                        )
                    
                    browse_button.clicked.connect(
                        lambda checked, p=param_name, i=input_widget: 
                        self.browse_path(p, i)
                    )
                    
                    # 创建水平布局，让输入框自动扩展
                    hbox = QHBoxLayout()
                    hbox.addWidget(input_widget, 1)  # 添加拉伸因子1
                    hbox.addWidget(browse_button)
                    hbox.setContentsMargins(0, 0, 0, 0)
                    
                    hbox_widget = QWidget()
                    hbox_widget.setLayout(hbox)
                    layout.addWidget(hbox_widget, row, 0, 1, 2)  # 跨两列
                else:
                    layout.addWidget(input_widget, row, 0, 1, 2)  # 跨两列
                
                self.param_widgets[param_name] = {'input': input_widget}
            
            # 添加间距
            row += 1
            
            # 添加空行作为间距
            spacer = QLabel("")
            spacer.setFixedHeight(5)
            layout.addWidget(spacer, row, 0, 1, 2)
            row += 1
    
    def browse_path(self, param_name, input_widget):
        """打开文件对话框选择路径"""
        current_path = input_widget.text()
        
        # 检查是文件还是目录
        if os.path.exists(current_path):
            if os.path.isfile(current_path):
                start_dir = os.path.dirname(current_path)
            else:
                start_dir = current_path
        else:
            start_dir = os.path.expanduser("~")
        
        # 获取参数类型（从param_prompts中）
        param_type = None
        for name, widgets in self.param_widgets.items():
            if name == param_name:
                # 查找对应的参数提示信息
                if hasattr(self, 'current_param_prompts') and param_name in self.current_param_prompts:
                    param_type = self.current_param_prompts[param_name].get('type', 'str')
                break
        
        # 根据参数类型选择对话框
        if param_type == 'file':
            # 文件选择对话框
            file_path, _ = QFileDialog.getOpenFileName(
                self, f"Select {param_name} file", start_dir
            )
            if file_path:
                input_widget.setText(file_path)
        elif "input" in param_name.lower() or "dir" in param_name.lower() or "directory" in param_name.lower() or param_type == 'path':
            # 目录选择对话框
            dir_path = QFileDialog.getExistingDirectory(
                self, f"Select {param_name} directory", start_dir
            )
            if dir_path:
                input_widget.setText(dir_path)
                
                # 如果是输入目录，自动填充输出目录
                if param_name == 'input_dir':
                    output_widget = self.get_output_widget()
                    if output_widget:
                        self.auto_fill_output_dir(dir_path, output_widget)
        else:
            # 默认使用文件选择
            file_path, _ = QFileDialog.getOpenFileName(
                self, f"Select {param_name} file", start_dir
            )
            if file_path:
                input_widget.setText(file_path)
    
    def get_output_widget(self):
        """获取输出目录的输入控件"""
        if 'output_dir' in self.param_widgets and 'input' in self.param_widgets['output_dir']:
            return self.param_widgets['output_dir']['input']
        return None
    
    def auto_fill_output_dir(self, input_dir, output_widget):
        """根据输入目录自动填充输出目录为../assets"""
        if not input_dir:
            return
        
        try:
            input_path = Path(input_dir)
            # 获取输入目录的父目录
            parent_dir = input_path.parent
            # 构建输出目录路径：父目录/assets
            output_dir = parent_dir / "assets"
            
            # 只在不为空时才更新
            if not output_widget.text():
                output_widget.setText(str(output_dir))
        except Exception as e:
            print(f"自动填充输出目录时出错: {e}")
    
    def clear_param_widgets(self):
        """清理参数控件"""
        # 移除所有子控件
        layout = self.params_group.layout()
        if layout:
            while layout.count():
                item = layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
        
        self.param_widgets = {}
        self.current_param_prompts = {}
    
    def clear_output(self):
        self.output_text.clear()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()