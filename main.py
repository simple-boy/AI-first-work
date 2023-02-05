
import os
import random
import shutil

list_classes = os.listdir("flower_dataset")
pwd = os.getcwd()  # 绝对路径
f = open(os.path.join(pwd, "flower_dataset/classes.txt"), "w")

for line in list_classes:
    f.write(line + '\n')
f.close()
class_train = []
class_val = []

j = 0
for line in list_classes:
    line_class = os.listdir(os.path.join("flower_dataset", line))
    random.shuffle(line_class)
    line_class1 = line_class[:int(len(line_class)*0.8)]
    for i in range(len(line_class1)):
        line_class1[i] = line + '\\' + line_class1[i]
        old_name = line_class1[i]
        new_name = 'train\\' + line
        flag = os.path.exists(pwd + '\\flower_dataset\\' + new_name)
        if not flag:
            os.makedirs(pwd + '\\flower_dataset\\' + new_name)
        shutil.copy(pwd + '\\flower_dataset\\' + old_name, pwd + '\\flower_dataset\\' + new_name)
        line_class1[i] = line_class1[i] + " " + str(j)
    line_class2 = line_class[int(len(line_class)*0.8):]
    for i in range(len(line_class2)):
        line_class2[i] = line + '\\' + line_class2[i]
        old_name = line_class2[i]
        new_name = 'val\\' + line
        flag = os.path.exists(pwd + '\\flower_dataset\\' + new_name)
        if not flag:
            os.makedirs(pwd + '\\flower_dataset\\' + new_name)
        shutil.copy(pwd + '\\flower_dataset\\' + old_name, pwd + '\\flower_dataset\\' + new_name)
        line_class2[i] = line_class2[i] + " " + str(j)
    class_train = class_train + line_class1
    class_val = class_val + line_class2
    j = j + 1


f1 = open(os.path.join(pwd, "flower_dataset/train.txt"), "w")
for line in class_train:
    f1.write(line + '\n')
f1.close()

f2 = open(os.path.join(pwd, "flower_dataset/val.txt"), "w")
for line in class_val:
    f2.write(line + '\n')
f2.close()

