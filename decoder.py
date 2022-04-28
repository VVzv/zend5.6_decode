# !/usr/bin/python
# -*- coding:utf-8 -*-
# __Author__: VVzv
import os
import shutil


decode_php_file_path1 = "index.php"
decode_php_file_path2 = "index2.php"

def dirExist(des_file):
    file_dir = "".join([i+"/" for i in des_file.split("/")[:-1]]) 
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

def fileFilter(src_file_dir, des_file_dir):
    src_file_list = []
    for root, dirs, files in os.walk(src_file_dir):
        for file in files:
            filename = os.path.join(root, file)
            if os.path.splitext(file)[1] == '.php':
                src_file_list.append(filename)
            else:
                des_filename = filename.replace(src_file_dir, des_file_dir)
                dirExist(des_filename)
                shutil.copy(filename, des_filename)
    return src_file_list

def decoder(filename):
    # <?php @Zend;
    cmd1 = "php {} {}".format(decode_php_file_path1, filename)
    cmd2 = "php {} {}".format(decode_php_file_path2, filename)
    print("\033[36m[*] 正在进行解密：{}".format(filename))
    save_name = filename.replace("source", "destination")
    info = os.popen(cmd1).read()
    if "<?php @Zend;" not in info and "file not foud!" not in info:
        dirExist(save_name)
        with open(save_name, "w") as f:
            f.write(info)
    else:
        info = os.popen(cmd2).read()
        if "<?php @Zend;" not in info and "file not foud!" not in info:
            dirExist(save_name)
            with open(save_name, "w") as f:
                f.write(info)
        else:
            shutil.copy(filename, save_name)
            print("\033[35m[-] 解密失败[{}]\033[0m".format(filename))


if __name__ == '__main__':

    f_list = fileFilter("source", "destination")
    for f in f_list:
        decoder(f)

