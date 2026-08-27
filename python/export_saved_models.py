"""
Export and serialize the 3 trained ML models to .sav files using Python pickle.
Creates files in saved_models/ and models/ directories.
"""
import os
import pickle
from diabetes_model import DiabetesModel
from heart_disease_model import HeartDiseaseModel
from parkinsons_model import ParkinsonsModel

def export_models():
    os.makedirs("saved_models", exist_ok=True)
    os.makedirs("models", exist_ok=True)
    
    diabetes = DiabetesModel()
    heart = HeartDiseaseModel()
    parkinsons = ParkinsonsModel()
    
    # Save to saved_models/
    with open("saved_models/diabetes_model.sav", "wb") as f:
        pickle.dump(diabetes, f)
    with open("saved_models/heart_disease_model.sav", "wb") as f:
        pickle.dump(heart, f)
    with open("saved_models/parkinsons_model.sav", "wb") as f:
        pickle.dump(parkinsons, f)
        
    # Save to models/ as well for compatibility
    with open("models/diabetes_model.sav", "wb") as f:
        pickle.dump(diabetes, f)
    with open("models/heart_disease_model.sav", "wb") as f:
        pickle.dump(heart, f)
    with open("models/parkinsons_model.sav", "wb") as f:
        pickle.dump(parkinsons, f)
        
    print("Exported .sav models successfully to saved_models/ and models/")

if __name__ == '__main__':
    export_models()
