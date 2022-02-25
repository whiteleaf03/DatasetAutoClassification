import os
import xml.etree.ElementTree as ET
import glob

# 类别 对应0-n 注意此处应与标注时的名称保持一致
classes = ['心脏']
# xml目录
xml_path = 'D:\\Code\\python\\heart\\patient-test1\\time001\\outputs\\'
# txt目录
txt_path = 'D:\\Code\\python\\heart\\patient-test1\\time001\\outputs\\'


class xml2txt():
    def __init__(self):
        self.classes = classes
        self.xml_path = xml_path
        self.txt_path = txt_path

    def to_txt(self):
        os.chdir(self.xml_path)
        annotations = os.listdir('.')
        annotations = glob.glob(str(annotations) + '*.xml')
        print(annotations)
        for i, file in enumerate(annotations):

            file_save = file.split('.')[0] + '.txt'
            # file_txt=os.path.join(self.txt_path,file_save)
            file_txt = self.txt_path + "\\" + file_save
            # print(file_save)
            f_w = open(file_txt, 'w', encoding='utf-8')

            # actual parsing
            in_file = open(file, encoding='utf-8')
            tree = ET.parse(in_file)
            root = tree.getroot()
            # filename = root.find('filename').text  # 这里是xml的根，获取filename那一栏
            for obj in root.iter('object'):
                # current = list()
                name = obj.find('name').text  # 这里获取多个框的名字，底下是获取每个框的位置
                name = self.classes.index(name)
                xmlbox = obj.find('bndbox')
                xn = xmlbox.find('xmin').text
                xx = xmlbox.find('xmax').text
                yn = xmlbox.find('ymin').text
                yx = xmlbox.find('ymax').text
                f_w.write(f'{name} {xn} {yn} {xx} {yx}\n')


if __name__ == '__main__':
    change = xml2txt()
    change.xml_path = xml_path
    change.txt_path = txt_path
    change.to_txt()
