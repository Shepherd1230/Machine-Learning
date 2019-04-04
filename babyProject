# 两层的全连接层神经网络

import torch
import torch.nn as nn
import torch.nn.functional as F
class MyNet(nn.Module):
    def __init__(self):
        super(MyNet, self).__init__()  #调用父类的初始化函数
        self.f1 = nn.Linear(100, 200)
        self.f2 = nn.Linear(200, 10)
    def forward(self, x):
        x = self.f1(x)
        x = F.relu(x)
        x = self.f2(x)
        x = F.softmax(x,dim=-1)
        return x

x=torch.ones(100,dtype=torch.float)
net=MyNet()

y=net(x)
print(y)
