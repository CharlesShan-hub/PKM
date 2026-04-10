import sys
import json
import importlib.util
import os
import io
import time
import threading
import queue
from pathlib import Path
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QListWidget, QTextEdit,
    QLabel, QSplitter, QFrame, QLineEdit, QFileDialog,
    QGridLayout, QGroupBox, QCheckBox, QComboBox, QInputDialog,
    QMessageBox, QDialog, QScrollArea, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt, QThread, Signal, QObject, QTimer
from PySide6.QtGui import QFont, QIcon


# 全局输出队列（供脚本和主程序共享）
output_queue = queue.Queue()

# API Key 配置文件路径
CONFIG_FILE = Path(__file__).parent / ".api_key"


def load_api_key():
    """从配置文件读取 API Key"""
    try:
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                return f.read().strip()
    except Exception:
        pass
    return ""


def save_api_key(api_key):
    """保存 API Key 到配置文件"""
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            f.write(api_key.strip())
        return True
    except Exception as e:
        print(f"保存 API Key 失败: {e}")
        return False


class ScriptRunner(QObject):
    """使用队列模式：子线程执行，主线程定期读取队列"""
    finished = Signal(str)
    error = Signal(str)

    def __init__(self, script_path, args=None):
        super().__init__()
        self.script_path = script_path
        self.args = args or {}
        self._thread = None
        self._stop_flag = False

    def run(self):
        """在新线程中运行脚本"""
        self._thread = threading.Thread(target=self._run_in_thread, daemon=True)
        self._thread.start()

    def _run_in_thread(self):
        """在子线程中执行脚本 - 直接用 importlib"""
        try:
            # 动态加载模块
            spec = importlib.util.spec_from_file_location("script_module", self.script_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            if hasattr(module, 'run'):
                # 收集参数值
                args_dict = {}
                for param_name, param_value in self.args.items():
                    if param_value:
                        args_dict[param_name] = param_value

                # 重定向 stdout 到队列
                original_stdout = sys.stdout
                sys.stdout = QueueWriter(output_queue)

                try:
                    result = module.run(**args_dict)
                    # 输出最终结果
                    if result:
                        output_queue.put(f"\n{'='*60}")
                        output_queue.put("Final Result:")
                        output_queue.put(result)
                        output_queue.put("=" * 60)
                finally:
                    sys.stdout = original_stdout

                self.finished.emit("Done")
            else:
                self.error.emit(f"Script has no 'run' function")

        except Exception as e:
            self.error.emit(f"Error: {str(e)}")

    def stop(self):
        """停止脚本执行"""
        self._stop_flag = True


class QueueWriter:
    """将输出重定向到队列"""
    def __init__(self, q):
        self.queue = q
        self._closed = False

    def write(self, text):
        if text and text.strip() and not self._closed:
            self.queue.put(text)

    def flush(self):
        pass

    def close(self):
        self._closed = True


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.scripts_dir = Path(__file__).parent / "scripts"
        self.prompts_file = Path(__file__).parent / "prompts.json"
        self.prompts_config = {}  # 提示词配置（内存副本，支持编辑）
        self.init_ui()
        self.load_scripts()
        
        # 设置定时器，定期检查输出队列
        self.queue_timer = QTimer()
        self.queue_timer.timeout.connect(self._check_output_queue)
        self.queue_timer.setInterval(100)  # 每 100ms 检查一次
        self._is_running = False
        
        # 加载提示词配置
        self._load_prompts()

    def _check_output_queue(self):
        """定期检查输出队列"""
        if not self._is_running:
            return
        
        try:
            while True:
                line = output_queue.get_nowait()
                self.output_text.append(line)
                # 自动滚动到底部
                self.output_text.verticalScrollBar().setValue(
                    self.output_text.verticalScrollBar().maximum()
                )
        except queue.Empty:
            pass

    def _update_api_key_ui(self):
        """更新 API Key 显示状态"""
        api_key = load_api_key()
        has_key = bool(api_key)
        
        self.api_key_input.setVisible(False)
        self.api_key_status.setVisible(True)
        
        if has_key:
            # 已加载状态：显示 loaded
            self.api_key_status.setText("✅ loaded")
            self.api_key_status.setStyleSheet("color: #27ae60; font-weight: bold;")
        else:
            # 未加载状态
            self.api_key_status.setText("⚠️ unload")
            self.api_key_status.setStyleSheet("color: #e67e22; font-weight: bold;")
        
        self.save_key_btn.setText("✏️")
        self.save_key_btn.setToolTip("Edit")

    def _edit_api_key(self):
        """切换编辑模式"""
        if self.api_key_status.isVisible():
            # 进入编辑模式
            self.api_key_status.setVisible(False)
            self.api_key_input.setVisible(True)
            self.api_key_input.setText(load_api_key())
            self.api_key_input.setFocus()
            self.api_key_input.selectAll()
            self.save_key_btn.setText("💾")
            self.save_key_btn.setToolTip("Save")
        else:
            # 保存
            api_key = self.api_key_input.text().strip()
            if api_key:
                if save_api_key(api_key):
                    self.output_text.append(f"✅ API Key saved")
            else:
                try:
                    if CONFIG_FILE.exists():
                        CONFIG_FILE.unlink()
                    self.output_text.append("✅ API Key cleared")
                except Exception as e:
                    self.output_text.append(f"❌ Failed: {e}")
            
            self._update_api_key_ui()

    def _load_prompts(self):
        """加载提示词配置文件"""
        try:
            if self.prompts_file.exists():
                with open(self.prompts_file, 'r', encoding='utf-8') as f:
                    self.prompts_config = json.load(f)
        except Exception as e:
            print(f"加载提示词配置失败: {e}")
            self.prompts_config = {}

    def _setup_prompt_editor(self, param_prompts):
        """设置提示词编辑器"""
        # 查找是否有 prompt_name 参数
        if 'prompt_name' not in param_prompts:
            self.prompt_editor_group.setVisible(False)
            return
        
        # 填充下拉列表
        self.prompt_combo.blockSignals(True)  # 阻止信号，避免触发 _on_prompt_changed
        self.prompt_combo.clear()
        
        options = param_prompts['prompt_name'].get('options', {})
        default_key = param_prompts['prompt_name'].get('default', '')
        
        for key, display_name in options.items():
            self.prompt_combo.addItem(display_name, key)
            # 如果是默认选项，选中它
            if key == default_key:
                self.prompt_combo.setCurrentIndex(self.prompt_combo.count() - 1)
        
        self.prompt_combo.blockSignals(False)
        
        # 显示编辑区
        self.prompt_editor_group.setVisible(True)
        
        # 加载当前选中提示词的内容
        self._update_prompt_editor()

    def _on_prompt_changed(self, index):
        """下拉选择改变时更新编辑区"""
        self._update_prompt_editor()

    def _update_prompt_editor(self):
        """更新提示词编辑区的内容"""
        current_key = self.prompt_combo.currentData()
        if not current_key or current_key not in self.prompts_config:
            self.system_prompt_edit.clear()
            self.user_prompt_edit.clear()
            return
        
        prompt_data = self.prompts_config[current_key]
        self.system_prompt_edit.setText(prompt_data.get('system_prompt', ''))
        self.user_prompt_edit.setText(prompt_data.get('user_prompt_template', ''))

    def _new_prompt(self):
        """新建提示词"""
        # 弹出输入对话框
        key, ok = QInputDialog.getText(
            self, 'New Prompt', 'Enter prompt key (e.g., my_prompt):',
            text='my_prompt'
        )
        if not ok or not key.strip():
            return
        
        key = key.strip().replace(' ', '_')  # 替换空格为下划线
        
        if key in self.prompts_config:
            QMessageBox.warning(self, 'Warning', 'Prompt key already exists!')
            return
        
        # 输入显示名称
        name, ok = QInputDialog.getText(
            self, 'New Prompt', 'Enter display name:',
            text='My Prompt'
        )
        if not ok or not name.strip():
            return
        
        name = name.strip()
        
        # 添加到配置
        self.prompts_config[key] = {
            'name': name,
            'description': f'Custom prompt: {name}',
            'system_prompt': '',
            'user_prompt_template': '{content}'
        }
        
        # 添加到下拉列表
        self.prompt_combo.blockSignals(True)
        self.prompt_combo.addItem(name, key)
        self.prompt_combo.setCurrentIndex(self.prompt_combo.count() - 1)
        self.prompt_combo.blockSignals(False)
        
        # 清空编辑区
        self.system_prompt_edit.clear()
        self.user_prompt_edit.setPlainText('{content}')
        
        # 更新脚本参数中的 options（如果有的话）
        self._update_script_options()
        
        # 保存到文件
        self._save_prompts()

    def _delete_prompt(self):
        """删除当前提示词"""
        current_key = self.prompt_combo.currentData()
        current_text = self.prompt_combo.currentText()
        
        if not current_key:
            return
        
        # 确认对话框
        reply = QMessageBox.question(
            self, 'Confirm Delete',
            f'Delete prompt "{current_text}"?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply != QMessageBox.Yes:
            return
        
        # 从配置中删除
        if current_key in self.prompts_config:
            del self.prompts_config[current_key]
        
        # 从下拉列表中删除
        self.prompt_combo.blockSignals(True)
        current_index = self.prompt_combo.currentIndex()
        self.prompt_combo.removeItem(current_index)
        self.prompt_combo.blockSignals(False)
        
        # 更新编辑区
        self._update_prompt_editor()
        
        # 更新脚本参数中的 options（如果有的话）
        self._update_script_options()
        
        # 保存到文件
        self._save_prompts()

    def _update_script_options(self):
        """更新当前脚本参数中的 options"""
        if 'prompt_name' in self.current_param_prompts:
            # 构建新的 options
            new_options = {}
            for key, data in self.prompts_config.items():
                new_options[key] = data.get('name', key)
            self.current_param_prompts['prompt_name']['options'] = new_options

    def _save_prompts(self):
        """保存提示词配置到文件"""
        try:
            with open(self.prompts_file, 'w', encoding='utf-8') as f:
                json.dump(self.prompts_config, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存提示词配置失败: {e}")

    def _get_current_prompt(self):
        """获取当前编辑的提示词"""
        current_key = self.prompt_combo.currentData()
        if not current_key:
            return {}, ""
        
        # 更新配置（保存用户编辑的内容）
        self.prompts_config[current_key] = {
            'system_prompt': self.system_prompt_edit.toPlainText(),
            'user_prompt_template': self.user_prompt_edit.toPlainText(),
        }
        
        return self.prompts_config[current_key], current_key

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

        title_label = QLabel("🛠️ PKM Tools")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(title_label)

        # 全局 API Key 设置区域
        api_key_group = QGroupBox("🔑 DeepSeek API Key")
        api_key_group.setStyleSheet("""
            QGroupBox {
                border: 2px solid #3498db;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
            }
        """)
        api_key_layout = QHBoxLayout(api_key_group)
        api_key_layout.setContentsMargins(5, 5, 5, 5)
        
        # API Key 状态显示/编辑区域
        self.api_key_widget = QWidget()
        api_key_inner_layout = QHBoxLayout(self.api_key_widget)
        api_key_inner_layout.setContentsMargins(0, 0, 0, 0)
        api_key_inner_layout.setSpacing(5)
        
        # 状态标签
        self.api_key_status = QLabel()
        self.api_key_status.setFixedWidth(70)
        
        # 输入框（默认隐藏）
        self.api_key_input = QLineEdit()
        self.api_key_input.setPlaceholderText("sk-xxxxx")
        self.api_key_input.setVisible(False)
        
        api_key_inner_layout.addWidget(self.api_key_status)
        api_key_inner_layout.addWidget(self.api_key_input, 1)
        
        # 编辑按钮
        self.save_key_btn = QPushButton("✏️")
        self.save_key_btn.setFixedWidth(40)
        self.save_key_btn.setToolTip("Edit")
        self.save_key_btn.clicked.connect(self._edit_api_key)
        
        api_key_layout.addWidget(self.api_key_widget, 1)
        api_key_layout.addWidget(self.save_key_btn)
        
        # 初始状态
        self._update_api_key_ui()
        
        # 滚动区域容器
        scroll_container = QWidget()
        scroll_layout = QVBoxLayout(scroll_container)
        scroll_layout.setSpacing(12)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        
        scroll_layout.addWidget(api_key_group)

        # Available Tools 区域
        tools_group = QGroupBox("🔧 Available Tools")
        tools_group.setStyleSheet("""
            QGroupBox {
                border: 2px solid #9b59b6;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
            }
        """)
        tools_layout = QVBoxLayout(tools_group)
        tools_layout.setSpacing(10)
        tools_layout.setContentsMargins(12, 18, 12, 12)
        
        # 下拉框 + 描述按钮 同一行
        combo_layout = QHBoxLayout()
        self.script_combo = QComboBox()
        self.script_combo.currentIndexChanged.connect(self.on_script_selected)
        combo_layout.addWidget(self.script_combo, 1)
        
        self.desc_btn = QPushButton("ℹ️")
        self.desc_btn.setFixedWidth(30)
        self.desc_btn.setToolTip("View Description")
        self.desc_btn.clicked.connect(self._show_description_dialog)
        self.desc_btn.setEnabled(False)
        combo_layout.addWidget(self.desc_btn)
        
        tools_layout.addLayout(combo_layout)
        
        scroll_layout.addWidget(tools_group)

        # 参数输入区域
        self.params_group = QGroupBox("⚙️ Tool Parameters")
        self.params_group.setStyleSheet("""
            QGroupBox {
                border: 2px solid #e67e22;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
            }
        """)
        self.params_group.setVisible(False)
        params_layout = QGridLayout(self.params_group)
        params_layout.setSpacing(10)
        params_layout.setContentsMargins(12, 15, 12, 12)
        params_layout.setColumnStretch(0, 1)  # 第一列可拉伸
        params_layout.setColumnStretch(1, 1)  # 第二列可拉伸
        
        self.param_widgets = {}
        self.current_param_prompts = {}
        self.current_script_name = ""
        self.current_script_description = ""
        
        scroll_layout.addWidget(self.params_group)
        
        # 提示词编辑区域（默认隐藏）
        self.prompt_editor_group = QGroupBox("✍️ Prompt Editor")
        self.prompt_editor_group.setStyleSheet("""
            QGroupBox {
                border: 2px solid #27ae60;
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 10px;
            }
        """)
        prompt_editor_layout = QVBoxLayout(self.prompt_editor_group)
        prompt_editor_layout.setSpacing(10)
        prompt_editor_layout.setContentsMargins(12, 15, 12, 12)
        
        # 提示词选择下拉 + 操作按钮
        prompt_select_layout = QHBoxLayout()
        prompt_select_layout.addWidget(QLabel("Template:"))
        self.prompt_combo = QComboBox()
        self.prompt_combo.currentIndexChanged.connect(self._on_prompt_changed)
        prompt_select_layout.addWidget(self.prompt_combo, 1)
        
        # 新建按钮
        self.new_prompt_btn = QPushButton("+")
        self.new_prompt_btn.setFixedWidth(30)
        self.new_prompt_btn.setToolTip("New Prompt")
        self.new_prompt_btn.clicked.connect(self._new_prompt)
        prompt_select_layout.addWidget(self.new_prompt_btn)
        
        # 删除按钮
        self.delete_prompt_btn = QPushButton("-")
        self.delete_prompt_btn.setFixedWidth(30)
        self.delete_prompt_btn.setToolTip("Delete Prompt")
        self.delete_prompt_btn.clicked.connect(self._delete_prompt)
        prompt_select_layout.addWidget(self.delete_prompt_btn)
        
        prompt_editor_layout.addLayout(prompt_select_layout)
        
        # 系统提示词
        system_label = QLabel("System Prompt:")
        system_label.setStyleSheet("font-weight: bold;")
        prompt_editor_layout.addWidget(system_label)
        self.system_prompt_edit = QTextEdit()
        self.system_prompt_edit.setPlaceholderText("System prompt will appear here...")
        self.system_prompt_edit.setFixedHeight(180)
        prompt_editor_layout.addWidget(self.system_prompt_edit)
        
        # 用户提示词模板
        user_label = QLabel("User Prompt Template:")
        user_label.setStyleSheet("font-weight: bold;")
        prompt_editor_layout.addWidget(user_label)
        self.user_prompt_edit = QTextEdit()
        self.user_prompt_edit.setPlaceholderText("User prompt will appear here...\nUse {content} as placeholder for file content.")
        self.user_prompt_edit.setFixedHeight(200)
        prompt_editor_layout.addWidget(self.user_prompt_edit)
        
        # 提示说明
        hint_label = QLabel("Tip: Use {content} as placeholder for file content")
        hint_label.setStyleSheet("color: gray; font-size: 10px;")
        prompt_editor_layout.addWidget(hint_label)
        
        self.prompt_editor_group.setVisible(False)
        scroll_layout.addWidget(self.prompt_editor_group)
        
        scroll_layout.addStretch()
        
        # 滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidget(scroll_container)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.NoFrame)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        left_layout.addWidget(scroll_area)

        # 版权信息
        copyright_label = QLabel("© 2026 PKM Tools · Made with Charles Shan")
        copyright_label.setAlignment(Qt.AlignCenter)
        copyright_label.setStyleSheet("""
            color: #95a5a6;
            font-size: 11px;
            padding: 5px;
        """)
        left_layout.addWidget(copyright_label)

        right_panel = QFrame()
        right_panel.setFrameStyle(QFrame.StyledPanel | QFrame.Raised)
        right_layout = QVBoxLayout(right_panel)
        right_layout.setSpacing(10)
        right_layout.setContentsMargins(10, 10, 10, 10)

        right_layout.addWidget(QLabel("📤 Output:"))

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setFont(QFont("Courier", 10))
        right_layout.addWidget(self.output_text)

        # 创建按钮区域
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        self.run_button = QPushButton("▶️ Run")
        self.run_button.clicked.connect(self.run_selected_script)
        self.run_button.setFixedHeight(35)
        self.run_button.setEnabled(False)  # 初始禁用
        
        self.stop_button = QPushButton("⏹️ Stop")
        self.stop_button.clicked.connect(self.stop_script)
        self.stop_button.setFixedHeight(35)
        self.stop_button.setEnabled(False)  # 初始禁用
        
        clear_button = QPushButton("🗑️ Clear")
        clear_button.clicked.connect(self.clear_output)
        clear_button.setFixedHeight(35)
        
        button_layout.addWidget(self.run_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(clear_button)
        button_layout.addStretch()
        
        # 将按钮区域添加到主布局
        right_layout.addLayout(button_layout)

        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([400, 600])  # 左侧40%，右侧60%
        splitter.setHandleWidth(8)
        splitter.setStretchFactor(0, 1)  # 左侧可拉伸
        splitter.setStretchFactor(1, 3)  # 右侧可拉伸更多

        main_layout.addWidget(splitter)

    def load_scripts(self):
        if not self.scripts_dir.exists():
            self.scripts_dir.mkdir(parents=True)
            self.output_text.append("Created scripts directory")
            return

        self.script_combo.clear()
        for script_file in self.scripts_dir.glob("*.py"):
            if script_file.name != "__init__.py":
                self.script_combo.addItem(script_file.stem)

    def _show_description_dialog(self):
        """显示脚本描述弹窗"""
        if not self.current_script_description:
            return
        
        dialog = QDialog(self)
        dialog.setWindowTitle(f"About: {self.current_script_name}")
        dialog.setMinimumSize(400, 200)
        
        layout = QVBoxLayout(dialog)
        
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setText(self.current_script_description)
        text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #f5f5f5;
                color: #333;
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 10px;
            }
        """)
        layout.addWidget(text_edit)
        
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(dialog.close)
        layout.addWidget(close_btn)
        
        dialog.exec()

    def on_script_selected(self, index):
        if index < 0:
            return
        script_name = self.script_combo.currentText()
        script_path = self.scripts_dir / f"{script_name}.py"
        
        try:
            spec = importlib.util.spec_from_file_location(
                "temp_module", script_path
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            description = getattr(module, 'DESCRIPTION', "No description available")
            
            # 保存描述信息
            self.current_script_name = script_name
            self.current_script_description = description
            self.desc_btn.setEnabled(True)
            
            # 清空之前的参数控件
            self.clear_param_widgets()
            
            # 检查脚本是否有参数提示
            if hasattr(module, 'PARAM_PROMPTS'):
                self.setup_parameters(module.PARAM_PROMPTS)
                self.params_group.setVisible(True)
                # 设置提示词编辑器
                self._setup_prompt_editor(module.PARAM_PROMPTS)
            else:
                self.params_group.setVisible(False)
                self.prompt_editor_group.setVisible(False)
            
            self.run_button.setEnabled(True)
            
        except Exception as e:
            self.current_script_description = f"Error loading script: {str(e)}"
            self.desc_btn.setEnabled(True)
            self.clear_param_widgets()
            self.params_group.setVisible(False)
            self.run_button.setEnabled(False)

    def run_selected_script(self):
        script_name = self.script_combo.currentText()
        if not script_name:
            return
        script_path = self.scripts_dir / f"{script_name}.py"
        
        # 收集参数值 - 作为字典传递
        args = {}
        param_order = []  # 保持参数顺序
        global_api_key = load_api_key()  # 获取全局 API Key
        
        for param_name, widgets in self.param_widgets.items():
            param_order.append(param_name)
            
            # api_key 参数直接使用全局 API Key（不需要UI）
            if param_name == 'api_key':
                args[param_name] = global_api_key
                continue
            
            if 'input' in widgets and widgets['input'] is not None:
                args[param_name] = widgets['input'].text().strip()
            elif 'checkbox' in widgets:
                args[param_name] = widgets['checkbox'].isChecked()
            elif 'combo' in widgets:
                # 下拉列表：获取保存的值（key）而不是显示的文本
                args[param_name] = widgets['combo'].currentData()
        
        # 获取当前提示词编辑器的内容（如果有）
        if self.prompt_editor_group.isVisible():
            prompt_data, prompt_key = self._get_current_prompt()
            if 'system_prompt' in args:
                args['system_prompt'] = prompt_data.get('system_prompt', '')
            if 'user_prompt_template' in args:
                args['user_prompt_template'] = prompt_data.get('user_prompt_template', '')
        
        self.output_text.append(f"\n{'='*60}")
        self.output_text.append(f"Running: {script_name}")
        if args:
            # 显示按顺序的参数
            ordered_args = {k: args[k] for k in param_order}
            self.output_text.append(f"Parameters: {ordered_args}")
        self.output_text.append(f"{'='*60}\n")

        # 清空队列
        while not output_queue.empty():
            try:
                output_queue.get_nowait()
            except queue.Empty:
                break

        # 禁用运行按钮，启用停止按钮，启动队列检查
        self.run_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self._is_running = True
        self.queue_timer.start()

        self.thread = QThread()
        self.runner = ScriptRunner(str(script_path), args)
        self.runner.moveToThread(self.thread)
        
        self.thread.started.connect(self.runner.run)
        self.runner.finished.connect(self.on_script_finished)
        self.runner.error.connect(self.on_script_error)
        self.thread.finished.connect(self.thread.deleteLater)
        
        self.thread.start()

    def stop_script(self):
        """停止正在运行的脚本"""
        if hasattr(self, 'runner') and self.runner:
            self.output_text.append("\n正在停止脚本...")
            self.runner.stop()

    def on_script_finished(self, result):
        """处理脚本完成"""
        self._is_running = False
        self.queue_timer.stop()
        self.run_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        
        # 把队列里剩余的内容都读出来
        try:
            while True:
                line = output_queue.get_nowait()
                self.output_text.append(line)
        except queue.Empty:
            pass
        
        self.output_text.append(f"\n{'='*60}")
        self.output_text.append("Script finished")
        self.output_text.append(f"{'='*60}")
        self.output_text.verticalScrollBar().setValue(
            self.output_text.verticalScrollBar().maximum()
        )

    def on_script_error(self, error_msg):
        """处理脚本错误"""
        self._is_running = False
        self.queue_timer.stop()
        self.output_text.append(f"Error: {error_msg}")
        self.output_text.append(f"\n{'='*60}")
        self.output_text.append("Script failed")
        self.output_text.append(f"{'='*60}")
        self.run_button.setEnabled(True)
        self.stop_button.setEnabled(False)

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
            
            # api_key 参数使用全局 API Key，不需要显示输入框
            if param_name == 'api_key':
                # 记录到 param_widgets，但值为空字符串
                # 运行时会自动被全局 API Key 替换
                self.param_widgets[param_name] = {'input': None}
                continue
            
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
            elif param_type == 'select':
                # 下拉列表选择
                combo = QComboBox()
                combo.setEditable(False)
                options = prompt_info.get('options', {})
                for key, value in options.items():
                    combo.addItem(value, key)  # 显示文本为 value，保存的值为 key
                # 设置默认值
                if default_value and default_value in options:
                    combo.setCurrentText(options[default_value])
                layout.addWidget(combo, row, 0, 1, 2)  # 跨两列
                self.param_widgets[param_name] = {'combo': combo}
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
        
        # 如果没有 output_widget，直接返回
        if output_widget is None:
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