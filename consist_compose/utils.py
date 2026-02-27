import math
import random
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import re


def extract_bbox_and_subject(prompt: str):

    pattern = r'([^<]+?)\s*<bbox>\[([0-9.]+),\s*([0-9.]+),\s*([0-9.]+),\s*([0-9.]+)\]</bbox>'
    matches = re.findall(pattern, prompt)
    
    results = []
    for match in matches:
        subject = match[0].strip()
        x1, y1, x2, y2 = map(float, match[1:5])
        results.append((x1, y1, x2, y2, subject))
    return results


def draw_bbox(image: Image.Image, bbox_info: list) -> Image.Image:
    BBOX_COLORS = [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (255, 255, 0),
        (255, 0, 255),
        (0, 255, 255),
        (128, 0, 0),
        (0, 128, 0),
        (0, 0, 128),
        (255, 165, 0)
    ]

    BBOX_WIDTH = 3  
    draw = ImageDraw.Draw(image, "RGBA")
    img_width, img_height = image.size

    for idx, (x1, y1, x2, y2, _) in enumerate(bbox_info):
        x1_px = int(x1 * img_width)
        y1_px = int(y1 * img_height)
        x2_px = int(x2 * img_width)
        y2_px = int(y2 * img_height)

        color = BBOX_COLORS[idx % len(BBOX_COLORS)]
        
        draw.rectangle([x1_px, y1_px, x2_px, y2_px], 
                      outline=color, width=BBOX_WIDTH)

    return image


def resize_image_to_short_edge(image: Image.Image, short_edge: int = 512) -> Image.Image:
    width, height = image.size
    if width <= height:
        new_width = short_edge
        new_height = int(height * (short_edge / width))
    else:
        new_height = short_edge
        new_width = int(width * (short_edge / height))
    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    return resized_image


def add_special_tokens(tokenizer):
    all_special_tokens = []
    for k, v in tokenizer.special_tokens_map.items():
        if isinstance(v, str):
            all_special_tokens.append(v)
        elif isinstance(v, list):
            all_special_tokens += v

    new_tokens = []

    if "<|im_start|>" not in all_special_tokens:
        new_tokens.append("<|im_start|>")

    if "<|im_end|>" not in all_special_tokens:
        new_tokens.append("<|im_end|>")

    if "<|vision_start|>" not in all_special_tokens:
        new_tokens.append("<|vision_start|>")

    if "<|vision_end|>" not in all_special_tokens:
        new_tokens.append("<|vision_end|>")

    num_new_tokens = tokenizer.add_tokens(new_tokens)
    bos_token_id = tokenizer.convert_tokens_to_ids("<|im_start|>")
    eos_token_id = tokenizer.convert_tokens_to_ids("<|im_end|>")
    start_of_image = tokenizer.convert_tokens_to_ids("<|vision_start|>")
    end_of_image = tokenizer.convert_tokens_to_ids("<|vision_end|>")

    new_token_ids = dict(
        bos_token_id=bos_token_id,
        eos_token_id=eos_token_id,
        start_of_image=start_of_image,
        end_of_image=end_of_image,
    )

    return tokenizer, new_token_ids, num_new_tokens