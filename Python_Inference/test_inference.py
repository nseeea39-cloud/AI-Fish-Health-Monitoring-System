from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://classify.roboflow.com",
    api_key="mNSQVrMCyYV4Cu7MFseO"
)

result = CLIENT.infer(
    "fresh_455.png",
    model_id="my-first-project-twuzr/2"
)

print(result)