from PIL import Image
import os

def convert_bmp_to_png(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".bmp"):
            # 构建输入文件的完整路径
            input_path = os.path.join(folder_path, filename)

            # 构建输出文件的完整路径
            output_path = os.path.join(folder_path, os.path.splitext(filename)[0] + ".png")

            # 打开BMP图像并保存为PNG格式
            with Image.open(input_path) as image:
                image.save(output_path, "PNG")

            print(f"转换成功: {filename} -> {os.path.basename(output_path)}")

# 调用函数并传入要转换的文件夹路径
convert_bmp_to_png("./fig")