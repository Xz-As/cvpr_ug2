import os
path = "F:\cvpr\代码\反卷积\datas"
file_list = os.listdir(path)
 
for file in file_list:
    filename = file.zfill(8)
    new_name = ''.join(filename)
    os.rename(path + '\\' + file, path + '\\' + new_name)