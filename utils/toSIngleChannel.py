from skimage import io
import os
import cv2

def toSingleChannel(data_dir, out_dir, num_images):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    for z in range(num_images):
        img = cv2.imread(data_dir + str(z + 1) + '.tif',0)
        cv2.imwrite(out_dir+str(z+1)+'.tif', img)
        print("finish:第"+str(z+1)+"张")

if __name__ == '__main__':
    data_dir = '../datasets/lr_u/test/down_up_3/'
    out_dir = '../datasets/lr_u/liangdu/test/down_up_3/'
    # num_images=5290
    num_images=2267

    toSingleChannel(data_dir, out_dir, num_images)
