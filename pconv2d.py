class PConv2d(nn.Module):
    def __init__(self):
        super(ASL_Classifier, self).__init__()
        self.name = "pconv_2d"
        # encoder stage
        self.pconv1 = nn.Conv2d(1, 64, kernel_size=7, stride=2)
        self.pconv2 = nn.Conv2d(64, 128, kernel_size=5, stride=2)
        self.pconv3 = nn.Conv2d(128, 256, kernel_size=5, stride=2)
        self.pconv4 = nn.Conv2d(256, 512, kernel_size=3, stride=2)
        self.pconv5 = nn.Conv2d(512, 512, kernel_size=3, stride=2)
        self.pconv6 = nn.Conv2d(512, 512, kernel_size=3, stride=2)
        self.pconv7 = nn.Conv2d(512, 512, kernel_size=3, stride=2)
        self.pconv8 = nn.Conv2d(512, 512, kernel_size=3, stride=2)        
        # decoder stage
        self.UpsamplingNN = nn.functional.interpolate(scale_factor=(2), mode='nearest')

        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(5, 10, 5)
        self.fc1 = nn.Linear(10 * 53 * 53, 32) 
        self.fc2 = nn.Linear(32, 9)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 10 * 53 * 53)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x



# https://discuss.pytorch.org/t/using-nn-function-interpolate-inside-nn-sequential/23588
# https://pytorch.org/docs/stable/_modules/torch/nn/functional.html
class Interpolate(nn.Module):
    def __init__(self, scale_factor, mode):
        super(Interpolate, self).__init__()
        self.interp = nn.functional.interpolate
        self.scale_factor = scale_factor
        self.mode = mode
        
    def forward(self, x):
        x = self.interp(x, scale_factor=self.scale_factor, mode=self.mode, align_corners=False)
        return x