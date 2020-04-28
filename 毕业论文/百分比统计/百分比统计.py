import numpy as np
import paddle.dataset as dataset
#
# color[img == 0] = [255, 255, 255]  # 其他，白色，0  765
# color[img == 1] = [0, 255, 0]  # 植被，绿色，1    255
# color[img == 2] = [0, 0, 0]  # 道路，黑色，2    0
# color[img == 3] = [131, 139, 139]  # 建筑，黄色，3   409
# color[img == 4] = [139, 69, 19]  # 水体，蓝色，4    227

import cv2


print('植被（标记1）、道路（标记2）、建筑（标记3）、水体（标记4）以及其他(标记0)')
path = '50000.png'
#{255: 277834白色, 植被：945191，道路：217109, 131: 359915建筑, 139: 305897水体}
out = {}
# label = cv2.imread(path)[:, :, 0]
# print(label.shape)
image = cv2.imread(path)
sh = image.shape
for i in range(sh[0]):
    for j in range(sh[1]):
        a = []
        for k in range(3):
            label = image[i,j,k]
            a.append(label)
        # print(a)
        ss = sum(a)
        if ss not in out:
            out[ss] = 1
        else:
            out[ss] = out[ss] + 1
print(out)
leng = []
for k,v in out.items():
    leng.append(v)
print(leng)
for i in range(len(leng)):
    print(i,leng[i]/sum(leng))
# cv2.imwrite("out.png",image)




# for i in range(5,6):
#
#     # path1 = str(i) + path
#     # print(path1)
#     label = cv2.imread(path)[:,:,1]
#     print(label.shape)
#     for i in label:
#
#         for k in i:
#             if k not in a:
#                 a[k] = 1
#             else:
#                 a[k] = a[k] +1
#
#     # label1 = dataset.image.load_image(path, is_color=False).astype("float32") +1
#     print(label.shape)
# print(a)
# #1: 1499827, 0: 10449501, 2: 2040997, 3: 6516046, 4: 25041
# # 3: 56383052, 4: 10024585, 1: 42993819, 0: 61367410, 2: 15325786
# a = [277834,945191,217109,359915,305897]
# for i in a:
#     print(i/sum(a))
# #




