from inference_sdk import InferenceHTTPClient
from datetime import datetime
import pandas as pd
import os

CLIENT = InferenceHTTPClient(
    api_url="https://classify.roboflow.com",
    api_key="mNSQVrMCyYV4Cu7MFseO"
)

results = []

cages = ["Cage1", "Cage2", "Cage3"]

for cage in cages:

    for image in os.listdir(cage):

        image_path = os.path.join(cage, image)

        result = CLIENT.infer(
            image_path,
            model_id="my-first-project-twuzr/2"
        )

        results.append({
            "cage": cage,
            "image_id": image,
            "prediction": result["top"],
            "confidence": result["confidence"],
            "timestamp": datetime.now()
        })

        print(f"{cage} - {image} -> {result['top']}")

df = pd.DataFrame(results)

df.to_csv("fish_predictions.csv", index=False)

print("CSV Generated Successfully")