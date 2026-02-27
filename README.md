# ConsistCompose: Unified Multimodal Layout Control for Image Composition

<div align="center">
English | [简体中文](README_CN.md)

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
</div>

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
| Methods | Instance Success Ratio (Avg) | Image Success Ratio (Avg) | mIoU | AP | AP50 | AP75 |
|---------|------------------------------|---------------------------|------|----|------|------|
| GLIGEN | 82.6% | 52.1% | 69.0 | 40.5 | 75.9 | 39.1 |
| InstanceDiffusion | 87.8% | 65.5% | 78.1 | 57.2 | 83.6 | 65.5 |
| MIGC++ | 86.8% | 63.4% | 74.9 | 48.3 | 79.2 | 52.6 |
| CreatiLayout | 74.0% | 42.5% | 64.9 | 32.4 | 61.1 | 31.6 |
| PlanGen | 82.5% | 50.3% | 66.2 | 31.9 | 74.0 | 21.5 |
| **Ours (ConsistCompose)** | **92.6%** | **76.1%** | **85.3** | **70.9** | **89.1** | **76.9** |

> 7.2% mIoU gain and 13.7% AP improvement over state-of-the-art baselines

### 2. MS-Bench & MS-Bench-Random
| Methods | MS-Bench | | | | MS-Bench-Random | | | |
|---------|----------|------|------|----|----------------|------|------|----|
| | CLIP-T | DINO | mIoU | AP | CLIP-T | DINO | mIoU | AP |
| GLIGEN | 0.309 | 0.454 | 0.868 | 0.751 | 0.312 | 0.431 | 0.858 | 0.722 |
| MS-Diffusion | 0.336 | 0.555 | 0.466 | 0.108 | 0.334 | 0.544 | 0.464 | 0.105 |
| MUSE | 0.320 | 0.619 | 0.698 | 0.352 | 0.321 | 0.607 | 0.673 | 0.303 |
| **Ours (ConsistCompose)** | **0.333** | **0.660** | **0.889** | **0.789** | **0.334** | **0.630** | **0.878** | **0.756** |

### 3. General Multimodal Capabilities
| Model | MMBench | MMMU | GenEval | GEdit |
|-------|----------|------|---------|-------|
| Bagel Base | 81.4 | 46.4 | 0.86 | 6.68 |
| Ours (w/o Coord) | 81.5 | 39.4 | 0.88 | 6.23 |
| Ours (w/ Coord) | 81.4 | 42.3 | 0.88 | 6.31 |

### 4. DreamBench (Identity Preservation)
| Method | Single | | | Multi | | |
|---------|--------|--------|--------|-------|-------|-------|
| | DINO | CLIP-I | CLIP-T | DINO | CLIP-I | CLIP-T |
| UNO | 0.661 | 0.796 | 0.304 | 0.491 | 0.715 | 0.323 |
| OmniGen | 0.554 | 0.746 | 0.322 | 0.441 | 0.692 | 0.341 |
| OmniGen2 | 0.671 | 0.791 | 0.312 | 0.459 | 0.698 | 0.333 |
| **Ours (ConsistCompose)** | **0.677** | **0.792** | **0.314** | **0.506** | **0.703** | **0.335** |

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

<!-- ## Evaluation
To reproduce benchmark results, use the official evaluation pipeline:
```bash
# Install EASI evaluation suite
git clone git@github.com/EvolvingLMMs-Lab/EASI.git
cd EASI && pip install -e .

# Run layout control evaluation
python evaluate.py \
  --model consistcompose \
  --model_path sensenova/ConsistCompose-BAGEL-7B-MoT \
  --benchmark coco_position,ms_bench,dreambench \
  --output_path results/consistcompose_evaluation.json \
  --num_samples 1000
``` -->

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
