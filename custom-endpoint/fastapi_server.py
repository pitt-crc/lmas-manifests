import os
from fastapi import FastAPI
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from pydantic import BaseModel

app = FastAPI()

# Define input structure using pydantic
class TextGenerationInput(BaseModel):
    prompt: str
    max_length: int = 250
    temperature: float = 0.1

if "MODEL_NAME" in os.environ:
    model_name = os.environ["MODEL_NAME"]
else:
    model_name = "meta-llama/Meta-Llama-3.1-8B"

@app.on_event("startup")
async def load_model():
    global model, tokenizer
    #print("Loading the LLaMA 3.1 8-bit model...")
    if "PRIVATE_REPO_TOKEN" in os.environ:
        access_token = os.environ["PRIVATE_REPO_TOKEN"]
    else:
        access_token = ""
    
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto",  # Automatically map layers to GPUs
        token = access_token
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name, token=access_token)
    print("Model loaded successfully!")


@app.post("/generate")
async def generate_text(input_data: TextGenerationInput):
    # Tokenize the input text
    inputs = tokenizer(input_data.prompt, return_tensors="pt").input_ids.cuda()

    # Generate output text using the model with the given parameters
    outputs = model.generate(
        inputs,
        max_length=input_data.max_length,
        temperature=input_data.temperature
    )

    # Decode and return the generated text
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"generated_text": generated_text}
