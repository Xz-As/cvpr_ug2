import json

json_file = 'F:\\cvpr\\dataset\\annotaions\\train.json' #root
txt_file = '' #root
f = open(json_file)
datas = json.load(f)
#datas:dict = {'images', 'annotations', 'categories'}
#放大图片
l_img = datas['images']
for i in range(len(l_img)):
    l_img[i]['height'] *= 2
    l_img[i]['width'] *= 2
    print(l_img[i])
#放大标注
l_ann = datas['annotations']
print(l_ann[1])
for i in range(len(l_ann)):
    l_ann[i]['bbox'][0] *= 2
    l_ann[i]['bbox'][1] *= 2
    l_ann[i]['bbox'][2] *= 2
    l_ann[i]['bbox'][3] *= 2
    l_ann[i]['segmentation'][0][0] *= 2
    l_ann[i]['segmentation'][0][1] *= 2
    l_ann[i]['segmentation'][0][2] *= 2
    l_ann[i]['segmentation'][0][3] *= 2
    l_ann[i]['segmentation'][0][4] *= 2
    l_ann[i]['segmentation'][0][5] *= 2
    l_ann[i]['segmentation'][0][6] *= 2
    l_ann[i]['segmentation'][0][7] *= 2
print(l_ann[1])#
datas = {'images':l_img, 'annotations':l_ann, 'categories':datas['categories']}
f.close()
#print(str(datas))
with open('F:\\cvpr\\dataset\\annotaions\\train1.json', 'w') as f:
    f.write(str(datas))