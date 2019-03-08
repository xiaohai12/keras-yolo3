"""
Obtain class name of dataset
"""
from os import listdir

mypath = '../datasets/openlogo/ImageSets/class_sep'
class_list = []
for name in listdir(mypath):
    if 'train' in name:
        class_list.append(name[:-10])
class_list.remove('all')
class_list.remove('')
with open('openlogo_class.txt','w') as f:
    for item in class_list:
        f.write("%s\n" % item)

