from randomImage import randomImage
from xml2txt import xml2txt

'''
用于深度学习模型训练时对图片和标签进行划分
path路径下存在images和labels两个文件夹分别存放图片和标签
运行后会在同样目录下生成train valid test三个文件夹
每个文件夹中包含images和labels

'''

'''用户修改部分'''

# train valid test 对应 训练集 验证集 测试集三者比例
train = 0.8
valid = 0.1
test = 0.1
# path为数据集路径
path = 'D:\\Code\\python\\heart\\patient-test1\\time001\\test\\'

# 用于xml2txt类
# 类别 对应0-n 注意此处应与标注时的名称保持一致
classes = ['心脏']
# xml目录
xml_path = 'D:\\Code\\python\\heart\\patient-test1\\time001\\outputs\\'
# txt目录
txt_path = 'D:\\Code\\python\\heart\\patient-test1\\time001\\outputs\\'

'''用户修改部分'''

'''程序执行部分 不可修改'''

if __name__ == '__main__':
    # 转化格式
    change = xml2txt()
    change.classes = classes
    change.xml_path = xml_path
    change.txt_path = txt_path
    change.to_txt()

    # 对图片和标签划分
    segmentation = randomImage()
    segmentation.train = train
    segmentation.valid = valid
    segmentation.test = test
    segmentation.path = path
    segmentation.move_file()

    print('Successful!')

'''程序执行部分 不可修改'''
