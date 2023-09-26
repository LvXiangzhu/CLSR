import datetime
import os

import cv2
import numpy as np
from PIL import Image
import torch
import torchvision

now = datetime.datetime.now()
fur_img_path = '/home/lxz/下载/20220514（另一个复件）/results/brightness/student/2022-07-04 13:06:20.140724/l_output'
# fur_img_path = '/home/lxz/下载/20220514（另一个复件）/datasets/lr_u/brightness/test'
visimage_path = '/home/lxz/下载/20220514/datasets/lr_u/color/test/down_up_1'
# print(len('/home/lxz/下载/20220514/datasets/lr_u/color/test/down_up_1'))
output_img_path = '/home/lxz/下载/20220514（另一个复件）/output_rgb_img_{}/'.format(now)
if not os.path.exists(output_img_path):
    os.makedirs(output_img_path)
fur_img = os.listdir(fur_img_path)
visimage = os.listdir(visimage_path)
fur_img = [os.path.join(fur_img_path, x) for x in os.listdir(fur_img_path)]
visimage = [os.path.join(visimage_path, x) for x in os.listdir(visimage_path)]
fur_img.sort(key=lambda x: int(x[92:-4]))
# fur_img.sort(key=lambda x: int(x[59:-4]))
visimage.sort(key=lambda x: int(x[57:-4]))

for i in range(len(fur_img)):
    fur_img1 = cv2.imread(fur_img[i])

    visimage1 = cv2.imread(visimage[i])
    visimage1 = visimage1[:, :, 0:2]

    fur_img1 = fur_img1[:, :, 0]
    fur_img1 = np.expand_dims(fur_img1, axis=2)
    hsv = cv2.merge([visimage1, fur_img1])
    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
    cv2.imwrite(output_img_path+str(i+1)+'.tif', rgb)
    print(i+1)