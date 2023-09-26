import shutil
import os


def remove_file(old_path_pan, new_path_pan,old_path_mul, new_path_mul):
    # print(old_path)
    # print(new_path)
    filelist = os.listdir(old_path_pan)  # 列出该目录下的所有文件,listdir返回的文件列表是不包含路径的。
    print(filelist)
    count=0
    train_size=8430
    test_size=3614
    # for file in filelist:
    for i in range(train_size):
        file=filelist[i]

        src1 = os.path.join(old_path_pan, file)
        dst1 = os.path.join(new_path_pan, file)
        print('src:', src1)
        print('dst:', dst1)
        shutil.move(src1, dst1)

        src2 = os.path.join(old_path_mul, file)
        dst2 = os.path.join(new_path_mul, file)
        print('src:', src2)
        print('dst:', dst2)
        shutil.move(src2, dst2)

        count+=1
    print(count)


if __name__ == '__main__':
    old_path_pan="../datasets/原始数据集/裁剪size252/pan/train (another copy)"
    new_path_pan="../datasets/原始数据集/裁剪size252/pan/train"
    if not os.path.exists(new_path_pan):
        os.makedirs(new_path_pan)

    old_path_mul = "../datasets/原始数据集/裁剪size252/mul/train (another copy)"
    new_path_mul = "../datasets/原始数据集/裁剪size252/mul/train"
    if not os.path.exists(new_path_mul):
        os.makedirs(new_path_mul)

    remove_file(old_path_pan, new_path_pan,old_path_mul,new_path_mul)