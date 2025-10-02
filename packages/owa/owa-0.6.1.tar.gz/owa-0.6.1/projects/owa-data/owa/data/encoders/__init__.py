from .base_encoder import BaseEventEncoder
from .exceptions import (
    EventEncoderError,
    InvalidInputError,
    InvalidTokenError,
    UnsupportedInputError,
    UnsupportedTokenError,
)
from .factorized_event_encoder import FactorizedEventEncoder, FactorizedEventEncoderConfig
from .hierarchical_event_encoder import HierarchicalEventEncoder, HierarchicalEventEncoderConfig
from .json_event_encoder import JSONEventEncoder, JSONEventEncoderConfig


def create_encoder(encoder_type: str, **kwargs) -> BaseEventEncoder:
    """Create an encoder instance based on the specified type."""
    encoders = {
        "hierarchical": HierarchicalEventEncoder,
        "factorized": FactorizedEventEncoder,
        "json": JSONEventEncoder,
    }

    encoder_class = encoders.get(encoder_type.lower())
    if encoder_class is None:
        raise ValueError(f"Unsupported encoder type: {encoder_type}. Available: {list(encoders.keys())}")

    return encoder_class(**kwargs)


__all__ = [
    "BaseEventEncoder",
    "EventEncoderError",
    "InvalidInputError",
    "InvalidTokenError",
    "UnsupportedInputError",
    "UnsupportedTokenError",
    "create_encoder",
    "JSONEventEncoder",
    "HierarchicalEventEncoder",
    "HierarchicalEventEncoderConfig",
    "FactorizedEventEncoder",
    "FactorizedEventEncoderConfig",
    "JSONEventEncoderConfig",
]
