import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 初始化 Tkinter 窗口
root = tk.Tk()
root.title("UAV Path Planning")

# 定义绘图函数
def initialize_plot():
    # 清空之前的绘图
    ax.clear()

    # 设置坐标轴范围和刻度
    ax.set_xlim([-1500, 4000])
    ax.set_ylim([-1500, 1500])
    ax.set_xticks(range(-1500, 4001, 500))
    ax.set_yticks(range(-1500, 1501, 500))

    # 设置坐标轴的比例，使圆形看起来是正圆
    ax.set_aspect('equal', adjustable='box')

    # 绘制坐标轴
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)

    # 绘制障碍圆
    circle_center = (0, 0)  # 圆心坐标
    circle_radius = 500  # 圆的半径
    circle = plt.Circle(circle_center, circle_radius, color='r', fill=False, linestyle='--')
    ax.add_artist(circle)

    # 绘制 A 点和 B 点
    A_start = [-1000, 0]
    B_start = [3500, 0]
    ax.plot(A_start[0], A_start[1], 'bo', label='A Start')
    ax.plot(B_start[0], B_start[1], 'go', label='B Start')

    # 标记 A 点和 B 点
    ax.text(A_start[0], A_start[1], 'A Start', fontsize=12, ha='right')
    ax.text(B_start[0], B_start[1], 'B Start', fontsize=12, ha='left')

    # 设置图例和标题
    ax.legend()
    ax.set_title('Initial Coordinate System')

    # 更新画布
    canvas.draw()

# 初始化按钮
initialize_button = tk.Button(root, text="Initialize", command=initialize_plot)
initialize_button.pack()

# 创建绘图区域
fig, ax = plt.subplots(figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

# 运行 Tkinter 主循环
root.mainloop()
