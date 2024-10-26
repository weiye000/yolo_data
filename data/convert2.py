import os
import random
import shutil

# 设置路径
base_path = '.'  # 替换为您的数据集路径
images_path = os.path.join(base_path, 'images')
labels_path = os.path.join(base_path, 'labels')

# 创建train、val、test子文件夹
for folder in ['train', 'val', 'test']:
    os.makedirs(os.path.join(images_path, folder), exist_ok=True)
    os.makedirs(os.path.join(labels_path, folder), exist_ok=True)

# 获取所有图片文件
image_files = [f for f in os.listdir(images_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
random.shuffle(image_files)

# 划分比例
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# 计算各组数量
total_images = len(image_files)
train_count = int(total_images * train_ratio)
val_count = int(total_images * val_ratio)
test_count = total_images - train_count - val_count

# 划分图片
train_files = image_files[:train_count]
val_files = image_files[train_count:train_count + val_count]
test_files = image_files[train_count + val_count:]

# 定义函数用于移动文件
def move_files(file_list, subset):
    for file_name in file_list:
        # 生成标签文件名称
        label_name = file_name.replace('.jpg', '.txt').replace('.png', '.txt').replace('.jpeg', '.txt')
        
        # 检查标签文件是否存在
        if os.path.exists(os.path.join(labels_path, label_name)):
            # 移动图片文件
            shutil.move(os.path.join(images_path, file_name), os.path.join(images_path, subset, file_name))
            
            # 移动对应标签文件
            shutil.move(os.path.join(labels_path, label_name), os.path.join(labels_path, subset, label_name))
        else:
            print(f"未找到 {file_name} 的标签文件，跳过此文件。")

# 将文件移动到对应文件夹
move_files(train_files, 'train')
move_files(val_files, 'val')
move_files(test_files, 'test')

# 清理剩余文件
for file in os.listdir(images_path):
    file_path = os.path.join(images_path, file)
    if os.path.isfile(file_path):
        os.remove(file_path)

for file in os.listdir(labels_path):
    file_path = os.path.join(labels_path, file)
    if os.path.isfile(file_path):
        os.remove(file_path)

print("数据集划分并清理完成！")
