import os
path_pan = "../datasets/原始数据集/裁剪size252/pan/test/"
path_mul="../datasets/原始数据集/裁剪size252/mul/test/"
# 获取该目录下所有文件，存入列表中
f = os.listdir(path_pan)
print(len(f))
print(f[0])

n = 0
i = 0
for i in f:
    # 设置旧文件名（就是路径+文件名）
    oldname = f[n]

    # 设置新文件名
    newname = str(n+1) + '.tif'
    # 用os模块中的rename方法对文件改名
    os.rename(path_pan+oldname, path_pan+newname)
    os.rename(path_mul+oldname, path_mul+newname)
    print(oldname, '======>', newname)

    n += 1
