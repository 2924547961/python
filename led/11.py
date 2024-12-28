# -*- coding: utf-8 -*-

import sys
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from fsspec.utils import _translate

from led import Ui_mainWindow
from ultralytics import YOLO

"""
Results 对象具有以下属性

属性	类型	说明
orig_img	numpy.ndarray	原始图像的 numpy 数组。
orig_shape	tuple	原始图像的形状，格式为（高、宽）。
boxes	Boxes, optional	包含检测边界框的方框对象。
masks	Masks, optional	包含检测掩码的掩码对象。
probs	Probs, optional	Probs 对象，包含分类任务中每个类别的概率。
keypoints	Keypoints, optional	关键点对象，包含每个对象的检测关键点。
obb	OBB, optional	包含定向包围盒的 OBB 对象。
speed	dict	每幅图像的预处理、推理和后处理速度字典，单位为毫秒。
names	dict	类名字典。
path	str	图像文件的路径。


Results 对象有以下方法：

方法	返回类型	说明
update()	None	更新结果对象的方框、掩码和 probs 属性。
cpu()	Results	在CPU 内存中返回包含所有张量的 Results 对象副本。
numpy()	Results	返回结果对象的副本，其中所有张量均为 numpy 数组。
cuda()	Results	在GPU 内存中返回包含所有张量的 Results 对象副本。
to()	Results	返回带有指定设备和 dtype 上张量的 Results 对象副本。
new()	Results	返回一个具有相同图像、路径和名称的新结果对象。
plot()	numpy.ndarray	绘制检测结果。返回注释图像的 numpy 数组。
show()	None	在屏幕上显示带注释的结果。
save()	None	将注释结果保存到文件中。
verbose()	str	返回每个任务的日志字符串。
save_txt()	None	将预测结果保存到 txt 文件中。
save_crop()	None	将裁剪后的预测保存到 save_dir/cls/file_name.jpg.
tojson()	str	将对象转换为 JSON 格式。
"""


class MyMainWindow(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)

        # 连接按钮的点击事件到槽函数
        self.push1.clicked.connect(self.load_local_video)
        self.push2.clicked.connect(self.start_camera)
        self.push3.clicked.connect(self.start_recognition)
        self.push6.clicked.connect(self.pause_video)
        self.push4.clicked.connect(self.play_video)

        # 初始化视频捕获对象
        # self.cap = None
        self.cap = cv2.VideoCapture(0)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        # 标志位qi
        self.do_detection = False
        # 初始化模型
        self.model = YOLO('yolov8s.pt')

    def load_local_video(self):
        # 打开文件选择对话框
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, "选择本地视频", "", "Video Files (*.mp4)", options=options)

        if file_name:
            # 初始化视频捕获对象
            self.cap = cv2.VideoCapture(file_name)
            if not self.cap.isOpened():
                print("无法打开视频文件")
                return

            # 启动定时器以更新帧
            self.timer.start(30)  # 30 ms 更新一次

    def update_frame(self):
        self.textEdit.clear()  # 清除文本框内容
        if self.cap and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                # 获取 QGraphicsView 的大小
                view_width = self.graphicsView.width()
                view_height = self.graphicsView.height()

                # 调整图像大小
                frame = cv2.resize(frame, (view_width, view_height))

                # 将图像从 BGR 转换为 RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                if self.do_detection:
                    results = self.model.predict(frame, verbose=False)
                    # 使用YOLOv8的plot方法绘制检测结果，返回的是RGB格式的图像
                    frame = results[0].plot()
                    result = results[0]
                    # 获取识别的边界框信息
                    boxes = result.boxes

                    # 初始化字典来统计每个类别的数量
                    class_counts = {name: 0 for name in result.names.values()}

                    # 遍历所有边界框
                    for box in boxes:
                        # 获取边界框的坐标 (x1, y1, x2, y2)
                        xyxy = tuple(box.xyxy[0].cpu().numpy())  # 转换为 Python 元组
                        # 获取置信度分数
                        confidence = box.conf.item()  # 转换为 Python 的数值类型
                        # 获取类别索引
                        class_idx = box.cls
                        # 获取类别名称
                        class_name = result.names[int(class_idx)]
                        # 更新字典中对应类别的计数
                        class_counts[class_name] += 1
                        # 打印结果
                        print(f"类别: {class_name},  置信度: {confidence}, 坐标: {xyxy}")
                    
                    # 输出类别计数到 textEdit 控件
                    for class_name, count in class_counts.items():
                        self.textEdit.append(f"类别: {class_name}, 数量: {count}")
                    """
                    # 打印每类的数量统计
                    for class_name, count in class_counts.items():
                        print(f"Class: {class_name}, Count: {count}")
                    """
                # 将图像转换为 QImage
                height, width, channel = frame.shape
                bytes_per_line = 3 * width
                q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)

                # 将 QImage 转换为 QPixmap 并显示在 QGraphicsView 中
                pixmap = QPixmap.fromImage(q_img)
                scene = QtWidgets.QGraphicsScene()
                scene.addPixmap(pixmap)
                self.graphicsView.setScene(scene)

                # 输出日志到 textEdit 控件
                self.textEdit.append("Frame updated successfully.")
            else:
                # 如果视频播放完毕，重新开始播放
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                self.textEdit.append("Video ended, restarting from the beginning.")

    def start_camera(self):
    # 打开摄像头
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.textEdit.append("无法打开摄像头")
            return

    # 启动定时器以更新帧
        self.timer.start(30)  # 30 ms 更新一次
        self.textEdit.append("摄像头已启动")

    def start_recognition(self):
        # 实现启动识别的逻辑
        self.do_detection = True
        print("启动识别")

    def pause_video(self):
        if self.timer.isActive():
            self.timer.stop()
            self.textEdit.append("Video paused.")
        else:
            self.textEdit.append("Video is already paused.")

    def play_video(self):
        if not self.timer.isActive():
            self.timer.start(30)  # 30 ms 更新一次
            self.textEdit.append("Video playing.")
        else:
            self.textEdit.append("Video is already playing.")


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
