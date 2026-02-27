# ConsistCompose: 面向图像合成的统一多模态布局控制

<div align="center">
  <a href="README_zh.md">简体中文</a> | <a href="README.md">English</a>
</div>

<p align="center">
    <a href="https://arxiv.org/abs/2511.18333" target="_blank">
        <img alt="arXiv" src="https://img.shields.io/badge/ConsistCompose-论文-red?logo=arxiv" height="20" />
    </a>
    <a href="https://opensensenova.github.io/ConsistCompose/" target="_blank">
        <img alt="项目主页" src="https://img.shields.io/badge/项目主页-ConsistCompose-blue" height="20" />
    </a>
    <a href="https://huggingface.co/sensenova/ConsistCompose-BAGEL-7B-MoT" target="_blank">
        <img alt="模型" src="https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-模型-ffc107?color=ffc107&logoColor=white" height="20" />
    </a>
    <a href="https://huggingface.co/datasets/sensenova/ConsistCompose3M" target="_blank">
        <img alt="数据集" src="https://img.shields.io/badge/HuggingFace-数据集-blueviolet" height="20" />
    </a>
    <a href="https://github.com/OpenSenseNova/ConsistCompose" target="_blank">
        <img alt="GitHub" src="https://img.shields.io/badge/GitHub-代码-100000?style=flat-square&logo=github&logoColor=white" height="20" />
    </a>
</p>

## 概述
ConsistCompose 是一款面向**布局可控多实例图像合成**的新型统一多模态框架。该框架解决了现有多模态模型的核心痛点——多数模型虽擅长视觉定位（将语言与图像区域对齐），但在生成任务中缺乏对空间布局的精准控制能力。

ConsistCompose 基于 BAGEL 的统一理解与生成架构构建，并结合 SenseNova-SI 空间智能能力进行增强，创新性提出**语言嵌入型布局锚定生成（LELG）** 范式：将布局坐标直接以文本令牌形式嵌入语言提示词中，无需专用空间编码器或任务专属分支。为支撑大规模训练，我们构建了 **ConsistCompose3M**（340 万样本）高质量数据集，该数据集包含布局和身份标注，可为统一多模态学习提供结构化的空间语义监督。

ConsistCompose 在布局控制基准测试中达到业界领先性能，同时保持强大的通用多模态能力，为精准、灵活的图像合成提供了一套规范的解决方案。

<p align="center"><img src="assets/teaser.webp" width="95%"></p>

## 最新动态
- [2026-02-27] 正式发布 ConsistCompose 代码仓库、**ConsistCompose-BAGEL-7B-MoT** 模型及 **ConsistCompose3M** 数据集（Hugging Face）
- [2026-02-22] 相关研究成果被 **CVPR2026** 接收
- [2025-11-23] 论文首次提交至 arXiv ([2511.18333](https://arxiv.org/abs/2511.18333))

## 📊 基准测试结果

### 1. COCO-Position（布局控制）
<table style="width: 100%; text-align: center; border-collapse: collapse;">
<thead>
<tr style="text-align: center;">
  <th>方法</th>
  <th>实例成功率（平均）</th>
  <th>图像成功率（平均）</th>
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

> 相较于当前最优基线方法，mIoU 提升 7.2%，AP 提升 13.7%

---

### 2. MS-Bench & MS-Bench-Random
<table style="width: 100%; text-align: center; border-collapse: collapse;">
<thead>
<tr>
  <th rowspan="2" style="text-align: center;">方法</th>
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
  <td>0.868</td>
  <td>0.751</td>
  <td>0.312</td>
  <td>0.431</td>
  <td>0.858</td>
  <td>0.722</td>
</tr>
<tr>
  <td>MS-Diffusion</td>
  <td>0.336</td>
  <td>0.555</td>
  <td>0.466</td>
  <td>0.108</td>
  <td>0.334</td>
  <td>0.544</td>
  <td>0.464</td>
  <td>0.105</td>
</tr>
<tr>
  <td>MUSE</td>
  <td>0.320</td>
  <td>0.619</td>
  <td>0.698</td>
  <td>0.352</td>
  <td>0.321</td>
  <td>0.607</td>
  <td>0.673</td>
  <td>0.303</td>
</tr>
<tr>
  <td><b>Ours (ConsistCompose)</b></td>
  <td><b>0.333</b></td>
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

---

### 3. 通用多模态能力
<table style="width: 100%; text-align: center; border-collapse: collapse;">
<thead>
<tr style="text-align: center;">
  <th>模型</th>
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
  <td>Ours (无坐标)</td>
  <td>81.5</td>
  <td>39.4</td>
  <td>0.88</td>
  <td>6.23</td>
</tr>
<tr>
  <td>Ours (有坐标)</td>
  <td>81.4</td>
  <td>42.3</td>
  <td>0.88</td>
  <td>6.31</td>
</tr>
</tbody>
</table>

---

### 4. DreamBench（身份保留）
<table style="width: 100%; text-align: center; border-collapse: collapse;">
<thead>
<tr>
  <th rowspan="2" style="text-align: center;">方法</th>
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
  <td><b>Ours (ConsistCompose)</b></td>
  <td><b>0.677</b></td>
  <td><b>0.792</b></td>
  <td><b>0.314</b></td>
  <td><b>0.506</b></td>
  <td><b>0.703</b></td>
  <td><b>0.335</b></td>
</tr>
</tbody>
</table>
## 🛠️ 快速开始

### 环境安装
```bash
# 克隆代码仓库
git clone git@github.com:OpenSenseNova/ConsistCompose.git
cd ConsistCompose/

# 创建并激活 conda 环境
conda create -n cc python=3.10 -y
conda activate cc

# 安装基础依赖
pip install -r requirements.txt

# 安装 flash_attn（关键依赖）
pip install flash_attn==2.5.8 --no-build-isolation
```

### 核心示例

#### 1. 文本到图像的布局控制合成
该示例实现**基于布局锚定的文本到图像生成**，通过在提示词中嵌入归一化边界框坐标，可对输出图像中每个物体的位置和尺寸实现精准的空间控制。

```bash
python example_text2image.py  \
 --prompt "In a dimly lit cavern, a powerful dragon <bbox>[0.380, 0.086, 0.768, 0.673]</bbox> stands majestically, its textured scales glistening in the flickering firelight. Beside it, a brave man <bbox>[0.155, 0.231, 0.439, 0.717]</bbox> clad in armor, stands poised with determination, his hand gripping the hilt of a gleaming sword <bbox>[0.166, 0.401, 0.577, 0.663]</bbox> that reflects the dancing flames. The air is tense with anticipation as sparks rise from the crackling fire, illuminating the rocky surroundings and casting intricate shadows on the cavern walls. This scene paints a vivid picture of medieval fantasy, capturing a moment that is both dramatic and full of potential action." \
 --mode layout_t2i \
 --model_path sensenova/ConsistCompose-BAGEL-7B-MoT
```

#### 2. 多参考图像的布局控制合成
该示例支持**保留身份的多参考图像合成**，模型会保留参考图像中主体的视觉特征，同时按照给定的布局约束排列这些主体。

```bash
python example_subject_driven.py \
  --model_path sensenova/ConsistCompose-BAGEL-7B-MoT \
  --jsonl_path examples/layout_subject_driven.jsonl \
  --mode layout_subject_driven
```

### 数据集下载
通过 Hugging Face Datasets 加载 ConsistCompose3M 数据集：
```python
from datasets import load_dataset

dataset = load_dataset("sensenova/ConsistCompose3M", split="train")

t2i_dataset = load_dataset("sensenova/ConsistCompose3M", data_files="jsonl_extended/layout_t2i/*.jsonl")
```


## 🖊️ 引用
如果你的研究中使用了 ConsistCompose、ConsistCompose3M 或相关资源，请引用以下论文：
```bib
@article{shi2025consistcompose,
  title={ConsistCompose: Unified Multimodal Layout Control for Image Composition},
  author={Shi, Xuanke and Li, Boxuan and Han, Xiaoyang and Cai, Zhongang and Yang, Lei and Lin, Dahua and Wang, Quan},
  journal={arXiv preprint arXiv:2511.18333},
  year={2025}
}
```

## 许可证
- ConsistCompose 框架及模型基于 [Apache-2.0 许可证](LICENSE) 开源。
- ConsistCompose3M 数据集同样采用 Apache-2.0 许可证，衍生数据需遵循额外条款（详见数据集 [README](https://huggingface.co/datasets/sensenova/ConsistCompose3M/blob/main/README.md)）。
