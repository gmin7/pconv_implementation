I tried my hand at a bare bones implementation of NVIDIA's phenomenal photo inpainting algorithm: https://www.nvidia.com/research/inpainting/
It was a great opportunity to implement their pconv layer and get it functioning on a subset of Places2 using their non-rectangular binary masks which they made custom. Inpainting papers prior to this one mainly focussed on binary masks which were rectangular whereas this one allowed for more sophisticated image distortions.

Original paper found here explaining their novel Partial Convolution Layer architecture: https://arxiv.org/abs/1804.07723

Mask dataset: https://nv-adlr.github.io/publication/partialconv-inpainting

References that influenced my approach:
https://github.com/NVIDIA/partialconv
https://github.com/bobqywei/inpainting-partial-conv

Results obtained from overfitting onto a minidataset I pulled from Places2 and the above masks:
<p float="left">
  <img src="/results/p11.png" width="300" />
  <img src="/results/p12.png" width="300" />
</p>
<p float="left">
  <img src="/results/p21.png" width="300" />
  <img src="/results/p22.png" width="300" />
</p>
