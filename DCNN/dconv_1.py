from torchvision import transforms, datasets as ds
import torchvision as tv
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import numpy as np
from torch import nn
from torch.nn import init, Parameter
from torch.autograd import Variable
import torch
torch.set_default_tensor_type(torch.DoubleTensor)
DEVICE = ('cuda:0')
transform = transforms.Compose(
    [
        transforms.ToTensor()
    ]
)
#/media/asxz/新加卷/dataset/DarkFace_Train_2021/image/
train_set = tv.datasets.ImageFolder(root='./', transform=transform)
data_loader = DataLoader(dataset=train_set)
 
to_pil_image = transforms.ToPILImage()
ll = 0
for image, label in data_loader:
    ll += 1
    img = image[0]
    img = np.transpose(img, (1, 2, 0))  # 把channel那一维放到最后
    img_a = np.zeros((img.shape[2], img.shape[0] * 2 - 1, img.shape[1] * 2 - 1))
    print('image shape =',img.shape)
    img_shape = list(img.shape)
    for i in range(img_shape[2]):
        for j in range(0, img_shape[0] * 2 - 1, 2):
#            if j % 2 == 0:
                for k in range(0, img_shape[1] * 2 - 1, 2):
#                    if j % 2 == 0:
                        #img_l[i][j].append(img[int((j-1)/2), int((k-1)/2),i])
                        img_a[i,j,k] = img[int(j/2), int(k/2),i]

    #plt.imshow(img)
    print('enforced image shape =', img_a.shape)
    img = np.transpose(img_a, (1, 2, 0))
    for i in range(1):
        img1 = torch.tensor([img_a]).double().to(DEVICE)
        dconv=nn.ConvTranspose2d(in_channels=3,out_channels=3,kernel_size=3,
            stride=1,padding=1,bias=False)

        init.constant(dconv.weight,1)
        dconv.weight = Parameter(torch.tensor([[[[0.25, 0.5, 0.25],[0.5, 1, 0.5],[0.25, 0.5, 0.25]], [[0., 0., 0.],[0., 0., 0.],[0., 0., 0.]], [[0., 0., 0.],[0., 0., 0.],[0., 0., 0.]]], [[[0., 0., 0.],[0., 0., 0.],[0., 0., 0.]], [[0.25, 0.5, 0.25],[0.5, 1, 0.5],[0.25, 0.5, 0.25]], [[0., 0., 0.],[0., 0., 0.],[0., 0., 0.]]], [[[0., 0., 0.],[0., 0., 0.],[0., 0., 0.]], [[0., 0., 0.],[0., 0., 0.],[0., 0., 0.]], [[0.25, 0.5, 0.25],[0.5, 1, 0.5],[0.25, 0.5, 0.25]]]], requires_grad=True).to(DEVICE))
        #print(dconv.weight, '\n')

        input_ = Variable(img1).double()
        input_ = input_.double()
        #print(input_,'\n\n\n', img_a)
        ip = dconv(input_).detach()
        #print(ip)
    plt.imshow(np.transpose(ip.cpu().numpy()[0,:,:,:], (1, 2, 0)))
    plt.savefig(f'{ll}.png', dpi=500, bbox_inches = 'tight')
