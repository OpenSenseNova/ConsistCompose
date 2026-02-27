from .bagel import ConsistComposeBagelModel


def get_default_model_type(model_path):
    if "bagel" in model_path.lower():
        return "bagel"
    else:
        raise ValueError(f"Unknown model type for {model_path}")


def get_model(model_path, model_type="auto"):
    if model_type == "auto":
        model_type = get_default_model_type(model_path)
    elif model_type == "bagel":
        return SenseNovaSIBagelModel(model_path)
    else:
        raise ValueError(f"Unknown model type: {model_type}")


__all__ = [
    "get_default_model_type",
    "get_model",
    "ConsistComposeBagelModel",
]