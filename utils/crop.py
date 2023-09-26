from skimage import io
import os
import math
import cv2


def cutpan_overlap(pan_dir, mul_dir,pan_output_dir,mul_output_dir, num_images, cutshape, overlap_factor):
    if not os.path.exists(pan_output_dir):
        os.makedirs(pan_output_dir)
    if not os.path.exists(mul_output_dir):
        os.makedirs(mul_output_dir)
    print('Cut begining…………')
    img_index=9
    for z in range(num_images):
        pan = cv2.imread(pan_dir + str(img_index) + '.tif')
        mul = cv2.imread(mul_dir + str(img_index) + '.tif')
        print(pan.shape[0])
        print(mul.shape)
        factor1 = int(math.ceil(pan.shape[0] / overlap_factor))
        factor2 = int(math.ceil(pan.shape[1] / overlap_factor))
        count=0
        for i in range(factor2):
            for ii in range(factor1):
                start_x = ii * cutshape - ii * overlap_factor
                end_x = (ii + 1) * (cutshape) - ii * overlap_factor
                start_y = i * cutshape - i * overlap_factor
                end_y = (i + 1) * cutshape - i * overlap_factor
                if end_x > pan.shape[0]:
                    start_x = pan.shape[0] - cutshape
                    end_x = pan.shape[0]
                if end_y > pan.shape[1]:
                    start_y = pan.shape[1] - cutshape
                    end_y = pan.shape[1]
                pan_temp = pan[start_x+2:end_x+2, start_y:end_y, :]
                mul_temp = mul[start_x:end_x, start_y+1:end_y+1, :]
                count+=1

                cv2.imwrite(pan_output_dir+str(img_index)+"_"+str(count)+'.tif', pan_temp)
                cv2.imwrite(mul_output_dir+str(img_index)+"_"+str(count)+'.tif', mul_temp)
                if end_x == pan.shape[0] and end_y == pan.shape[1]:
                    break
                print(count)
        print("finish:第" + str(img_index) + "张")


if __name__ == '__main__':
    ##### cut
    pan_dir = '../datasets/原始数据集/pan_resize/'
    mul_dir = '../datasets/原始数据集/mul/'
    pan_output_dir = '../datasets/原始数据集/裁剪size252/pan/'
    mul_output_dir = '../datasets/原始数据集/裁剪size252/mul/'
    num_images=1
    cutshape = 252
    overlap_factor = 126

    cutpan_overlap(pan_dir, mul_dir,pan_output_dir,mul_output_dir, num_images, cutshape, overlap_factor)
