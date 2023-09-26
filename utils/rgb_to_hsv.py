import cv2
import numpy as np
import os

if __name__ == '__main__':
    path1='/home/lxz/下载/20220514/datasets/lr_u/彩色图/test/down_up_1_680/'
    path2='/home/lxz/下载/20220514（另一个复件）/datasets/lr_u/color/test_new/'
    path3='/home/lxz/下载/20220514（另一个复件）/datasets/lr_u/liangdu/test_new/'

    if not os.path.exists(path2):
        os.makedirs(path2)
    if not os.path.exists(path3):
        os.makedirs(path3)

    train=5290
    test=680

    # path8='/media/wmy/c9792eb3-1646-c646-81c7-34924646579b/wmy/CNNProjects/图像融合/image_fusion20210514/result_test/Model_3model_premium_4block_MSE/result/data_qiepian/finalFusion/'
    # path9='/media/wmy/c9792eb3-1646-c646-81c7-34924646579b/wmy/CNNProjects/图像融合/image_fusion20210514/result_test/Model_3model_premium_4block_MSE/result/data_qiepian/final/'
    for i in range(test):
        # hsi_image = cv2.imread(path2 + str(i + 1) + '.png') #颜色图像
        # fusion = cv2.imread(path3 + str(i + 1) + '.jpg', 0) #网络输出图像
        # hsi_image[:, :, 2] = fusion
        # rgb_img = cv2.cvtColor(hsi_image, cv2.COLOR_HSV2RGB)
        # cv2.imwrite(path5 + str(i + 1) + '.jpg', rgb_img)

        image = cv2.imread(path1 + str(i + 1588) + '.tif')
        hsi_image=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
        # color = hsi_image[:,:,0:2]
        liangdu=hsi_image[:,:,2]
        cv2.imwrite(path2+str(i+1)+'.tif',hsi_image)
        cv2.imwrite(path3 + str(i + 1) + '.tif', liangdu)
        print(i)
