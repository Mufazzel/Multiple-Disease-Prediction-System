#!/usr/bin/env python3
import sys
import json
from diabetes_model import DiabetesModel
from heart_disease_model import HeartDiseaseModel
from parkinsons_model import ParkinsonsModel

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Missing model name argument"}))
        sys.exit(1)

    model_name = sys.argv[1].lower()

    # Read input payload from second argument or stdin
    payload_str = ""
    if len(sys.argv) >= 3:
        payload_str = sys.argv[2]
    else:
        payload_str = sys.stdin.read()

    try:
        data = json.loads(payload_str) if payload_str.strip() else {}
    except Exception as e:
        print(json.dumps({"error": f"Invalid JSON payload: {str(e)}"}))
        sys.exit(1)

    result = {}
    if model_name in ['diabetes', 'diabetes_model']:
        model = DiabetesModel()
        result = model.predict(data)
    elif model_name in ['heart', 'heart_disease', 'heart_disease_model']:
        model = HeartDiseaseModel()
        result = model.predict(data)
    elif model_name in ['parkinsons', 'parkinsons_model']:
        model = ParkinsonsModel()
        result = model.predict(data)
    elif model_name == 'batch':
        # Batch evaluation
        items = data.get('items', [])
        disease = data.get('disease', 'diabetes')
        batch_results = []

        if disease == 'diabetes':
            m = DiabetesModel()
            for it in items:
                batch_results.append(m.predict(it))
        elif disease == 'heart':
            m = HeartDiseaseModel()
            for it in items:
                batch_results.append(m.predict(it))
        elif disease == 'parkinsons':
            m = ParkinsonsModel()
            for it in items:
                batch_results.append(m.predict(it))
        else:
            result = {"error": f"Unknown batch disease: {disease}"}

        result = {"disease": disease, "results": batch_results, "count": len(batch_results)}
    else:
        result = {"error": f"Unknown model name: {model_name}"}

    print(json.dumps(result))

if __name__ == '__main__':
    main()
