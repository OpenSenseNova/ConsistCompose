import torch
import random
import argparse
import numpy as np

from consist_compose import ConsistComposeBagelModel


def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

def main():
    parser = argparse.ArgumentParser(
        description="ConsistCompose layout control image generation example - generate image from text prompt with ICBP paradigm"
    )
    parser.add_argument(
        "--model_path",
        type=str,
        default="sensenova/ConsistCompose-BAGEL-7B-MoT",
        help="BAGEL model path",
    )
    parser.add_argument(
        "--prompt",
        type=str,
        default="A chubby cat made of 3D point clouds, stretching its body, translucent with a soft glow.",
        help="Text prompt used to generate an image",
    )
    parser.add_argument(
        "--mode",
        type=str,
        default="layout_t2i",
        choices=["layout_t2i", "layout_subject_driven", "generate", "think_generate"],
        help="BAGEL mode: generate or think_generate",
    )
    parser.add_argument(
        "--out_img_dir",
        type=str,
        default="./output_images/layout_t2i/",
        help="Directory to save generated images",
    )
    parser.add_argument(
        "--dtype",
        type=str,
        default="bf16",
        choices=["bf16"],
        help="Model precision type",
    )
    args = parser.parse_args()

    print(f"Model path: {args.model_path}")
    print(f"Mode: {args.mode}")
    print(f"Prompt: {args.prompt}")
    print("-" * 50)

    # Initialize BAGEL model with generate mode
    print("\nLoading ConsistCompose model...")
    model = ConsistComposeBagelModel(
        model_path=args.model_path,
        out_img_dir=args.out_img_dir,
        dtype=args.dtype,
    )
    # Set random seed for reproducibility
    set_seed()

    print("Generating image...")
    # Call generate with the prompt; images not needed for generate mode
    generated_image_path = model.generate(question=args.prompt, images=None, mode=args.mode, vis_bbox=True)

    print("-" * 50)
    print("Done!")
    print(f"Image saved to: {generated_image_path}")


if __name__ == "__main__":
    main()