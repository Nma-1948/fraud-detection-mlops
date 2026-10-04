"""Fraud detection model utilities."""

MODEL_VERSION = "0.1.0"


def model_info():
    """Return basic information about the current model."""
    return {
        "name": "fraud-detection-model",
        "version": MODEL_VERSION,
        "status": "development",
    }
