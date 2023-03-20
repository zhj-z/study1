#!/usr/bin/python
#coding:utf-8

import os

path_imgs = 'D:\HOG_SVM-master\HOG_SVM-master\image129'
img_names = os.listdir(path_imgs)
img_names.sort(key=lambda x:int(x.split('.')[0]))
#for files in os.listdir(path_imgs):
for files in img_names:
    print(files)
   # img_path = path_imgs+ files
    img_path =  files

    with open("D:\HOG_SVM-master\HOG_SVM-master\image129\ground.txt", "a") as f:
        f.write(str(img_path) + ' 2' + '\n')

