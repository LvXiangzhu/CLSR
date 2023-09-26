import datetime
import os

import cv2
import numpy as np
from PIL import Image
import torch
import torchvision


def bri2rgb(fus_img, visimage_clr):
    """
    fur_img:[GPU tensor] brightness image
    visimage_clr:[GPU tensor] color
    return: [cpu tensor] colorful image

    """
    bri_ori = fus_img.cpu().numpy().transpose(0, 2, 3, 1) * 255
    visimage_clr = visimage_clr.cpu().numpy().transpose(0, 2, 3, 1) * 255
    imgs = []
    for i in range(bri_ori.shape[0]):
        bri = bri_ori[i, :, :, :].squeeze()
        bri = bri[:,:,0]
        bri = np.where(bri < 0, 0, bri)
        bri = np.where(bri > 255, 255, bri)
        im1 = Image.fromarray(bri.astype(np.uint8))
        bri = np.expand_dims(bri, axis=2)

        clr = visimage_clr[i, :, :, :].squeeze()
        clr = np.concatenate((clr, bri), axis=2)

        clr[:, :, 2] = im1
        clr = cv2.cvtColor(clr.astype(np.uint8), cv2.COLOR_HSV2RGB)

        # cv2.imshow('a', clr)
        # cv2.waitKey()
        # cv2.destroyAllWindows()
        #
        clr = clr.transpose((2, 0, 1))[::-1]
        imgs.append(clr)
    imgs = np.ascontiguousarray(np.array(imgs))
    return torch.from_numpy(imgs)

def save_image_tensor2pillow(input_tensor: torch.Tensor, filename):
    """
    将tensor保存为pillow
    :param input_tensor: 要保存的tensor
    :param filename: 保存的文件名
    """
    assert (len(input_tensor.shape) == 4 and input_tensor.shape[0] == 1)
    # 复制一份
    input_tensor = input_tensor.clone().detach()
    # 到cpu
    input_tensor = input_tensor.to(torch.device('cpu'))
    # 反归一化
    # input_tensor = unnormalize(input_tensor)
    # 去掉批次维度
    input_tensor = input_tensor.squeeze()
    # 从[0,1]转化为[0,255]，再从CHW转为HWC，最后转为numpy
    # input_tensor = input_tensor.mul_(255).add_(0.5).clamp_(0, 255).permute(1, 2, 0).type(torch.uint8).numpy()
    input_tensor = input_tensor.clamp_(0, 255).type(torch.uint8).numpy()
    # 转成pillow
    input_tensor = input_tensor.transpose(1, 2, 0)

    im = Image.fromarray(input_tensor)
    im.save(filename)

if __name__ == '__main__':
    now = datetime.datetime.now()
    # fur_img_path = '/home/lxz/下载/20220514（另一个复件）/results/brightness/student/2022-07-03 10:45:26.992717/l_output'
    # visimage_path = '/home/lxz/下载/20220514（另一个复件）/datasets/lr_u/color/test'
    fur_img_path = '/home/lxz/下载/20220514（另一个复件）/datasets/lr_u/liangdu/test_new'
    visimage_path = '/home/lxz/下载/20220514（另一个复件）/datasets/lr_u/color/test_new'
    print(len('/home/lxz/下载/20220514（另一个复件）/datasets/lr_u/color/test_new'))
    output_img_path = '/home/lxz/下载/20220514（另一个复件）/output_rgb_img_{}/'.format(now)
    if not os.path.exists(output_img_path):
        os.makedirs(output_img_path)
    fur_img = os.listdir(fur_img_path)
    visimage = os.listdir(visimage_path)
    fur_img = [os.path.join(fur_img_path, x) for x in os.listdir(fur_img_path)]
    visimage = [os.path.join(visimage_path, x) for x in os.listdir(visimage_path)]
    # fur_img.sort(key=lambda x: int(x[92:-4]))
    # visimage.sort(key=lambda x: int(x[54:-4]))
    fur_img.sort(key=lambda x: int(x[60:-4]))
    visimage.sort(key=lambda x: int(x[58:-4]))
    print(len(fur_img))
    trans = torchvision.transforms.ToTensor()
    for i in range(len(fur_img)):
       fur_img1 = cv2.imread(fur_img[i])
       fur_img1_tensor = trans(fur_img1)
       fur_img1_tensor = torch.unsqueeze(fur_img1_tensor, 0)

       visimage1 = cv2.imread(visimage[i])
       visimage1_numpy = visimage1[:, :, 0:2]
       visimage1_numpy = visimage1_numpy.transpose(2, 0, 1)
       visimage1_tensor = torch.tensor(visimage1_numpy)

       visimage1_tensor = torch.unsqueeze(visimage1_tensor, 0)

       img = bri2rgb(fur_img1_tensor, visimage1_tensor)
       save_image_tensor2pillow(img, output_img_path + str(i + 1) + '.tif')

