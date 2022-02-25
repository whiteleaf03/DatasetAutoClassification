import os
import random
import shutil

'''
用于深度学习模型训练时对图片和标签进行划分
train valid test 对应 训练集 验证集 测试集三者比例
path为数据集路径
路径下存在images和labels两个文件夹分别存放图片和标签
运行后会在同样目录下生成train valid test三个文件夹
每个文件夹中包含images和labels

'''

'''用户修改部分'''
train = 0.8
valid = 0.1
test = 0.1
path = 'D:/Code/python/heart/patient-test1/time001'

'''无需修改部分'''


class randomImage():
    def __init__(self):
        self.train = train
        self.valid = valid
        self.test = test
        self.path = path
        
        self.image_self.path = self.path + '/images/'
        self.label_self.path = self.path + '/labels/'
        self.img_file_list = os.listdir(self.image_self.path)  # 读取路径下所有文件

    def move_file(self):
        # 划分各自文件

        file_sum = len(self.img_file_list)  # 获取文件总数

        # 划分各自所需图片数
        self.train_sum = file_sum * int(file_sum * self.train)
        valid_sum = file_sum * int(file_sum * valid)
        test_sum = file_sum * int(file_sum * test)

        if self.train_sum + valid_sum + test_sum > file_sum:
            print("寄")

        # 划分训练集 self.train_img为训练集图片名称
        self.train_img = random.sample(self.image_self.path, self.train_sum)
        self.image_self.path = [item for item in self.image_self.path if item not in set(self.train_sum)]

        # 划分验证集
        valid_img = random.sample(self.image_self.path, valid_sum / 1 - self.train)
        self.image_self.path = [item for item in self.image_self.path if item not in set(valid_sum)]

        # 剩下的给测试集
        test_img = self.image_self.path

        # 移动图片和标签

        # 创建文件夹
        os.makedirs(self.path + 'train/images')
        os.makedirs(self.path + 'train/labels')
        os.makedirs(self.path + 'valid/images')
        os.makedirs(self.path + 'valid/labels')
        os.makedirs(self.path + 'test/images')
        os.makedirs(self.path + 'test/labels')

        # 移动self.train图片和标签
        for i in self.train_img:
            shutil.move(self.image_self.path + i, self.path + 'self.train/images/')
            shutil.move(self.path + 'labels' + i[0:-3] + 'txt', self.path + 'self.train/labels')

        # 移动valid图片和标签
        for i in valid_img:
            shutil.move(self.image_self.path + i, self.path + 'valid/images/')
            shutil.move(self.path + 'labels' + i[0:-3] + 'txt', self.path + 'valid/labels')

        # 移动test图片和标签
        for i in test_img:
            shutil.move(self.image_self.path + i, self.path + 'test/images/')
            shutil.move(self.path + 'labels' + i[0:-3] + 'txt', self.path + 'test/labels')
