"""
Obtain standard annotation file through xml files
"""
import xml.etree.ElementTree as ET
from os import listdir

f = open('../datasets/openlogo/openlogo_class.txt','r')

classes = f.read().split('\n')[:-1]

def convert_annotation(annotation_path,list_file):
    in_file = open(annotation_path)
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))
        print('finished to write'+annotation_path)

img_dir = '../datasets/openlogo/JPEGImages/'
annotation_dir = '../datasets/openlogo/Annotations/'
list_file = open('train.txt','w')
for name in listdir(annotation_dir):
    img_path = img_dir + name
    list_file.write(img_path)
    annotation_path = annotation_dir + name
    convert_annotation(annotation_path,list_file)
    list_file.write('\n')
list_file.close()


