import sys
import cv2
import os
from PIL import Image
from PIL import ImageDraw

os.getcwd()
lr_u_path = '/home/lxz/下载/20220514/datasets/lr_u/brightness/test/down_up_1_1587'
mul_path = '/home/lxz/下载/20220514/datasets/mul/brightness/test_1587'
pan_path = '/home/lxz/下载/20220514/datasets/pan/brightness/test_1587'
lr_u_dir = [os.path.join(lr_u_path, x) for x in os.listdir(lr_u_path)]
mul_dir = [os.path.join(mul_path, x) for x in os.listdir(mul_path)]
pan_dir = [os.path.join(pan_path, x) for x in os.listdir(pan_path)]
print(len('/home/lxz/下载/20220514/datasets/lr_u/brightness/test/down_up_1_1587'))
lr_u_dir.sort(key=lambda x: int(x[67:-4]))
mul_dir.sort(key=lambda x: int(x[56:-4]))
pan_dir.sort(key=lambda x: int(x[56:-4]))

for i, lr_u in enumerate(lr_u_dir) :
    img = Image.open(lr_u)
    # ====================================================
    out1 = img.transpose(Image.FLIP_LEFT_RIGHT) # 水平翻转
    out2 = img.transpose(Image.FLIP_TOP_BOTTOM)

    name_x = 1588 + i
    path_x = '/home/lxz/下载/20220514/datasets/lr_u/brightness/test/down_up_1_1587_kuo_x/' + str(name_x) + '.tif'
    out1.save(path_x)
    name_y = 1588*2-1 + i
    path_y = '/home/lxz/下载/20220514/datasets/lr_u/brightness/test/down_up_1_1587_kuo_y/' + str(name_y) + '.tif'
    out2.save(path_y)
for j, mul in enumerate(mul_dir):
    img = Image.open(mul)
    # ====================================================
    out1 = img.transpose(Image.FLIP_LEFT_RIGHT)  # 水平翻转
    out2 = img.transpose(Image.FLIP_TOP_BOTTOM)

    name_x = 1588 + j
    path_x = '/home/lxz/下载/20220514/datasets/mul/brightness/test_1587_x/' + str(name_x) + '.tif'
    out1.save(path_x)
    name_y = 1588 * 2 - 1 + j
    path_y = '/home/lxz/下载/20220514/datasets/mul/brightness/test_1587_y/' + str(name_y) + '.tif'
    out2.save(path_y)
for k, pan in enumerate(pan_dir):
    img = Image.open(pan)
    # ====================================================
    out1 = img.transpose(Image.FLIP_LEFT_RIGHT)  # 水平翻转
    out2 = img.transpose(Image.FLIP_TOP_BOTTOM)

    name_x = 1588 + k
    path_x = '/home/lxz/下载/20220514/datasets/pan/brightness/test_1587_x/' + str(name_x) + '.tif'
    out1.save(path_x)
    name_y = 1588 * 2 - 1 + k
    path_y = '/home/lxz/下载/20220514/datasets/pan/brightness/test_1587_y/' + str(name_y) + '.tif'
    out2.save(path_y)
