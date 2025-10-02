from enum import StrEnum

import line_profiler
import torch
from transformers import ProcessorMixin


class ModelType(StrEnum):
    """Supported vision-language model types for data collation."""

    INTERNVL = "internvl"
    SMOLVLM = "smolvlm"
    UNKNOWN = "unknown"


def detect_model_type(model_name_or_path: str) -> ModelType:
    """Detect model type from HuggingFace model configuration."""
    from transformers import AutoConfig

    config = AutoConfig.from_pretrained(model_name_or_path)
    if config.model_type == "internvl":
        return ModelType.INTERNVL
    elif config.model_type == "smolvlm":
        return ModelType.SMOLVLM
    else:
        return ModelType.UNKNOWN


@line_profiler.profile
def collate_fn_smolvlm2(examples, max_sequence_length: int | None = None, processor: "ProcessorMixin | None" = None):
    """Collate function for SmolVLM2/Idefics3 with image padding."""
    input_ids_list = []
    attention_mask_list = []
    pixel_values_list = []

    for example in examples:
        input_ids_list.append(example["input_ids"])
        attention_mask_list.append(example["attention_mask"])
        pixel_values_list.append(example["images"])
        assert isinstance(example["images"], torch.Tensor), f"Expected tensor, got {type(example['images'])}"

    max_num_images = max([len(images) for images in pixel_values_list], default=0)

    # Pad image sequences to uniform length
    for idx, images in enumerate(pixel_values_list):
        if len(images) < max_num_images:
            # NOTE: Idefics3/SmolVLM expect all-zero image to be a padding image. see: https://github.com/huggingface/transformers/blob/69b158260fcb679ea3bfbc1e6a358545ee53ee28/src/transformers/models/idefics3/modeling_idefics3.py#L693
            padding = torch.zeros(max_num_images - len(images), *images.shape[1:], dtype=torch.float32)
            pixel_values_list[idx] = torch.concat([images, padding])

    # Convert to tensors
    input_ids = torch.stack(input_ids_list)  # [batch_size, seq_len]
    attention_mask = torch.stack(attention_mask_list)  # [batch_size, seq_len]
    pixel_values = torch.stack(pixel_values_list)  # [batch_size, max_num_images, 3, max_heights, max_widths]

    if max_sequence_length is not None and input_ids.shape[1] != max_sequence_length:
        raise ValueError(
            f"Input ids length ({input_ids.shape[1]}) does not match max_sequence_length ({max_sequence_length})"
        )

    # NOTE: we shift the labels inside the model, so we don't need to do it here
    labels = input_ids.clone()
    if processor is not None:
        # Mask padding and image tokens from loss computation
        labels[labels == processor.tokenizer.pad_token_id] = -100
        labels[labels == processor.tokenizer.image_token_id] = -100
        assert (labels[attention_mask == 0] == -100).all()
    else:
        labels[attention_mask == 0] = -100

    batch = {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "labels": labels,
        "pixel_values": pixel_values,
    }
    return batch


@line_profiler.profile
def collate_fn_internvl3(examples, max_sequence_length: int | None = None, processor: "ProcessorMixin | None" = None):
    """Collate function for InternVL3 with flattened image processing."""
    input_ids_list = []
    attention_mask_list = []
    all_images = []

    for example in examples:
        input_ids_list.append(example["input_ids"])
        attention_mask_list.append(example["attention_mask"])
        images = example["images"]
        if len(images) > 0:
            all_images.extend(images)

    # Flatten all images: (total_images, C, H, W)
    pixel_values = torch.stack(all_images) if all_images else torch.empty(0, 3, 448, 448)

    input_ids = torch.stack(input_ids_list)
    attention_mask = torch.stack(attention_mask_list)

    if max_sequence_length is not None and input_ids.shape[1] != max_sequence_length:
        raise ValueError(f"Input ids length ({input_ids.shape[1]}) != max_sequence_length ({max_sequence_length})")

    labels = input_ids.clone()
    if processor is not None:
        labels[labels == processor.tokenizer.pad_token_id] = -100

        # Ignore the image token index in the loss computation
        # For InternVL3, the tokenizer doesn't have image_token_id, so use processor
        labels[labels == processor.image_token_id] = -100
        assert (labels[attention_mask == 0] == -100).all()
    else:
        labels[attention_mask == 0] = -100

    if pixel_values.shape[0] == 0:
        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "labels": labels,
        }

    return {
        "input_ids": input_ids,
        "attention_mask": attention_mask,
        "labels": labels,
        "pixel_values": pixel_values,
    }


def get_collate_fn(model_name_or_path: str):
    """Get the appropriate collate function based on model type."""
    model_type = detect_model_type(model_name_or_path)

    if model_type == ModelType.INTERNVL:
        return collate_fn_internvl3
    elif model_type == ModelType.SMOLVLM:
        return collate_fn_smolvlm2
    else:
        raise ValueError(f"Unknown model type: {model_type}")
