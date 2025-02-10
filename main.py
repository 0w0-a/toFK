import tkinter as tk
import os

BOOKMARK_FILE = 'bookmark.txt'

def update_transparency(value):
    # 将拖动条的值转换为透明度（0.0 到 1.0）
    alpha = float(value) / 100
    root.attributes('-alpha', alpha)

def read_text_from_file(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='GBK') as file:
        return file.read()

def on_mouse_wheel(event):
    # 处理鼠标滚轮事件
    if event.delta > 0:
        # 向上滚动
        text_widget.yview_scroll(-1, "units")
    else:
        # 向下滚动
        text_widget.yview_scroll(1, "units")

def save_bookmark():
    # 保存当前的阅读位置
    current_position = text_widget.index(tk.INSERT)
    with open(BOOKMARK_FILE, 'w') as file:
        file.write(current_position)

def load_bookmark():
    # 加载上次的阅读位置
    if os.path.exists(BOOKMARK_FILE):
        with open(BOOKMARK_FILE, 'r') as file:
            position = file.read()
        text_widget.mark_set(tk.INSERT, position)
        text_widget.see(tk.INSERT)

# 创建主窗口
root = tk.Tk()
root.title(" ")

# 设置窗口大小
root.geometry("500x390")

# 读取当前文件夹下的 txt 文件内容
file_path = os.path.join(os.getcwd(), 'text.txt')
if os.path.exists(file_path):
    text_content = read_text_from_file(file_path)
else:
    text_content = "文件 text.txt 不存在"

# 创建一个 Text 组件用于显示文本
text_widget = tk.Text(root, wrap='word', height=20, width=70)
text_widget.insert(tk.END, text_content)
text_widget.pack(padx=10, pady=10)

# 绑定鼠标滚轮事件
text_widget.bind("<MouseWheel>", on_mouse_wheel)
text_widget.bind("<Button-4>", on_mouse_wheel)  # Linux 滚轮向上
text_widget.bind("<Button-5>", on_mouse_wheel)  # Linux 滚轮向下

# 创建一个拖动条
scale = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=update_transparency)
scale.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# 创建一个按钮用于保存书签
save_button = tk.Button(root, text="书签", command=save_bookmark)
save_button.pack(side=tk.LEFT, padx=10, pady=10)

# 加载上次的阅读位置
load_bookmark()

# 初始透明度设置为 100% 不透明
root.attributes('-alpha', 1.0)

# 运行主循环
root.mainloop()
