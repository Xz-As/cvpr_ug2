import json
import os
import numpy as np
import shutil

file_path='./data/test/'
op='./data/images/'
for i in np.arange(6000):
    a=file_path+'%d'%(i+1)+'_kindle.png'
    b =op+'%d'%(i+1)+'.png'
    shutil.copyfile(a, b)