# ConsistCompose: Unified Multimodal Layout Control for Image Composition

<div align="center">
  <a href="README.md">English</a> | <a href="README_CN.md">简体中文</a>
</div>

<p align="center">
    <a href="https://arxiv.org/abs/2511.18333" target="_blank">
        <img alt="arXiv" src="https://img.shields.io/badge/ConsistCompose-Paper-red?logo=arxiv" height="20" />
    </a>
    <a href="https://sensenova.github.io/ConsistCompose/" target="_blank">
        <img alt="Project Page" src="https://img.shields.io/badge/Project%20Page-ConsistCompose-blue" height="20" />
    </a>
    <a href="https://huggingface.co/sensenova/ConsistCompose-BAGEL-7B-MoT" target="_blank">
        <img alt="Model" src="https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-Model-ffc107?color=ffc107&logoColor=white" height="20" />
    </a>
    <a href="https://huggingface.co/datasets/sensenova/ConsistCompose3M" target="_blank">
        <img alt="Dataset" src="https://img.shields.io/badge/HuggingFace-Dataset-blueviolet" height="20" />
    </a>
    <a href="https://github.com/OpenSenseNova/ConsistCompose" target="_blank">
        <img alt="GitHub" src="https://img.shields.io/badge/GitHub-Code-100000?style=flat-square&logo=github&logoColor=white" height="20" />
    </a>
</p>

## Overview
ConsistCompose is a novel **unified multimodal framework** designed for layout-controllable multi-instance image composition. It addresses a critical gap in existing multimodal models—while most systems excel at visual grounding (aligning language with image regions), they lack precise control over spatial layout in generative tasks. 

Built upon the unified understanding and generation architecture of BAGEL and enhanced by SenseNova-SI's spatial intelligence, ConsistCompose introduces **Linguistic-Embedded Layout-Grounded Generation (LELG)**. This paradigm embeds layout coordinates directly into language prompts as textual tokens, eliminating the need for specialized spatial encoders or task-specific branches. To enable large-scale training, we construct **ConsistCompose3M** (3.4M samples), a high-quality dataset with layout and identity annotations that provides structured spatial-semantic supervision.

ConsistCompose achieves state-of-the-art performance on layout control benchmarks while preserving strong general multimodal capabilities, establishing a principled solution for precise, flexible image composition.


<p align="center"><img src="assets/teaser.webp" width="95%"></p>

## News
- [2026-02-27] Official release of the ConsistCompose code repository, **ConsistCompose-BAGEL-7B-MoT** model, and **ConsistCompose3M** dataset on Hugging Face
- [2026-02-22] Our work is accepted to the **CVPR2026**
- [2025-11-23] Initial submission of our paper to arXiv ([2511.18333](https://arxiv.org/abs/2511.18333))



## 📊 Benchmark Results

### 1. COCO-Position (Layout Control)
<table style="width: 100%; text-align: center; border-collapse: collapse;">
<thead>
<tr style="text-align: center;">
  <th>Methods</th>
  <th>Instance Success Ratio (Avg)</th>
  <th>Image Success Ratio (Avg)</th>
  <th>mIoU</th>
  <th>AP</th>
  <th>AP50</th>
  <th>AP75</th>
</tr>
</thead>
<tbody>
<tr>
  <td>GLIGEN</td>
  <td>82.6%</td>
  <td>52.1%</td>
  <td>69.0</td>
  <td>40.5</td>
  <td>75.9</td>
  <td>39.1</td>
</tr>
<tr>
  <td>InstanceDiffusion</td>
  <td>87.8%</td>
  <td>65.5%</td>
  <td>78.1</td>
  <td>57.2</td>
  <td>83.6</td>
  <td>65.5</td>
</tr>
<tr>
  <td>MIGC++</td>
  <td>86.8%</td>
  <td>63.4%</td>
  <td>74.9</td>
  <td>48.3</td>
  <td>79.2</td>
  <td>52.6</td>
</tr>
<tr>
  <td>CreatiLayout</td>
  <td>74.0%</td>
  <td>42.5%</td>
  <td>64.9</td>
  <td>32.4</td>
  <td>61.1</td>
  <td>31.6</td>
</tr>
<tr>
  <td>PlanGen</td>
  <td>82.5%</td>
  <td>50.3%</td>
  <td>66.2</td>
  <td>31.9</td>
  <td>74.0</td>
  <td>21.5</td>
</tr>
<tr>
  <td><b>Ours (ConsistCompose)</b></td>
  <td><b>92.6%</b></td>
  <td><b>76.1%</b></td>
  <td><b>85.3</b></td>
  <td><b>70.9</b></td>
  <td><b>89.1</b></td>
  <td><b>76.9</b></td>
</tr>
</tbody>
</table>

> 7.2% mIoU gain and 13.7% AP improvement over state-of-the-art baselines

### 2. MS-Bench & MS-Bench-Random
<table style="width: 100%; text-align: center; border-collapse: collapse;">
<thead>
<tr>
  <th rowspan="2" style="text-align: center;">Methods</th>
  <th colspan="4" style="text-align: center;">MS-Bench</th>
  <th colspan="4" style="text-align: center;">MS-Bench-Random</th>
</tr>
<tr>
  <th style="text-align: center;">CLIP-T</th>
  <th style="text-align: center;">DINO</th>
  <th style="text-align: center;">mIoU</th>
  <th style="text-align: center;">AP</th>
  <th style="text-align: center;">CLIP-T</th>
  <th style="text-align: center;">DINO</th>
  <th style="text-align: center;">mIoU</th>
  <th style="text-align: center;">AP</th>
</tr>
</thead>
<tbody>
<tr>
  <td>GLIGEN</td>
  <td>0.309</td>
  <td>0.454</td>
  <td><u>0.868</u></td>
  <td><u>0.751</u></td>
  <td>0.312</td>
  <td>0.431</td>
  <td><u>0.858</u></td>
  <td><u>0.722</u></td>
</tr>
<tr>
  <td>MS-Diffusion</td>
  <td><b>0.336</b></td>
  <td>0.555</td>
  <td>0.466</td>
  <td>0.108</td>
  <td><u>0.334</u></td>
  <td>0.544</td>
  <td>0.464</td>
  <td>0.105</td>
</tr>
<tr>
  <td>MUSE</td>
  <td>0.320</td>
  <td><u>0.619</u></td>
  <td>0.698</td>
  <td>0.352</td>
  <td>0.321</td>
  <td><u>0.607</u></td>
  <td>0.673</td>
  <td>0.303</td>
</tr>
<tr>
  <td><b>Ours</b></td>
  <td><u>0.333</u></td>
  <td><b>0.660</b></td>
  <td><b>0.889</b></td>
  <td><b>0.789</b></td>
  <td><b>0.334</b></td>
  <td><b>0.630</b></td>
  <td><b>0.878</b></td>
  <td><b>0.756</b></td>
</tr>
</tbody>
</table>

### 3. General Multimodal Capabilities
<table style="width: 100%; text-align: center; border-collapse: collapse;">
<thead>
<tr style="text-align: center;">
  <th>Model</th>
  <th>MMBench</th>
  <th>MMMU</th>
  <th>GenEval</th>
  <th>GEdit</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Bagel Base</td>
  <td>81.4</td>
  <td>46.4</td>
  <td>0.86</td>
  <td>6.68</td>
</tr>
<tr>
  <td>Ours (w/o Coord)</td>
  <td>81.5</td>
  <td>39.4</td>
  <td>0.88</td>
  <td>6.23</td>
</tr>
<tr>
  <td>Ours (w/ Coord)</td>
  <td>81.4</td>
  <td>42.3</td>
  <td>0.88</td>
  <td>6.31</td>
</tr>
</tbody>
</table>

### 4. DreamBench (Identity Preservation)
<table style="width: 100%; text-align: center; border-collapse: collapse;">
<thead>
<tr>
  <th rowspan="2" style="text-align: center;">Method</th>
  <th colspan="3" style="text-align: center;">Single</th>
  <th colspan="3" style="text-align: center;">Multi</th>
</tr>
<tr>
  <th style="text-align: center;">DINO</th>
  <th style="text-align: center;">CLIP-I</th>
  <th style="text-align: center;">CLIP-T</th>
  <th style="text-align: center;">DINO</th>
  <th style="text-align: center;">CLIP-I</th>
  <th style="text-align: center;">CLIP-T</th>
</tr>
</thead>
<tbody>
<tr>
  <td>UNO</td>
  <td>0.661</td>
  <td>0.796</td>
  <td>0.304</td>
  <td>0.491</td>
  <td>0.715</td>
  <td>0.323</td>
</tr>
<tr>
  <td>OmniGen</td>
  <td>0.554</td>
  <td>0.746</td>
  <td>0.322</td>
  <td>0.441</td>
  <td>0.692</td>
  <td>0.341</td>
</tr>
<tr>
  <td>OmniGen2</td>
  <td>0.671</td>
  <td>0.791</td>
  <td>0.312</td>
  <td>0.459</td>
  <td>0.698</td>
  <td>0.333</td>
</tr>
<tr>
  <td><b>Ours</b></td>
  <td><b>0.677</b></td>
  <td><b>0.792</b></td>
  <td><b>0.314</b></td>
  <td><b>0.506</b></td>
  <td><b>0.703</b></td>
  <td><b>0.335</b></td>
</tr>
</tbody>
</table>
## 🛠️ QuickStart

### Installation
```bash
# Clone repository
git clone git@github.com:OpenSenseNova/ConsistCompose.git
cd ConsistCompose/

conda create -n cc python=3.10 -y
conda activate cc
pip install -r requirements.txt
pip install flash_attn==2.5.8 --no-build-isolation
```

### Key Examples

#### 1. Layout Control for Text-to-Image Composition
This example performs **layout-grounded text-to-image generation** by embedding normalized bounding box coordinates directly into the prompt, enabling precise spatial control over the position and scale of each object in the output image.

```bash
python example_text2image.py  \
 --prompt "In a dimly lit cavern, a powerful dragon <bbox>[0.380, 0.086, 0.768, 0.673]</bbox> stands majestically, its textured scales glistening in the flickering firelight. Beside it, a brave man <bbox>[0.155, 0.231, 0.439, 0.717]</bbox> clad in armor, stands poised with determination, his hand gripping the hilt of a gleaming sword <bbox>[0.166, 0.401, 0.577, 0.663]</bbox> that reflects the dancing flames. The air is tense with anticipation as sparks rise from the crackling fire, illuminating the rocky surroundings and casting intricate shadows on the cavern walls. This scene paints a vivid picture of medieval fantasy, capturing a moment that is both dramatic and full of potential action." \
 --mode  layout_t2i \
 --model_path sensenova/ConsistCompose-BAGEL-7B-MoT
```

#### 2. Layout Control for Image Composition with Multi-Reference
This example supports **identity-preserving image composition with multiple references**, where the model maintains the visual characteristics of subjects from reference images while arranging them according to the given layout constraints.

```bash
python example_subject_driven.py \
  --model_path sensenova/ConsistCompose-BAGEL-7B-MoT \
  --jsonl_path examples/layout_subject_driven.jsonl \
  --mode layout_subject_driven
```


### Download Dataset
Load ConsistCompose3M via Hugging Face Datasets:
```python
from datasets import load_dataset

# Load full dataset (webdataset format)
dataset = load_dataset("sensenova/ConsistCompose3M", split="train")

# Load task-specific subset (e.g., layout-aware text-to-image)
t2i_dataset = load_dataset("sensenova/ConsistCompose3M", data_files="jsonl_extended/layout_t2i/*.jsonl")
```


## 🖊️ Citation
If you use ConsistCompose, ConsistCompose3M, or related resources in your research, please cite:
```bib
@article{shi2025consistcompose,
  title={ConsistCompose: Unified Multimodal Layout Control for Image Composition},
  author={Shi, Xuanke and Li, Boxuan and Han, Xiaoyang and Cai, Zhongang and Yang, Lei and Lin, Dahua and Wang, Quan},
  journal={arXiv preprint arXiv:2511.18333},
  year={2025}
}
```

## License
- The ConsistCompose framework and models are released under the [Apache-2.0 License](LICENSE).
- The ConsistCompose3M dataset is licensed under Apache-2.0, with additional terms for derived data (see dataset [README](https://huggingface.co/datasets/sensenova/ConsistCompose3M/blob/main/README.md) for details).
