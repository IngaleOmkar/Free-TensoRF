# Free-TensoRF: Frequency Regularized Tensorial Radiance Field

This project has been done as a Final Year Project and submitted in partial fulfillment of the degree of Bachelor of Engineering (Computer Science) of the Nanyang Technological University, Singapore.

This codebase has referenced other repositories which are recommended for viewing before exploring this repository:

- TensoRF: [Paper](https://arxiv.org/abs/2203.09517) | [GitHub](https://github.com/apchenstu/TensoRF) | [Project Page](https://apchenstu.github.io/TensoRF/)
- FreeNeRF: [Paper](https://arxiv.org/abs/2303.07418) | [GitHub](https://github.com/Jiawei-Yang/FreeNeRF) | [Project Page](https://jiawei-yang.github.io/FreeNeRF/)


Table of Contents

- [Abstract](#Abstract)
- [Data](#Data)
- [Output](#Output)
- [Instructions](#Instructions)


## Abstract
The goal of this study was to implement frequency regularization as studied in FreeNeRF into TensoRF. Metrics such as PSNR, SSIM, and LPIPS were used to judge the new Free-TensoRF model. Conclusions reached include (mentioned from report):
1. On the flower dataset, decoder functions that do not rely on features seem to be more successful.
2. Higher number of iterations lead to better performance and rendering of the scene.
3. Using frequency regularization in the decoder function leads to better rendering results.
This can be ascertained as:
    - It leads to better image quality and lower noise (visual inspection)
    - It leads to a higher Peak Signal-To-Noise Ratio (PSNR)
    - It leads to a higher Structural Similarity Index (SSIM)
    - A better (lower) Learned Perceptual Image Patch Similarity (LPIPS) score for both
AlexNet and VGG.
4. The best combination, especially for the flower dataset, seems to be the frequency
regularized decoder function without features with 10k steps. This is based on the available resources (this study used the T4 GPU in Google Colab). A better GPU along with more steps will certainly lead to a better rendering.
5. Lastly, the memory footprint of models created by Free-TensoRF is similar to that of models created by TensoRF.

## Data

The data used was from the LLFF dataset (flower). It can be found [here](https://drive.google.com/drive/u/0/folders/128yBriW1IG_3NJ5Rp7APSTZsJqdJdfc1).

## Output

The outputs of the experiments can be found [here](https://drive.google.com/drive/u/0/folders/1y7y7N5ejZBKyPjW53xZNfqF6pCoK4twc).

## Instructions

The code was run using Google Colab. You can use any of the notebooks that have been provided in the [ColabScripts](/ColabScripts/) directory to execute the codebase.

This assumes that you have added the data from the dataset in your google drive. You can do so by adding a shortcut from the repository to your own directory in drive. 

For convience, you can add the shortcut to your Colab Notebooks directory in Drive. All the notebooks in this project assume that location for data directory. Change as necessary.

'''
.../Colab Notebooks/nerf__llff_data/flower
'''

To run, you can use:
'''python
python train.py --config path/to/your/config --ckpt path/to/your/log/folder --freq 1 --shadingMode "MLP_PE"
'''
