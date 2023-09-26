from skimage import io
import os
import cv2

def down_up_sample_img(data_dir, out_dir, start_image,end_image, factor):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    print('down sample begining…………')
    for z in range(start_image,end_image+1):
        img = cv2.imread(data_dir + str(z) + '.tif')
        print(img.shape)
        out = img
        for i in range(factor):
            out = cv2.pyrDown(out)
            out = cv2.pyrUp(out)
        print(out.shape)
        cv2.imwrite(out_dir+str(z)+'.tif', out)
        print("finish:第" + str(z) + "张")

if __name__ == '__main__':
    data_dir = '/media/wmy/c9792eb3-1646-c646-81c7-34924646579b/wmy/CNNProjects/图像融合/20220514/datasets/原始数据集/裁剪size252/mul/train/'
    out_dir = '/media/wmy/c9792eb3-1646-c646-81c7-34924646579b/wmy/CNNProjects/图像融合/20220514/datasets/原始数据集/裁剪size252/lr_u/train/'
    #图片索引，开始和结束
    start_image=16861
    end_image=25290
    #变换次数
    factor=3 #1,2,3

    down_up_sample_img(data_dir, out_dir, start_image,end_image, factor)
