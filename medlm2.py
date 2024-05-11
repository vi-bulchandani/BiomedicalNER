import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("Henrychur/MMedLM2-1.8B", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("Henrychur/MMedLM2-1.8B", torch_dtype=torch.float16, trust_remote_code=True)
