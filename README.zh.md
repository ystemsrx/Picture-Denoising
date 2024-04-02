[English](README.md)
# 图片去噪

## 概述
这个Python脚本“Picture Denoising.py”旨在去除当前目录中的图像噪声。它利用OpenCV库高效地减少PNG、JPG、JPEG、TIFF、BMP和GIF等多种图像格式的噪声。

## 特点
- **支持多种图像格式：** 可处理PNG、JPG、JPEG、TIFF、BMP和GIF图像。
- **批量处理：** 自动去噪当前目录中所有支持的图像格式。
- **图像去噪：** 使用OpenCV的fastNlMeansDenoisingColored函数进行有效的噪声降低。

## 系统要求
- Python 3
- OpenCV Python库 (`cv2`)

## 安装
1. 确保您的系统上安装了Python 3。
2. 安装OpenCV库：`pip install opencv-python`。

## 使用方法
1. 将脚本放在包含图像的目录中。
2. 使用Python运行脚本：`python Picture Denoising.py`。
3. 脚本将处理每张图像，去除噪声，并将去噪后的图像以`denoised_`前缀保存在同一目录中。

```txt
# 脚本中选取的代码片段
import os
import cv2

# 获取当前工作目录
cwd = os.getcwd()

# 遍历目录下的所有文件
for filename in os.listdir(cwd):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        # 读取图片
        image = cv2.imread(filename)
        # 对彩色图片进行去噪
        dst = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)
        # 构建去噪后的图片文件名
        denoised_filename = f"denoised_{filename}"
        # 保存去噪后的图片
        cv2.imwrite(denoised_filename, dst)
        print(f"Processed and saved: {denoised_filename}")
```
