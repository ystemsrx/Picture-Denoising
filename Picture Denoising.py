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
