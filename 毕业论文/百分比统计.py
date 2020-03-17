import numpy as np
import paddle.dataset as dataset
import cv2
from PIL import Image
print('植被（标记1）、建筑（标记2）、水体（标记3）、道路（标记4）以及其他(标记0)')
path = '_class.png'
a = {}
for i in range(5,6):

    path1 = str(i) + path
    label = cv2.imread(path1)[:,:,1]

    for i in label:

        for k in i:
            if k not in a:
                a[k] = 1
            else:
                a[k] = a[k] +1

    # label1 = dataset.image.load_image(path, is_color=False).astype("float32") +1
    print(label.shape)
print(a)
#1: 1499827, 0: 10449501, 2: 2040997, 3: 6516046, 4: 25041
# 3: 56383052, 4: 10024585, 1: 42993819, 0: 61367410, 2: 15325786
# a = [56383052,1002458,42993819,61367410,15325786]
# for i in a:
#     print(i/sum(a))
#




