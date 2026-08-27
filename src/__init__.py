"""
Source package for Multiple Disease Prediction System.
"""
from python.diabetes_model import DiabetesModel
from python.heart_disease_model import HeartDiseaseModel
from python.parkinsons_model import ParkinsonsModel
from src.presets import DIABETES_PRESETS, HEART_PRESETS, PARKINSONS_PRESETS

__all__ = [
    "DiabetesModel",
    "HeartDiseaseModel",
    "ParkinsonsModel",
    "DIABETES_PRESETS",
    "HEART_PRESETS",
    "PARKINSONS_PRESETS"
]
