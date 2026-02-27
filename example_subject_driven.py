import os
import json
import argparse

import torch
import random
import numpy as np

from pathlib import Path
from consist_compose import ConsistComposeBagelModel


def set_seed(seed=42):
    """Set random seed for reproducibility"""
    import random
    import numpy as np
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    # Ensure deterministic behavior for CUDA
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


def load_jsonl(file_path):
    """Load JSONL file and return list of dictionaries"""
    data = []
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"JSONL file not found: {file_path}")
    
    with open(file_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                sample = json.loads(line)
                # Validate required fields
                if "image" not in sample or "grounding_prompt" not in sample:
                    raise ValueError(f"Missing 'image' or 'grounding_prompt' field")
                # Validate image paths (check if files exist, optional but useful)
                for img_path in sample["image"]:
                    if not os.path.exists(img_path):
                        print(f"[Warning] Line {line_num}: Image file not found - {img_path}")
                data.append(sample)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON format in line {line_num}: {e}") from e
            except Exception as e:
                raise ValueError(f"Error processing line {line_num}: {e}") from e
    
    if not data:
        raise ValueError(f"Empty JSONL file: {file_path}")
    
    print(f"Successfully loaded {len(data)} samples from {file_path}")
    return data


def main():
    parser = argparse.ArgumentParser(
        description="ConsistCompose batch inference - layout control image generation from JSONL file"
    )
    parser.add_argument(
        "--model_path",
        type=str,
        default="sensenova/ConsistCompose-BAGEL-7B-MoT",
        help="BAGEL model path (local directory or Hugging Face repo ID)",
    )
    parser.add_argument(
        "--jsonl_path",
        type=str,
        default="examples/layout_subject_driven.jsonl",
        help="Path to JSONL file containing image paths and grounding prompts",
    )
    parser.add_argument(
        "--mode",
        type=str,
        default="layout_subject_driven",
        choices=["layout_t2i", "layout_subject_driven", "generate", "think_generate"],
        help="BAGEL inference mode",
    )
    parser.add_argument(
        "--out_img_dir",
        type=str,
        default="./output_images/layout_subject_driven/",
        help="Directory to save generated images (will be created if not exists)",
    )
    parser.add_argument(
        "--dtype",
        type=str,
        default="bf16",
        choices=["bf16"],
        help="Model precision type",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility",
    )
    args = parser.parse_args()

    # Create output directory
    os.makedirs(args.out_img_dir, exist_ok=True)

    # Print configuration
    print(f"Model path:        {args.model_path}")
    print(f"JSONL path:        {args.jsonl_path}")
    print(f"Mode:              {args.mode}")
    print("=" * 50)

    # Load model (load once for all samples to save time)
    print("\nLoading ConsistCompose model...")
    model = ConsistComposeBagelModel(
        model_path=args.model_path,
        out_img_dir=args.out_img_dir,
        dtype=args.dtype,
    )


    # Set random seed
    set_seed(args.seed)

    # Load JSONL data
    print(f"\nLoading data from JSONL file: {args.jsonl_path}")
    samples = load_jsonl(args.jsonl_path)

    # Process each sample
    print("\nStarting batch inference...")
    print("-" * 60)
    success_count = 0
    fail_count = 0
    
    for idx, sample in enumerate(samples, 1):
        sample_id = idx
        images = sample["image"]
        prompt = sample["grounding_prompt"]
        
        print(f"\nProcessing sample {sample_id}/{len(samples)}")
        print(f"Prompt: {prompt[:100]}..." if len(prompt) > 100 else f"Prompt: {prompt}")
        print(f"Images: {', '.join(images)}")
        
        try:
            # Generate image
            generated_image_path = model.generate(
                question=prompt,
                images=images,
                mode=args.mode,
                vis_bbox=True,
            )
            
            # Print result
            if generated_image_path:
                success_count += 1
                print(f"✅ Sample {sample_id} completed: {generated_image_path}")
            else:
                fail_count += 1
                print(f"❌ Sample {sample_id} failed: No image generated")
                
        except Exception as e:
            fail_count += 1
            print(f"❌ Sample {sample_id} error: {str(e)}")
            continue

    print("\n" + "=" * 60)
    print("Batch Inference Summary")
    print(f"Total samples:     {len(samples)}")
    print(f"Output directory:  {os.path.abspath(args.out_img_dir)}")
    print("=" * 60)
    print("\nBatch inference completed!")


if __name__ == "__main__":
    main()