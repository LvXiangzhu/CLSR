from skimage import io
import os
import cv2

def resize_img(data_dir, out_dir, num_images,factor):
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    print('resize begining…………')
    for z in range(num_images):
        # img = io.imread(data_dir + str(1) + '.tif',0)

        # out = img.resize((size1, size2))
        # io.imsave(out_dir, out)

        img = cv2.imread(data_dir + str(z + 1) + '.tif')
        print(img.shape)
        height = img.shape[0]
        width = img.shape[1]
        channel = img.shape[2]

        size = (int(width * factor), int(height * factor))
        shrink = cv2.resize(img, size, interpolation=cv2.INTER_AREA)

        cv2.imwrite(out_dir+str(z+1)+'.tif', shrink)
        print(shrink.shape)
        print("finish:第"+str(z+1)+"张")

if __name__ == '__main__':
    data_dir = '../datasets/pan/'
    out_dir = '../datasets/pan_resize/'
    num_images=9
    factor=0.25

    resize_img(data_dir, out_dir, num_images, factor)
