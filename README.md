# WakeupUrban: Unsupervised Semantic Segmentation of Mid-20<sup>th</sup> century Urban Landscapes with Satellite Imagery

## 🌍 Overview

<table>
  <tr>
    <td style="vertical-align: top; width: 220px;">
      <img src="https://github.com/Tianxiang-Hao/WakeupUrban/blob/main/pictures/head.png" width="200" />
    </td>
    <td style="vertical-align: top; padding-left: 16px;">
      Historical satellite imagery archive, such as Keyhole satellite data, offers rare insights into understanding early urban development and long-term transformation. However, severe quality degradation ($\textit{e.g.}$, distortion, misalignment, and spectral scarcity) and the absence of annotations have long hindered its analysis. To bridge this gap and enhance understanding of urban development, we introduce $\textbf{WakeupUrbanBench}$, an annotated segmentation dataset based on historical satellite imagery with the earliest observation time among all existing remote sensing (RS) datasets, along with a framework for unsupervised segmentation tasks, $\textbf{WakeupUSM}$. First, WakeupUrbanBench serves as a pioneer, expertly annotated dataset built on mid-$20^{\text{th}}$ century RS imagery, involving four key urban classes and spanning 4 cities across 2 continents with nearly 1000 km$^2$ area of diverse urban morphologies, and additionally introducing one present-day city. Second, WakeupUSM is a novel unsupervised semantic segmentation framework for historical RS imagery. It employs a confidence-aware alignment mechanism and focal-confidence loss based on a self-supervised learning architecture, which generates robust pseudo-labels and adaptively prioritizes prediction difficulty and label reliability to improve unsupervised segmentation on noisy historical data without manual supervision. Comprehensive experiments demonstrate WakeupUSM significantly outperforms existing unsupervised segmentation methods $\textbf{both WakeupUrbanBench and public dataset}$, promising to pave the way for quantitative studies of long-term urban change using modern computer vision. Our full benchmark and models will be released later.
    </td>
  </tr>
</table>

## 📊 Datasets

<div align="center">
  <img src="https://github.com/Tianxiang-Hao/WakeupUrban/blob/main/pictures/relatedwork.png" style="width: 50%;">
</div>

Visualization of high-resolution remote sensing segmentation datasets by year, resolution, and coverage. More recent datasets show greater diversity in resolution and extent, while Urban1960SatBench is the earliest with relatively high resolution, bridging a key temporal gap.
### 🔧 How to use


<div align="center">
  <img src="https://github.com/Tianxiang-Hao/WakeupUrban/blob/main/pictures/intro.png" style="width: 80%;">
</div>

WakeupUrbanBench is a high-fidelity, city-scale semantic segmentation benchmark built from declassified 1960s Keyhole panchromatic reconnaissance imagery co-registered with contemporaneous official urban maps. We provide pixel-level labels for impervious surface and five land-use categories—roads, buildings, water bodies, green lands, and other urban types. Spanning four cities across two countries and two periods (1960s and 2020s), the benchmark constitutes a challenging domain due to grayscale distortions and limited spatial resolution in reconnaissance imagery, and it enables studies in historical urban morphology, cultural-heritage conservation, and cross-temporal/cross-city generalization. All assets (original imagery, semantic masks, impervious-surface “ISP” masks, metadata, and baseline scripts), together with detailed documentation, will be publicly released under a Creative Commons Attribution–NonCommercial (CC BY-NC) license on GitHub and Hugging Face.

#### Data preparation
To access the demo dataset (an earlier version for show), please download it here: [🔗 Urban1960SatBench](https://doi.org/10.7910/DVN/HT2B1S)

Usage examples are provided in the following Python files: [WakeupUrbanSS](https://github.com/Tianxiang-Hao/WakeupUrban/blob/main/datasets/wakeupurban.py) and [WakeupUrbanISP](https://github.com/Tianxiang-Hao/WakeupUrban/blob/main/datasets/wakeupurbanisp.py).

### The full dataset will be released soon...

## 📊 Model
<div align="center">
  <img src="https://github.com/Tianxiang-Hao/WakeupUrban/blob/main/pictures/model.png" style="width: 70%;">
</div>

### Model details will be announced soon...

## 📢 Reference & Statement
The architecture of the Model is mainly referenced from [Dino](https://github.com/facebookresearch/dino),[Dinov2](https://github.com/facebookresearch/dinov2), [SAM2](https://github.com/facebookresearch/sam2) and [Primaps](https://github.com/visinf/primaps). 

All experiments are carried out on NVIDIA 4090.

WakeupUrban will be continuously updated to include additional locations, time periods, and other categories, supporting broader research on early urban development processes and image segmentation.

## Citing WakeupUrban:

If you find this datasets or repository useful, please consider giving a star :star: and citation :t-rex::

```
@misc{hao2025urban1960satsegunsupervisedsemanticsegmentation,
      title={Urban1960SatSeg: Unsupervised Semantic Segmentation of Mid-20$^{th}$ century Urban Landscapes with Satellite Imageries}, 
      author={Tianxiang Hao and Lixian Zhang and Yingjia Zhang and Mengxuan Chen and Jinxiao Zhang and Haohuan Fu},
      year={2025},
      eprint={2506.09476},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2506.09476}, 
}
```
```
@data{DVN/HT2B1S_2025,
author = {Hao, Tianxiang and Zhang,Lixian and Zhang,Yingjia and Chen, Mengxuan and Zhang,Jinxiao and Fu,Haohuan},
publisher = {Harvard Dataverse},
title = {{Urban1960SatBench}},
year = {2025},
version = {V1},
doi = {10.7910/DVN/HT2B1S},
url = {https://doi.org/10.7910/DVN/HT2B1S}
}
```
