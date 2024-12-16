import os

os.environ["HF_DATASETS_CACHE"] = "/home/gxhe/models"
os.environ["HF_HOME"] = "/home/gxhe/models"
os.environ["HUGGINGFACE_HUB_CACHE"] = "/home/gxhe/models"
os.environ["HF_HUB_CACHE"] = "/home/gxhe/models"
# os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM


# download 9B-Chat-16K
# tokenizer = AutoTokenizer.from_pretrained("SparseLLM/sparsing-law-0.1b-relu")
# model = AutoModelForCausalLM.from_pretrained("SparseLLM/sparsing-law-0.1b-relu")
# print(f"hgx: model size = {model.num_parameters()}")

# del tokenizer
# del model

# download phi-3.5-mini-instruct
# tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3.5-mini-instruct", trust_remote_code=True)
# model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-3.5-mini-instruct", trust_remote_code=True)
# print(f"hgx: model size = {model.num_parameters()}")

# del tokenizer
# del model

# download Phi-3-mini-128k-instruct
# tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-128k-instruct", trust_remote_code=True)
# model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-3-mini-128k-instruct", trust_remote_code=True)
# print(f"hgx: model size = {model.num_parameters()}")

# del tokenizer
# del model

# download qwen2.5-0.5B
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B")
print(f"hgx: model size = {model.num_parameters()}")

del tokenizer
del model
