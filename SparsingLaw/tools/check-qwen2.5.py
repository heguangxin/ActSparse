import os

os.environ["HF_DATASETS_CACHE"] = "/home/gxhe/models"
os.environ["HF_HOME"] = "/home/gxhe/models"
os.environ["HUGGINGFACE_HUB_CACHE"] = "/home/gxhe/models"
os.environ["HF_HUB_CACHE"] = "/home/gxhe/models"
# os.environ["CUDA_VISIBLE_DEVICES"] = "0"

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

# download qwen2.5-0.5B
# tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B")
# model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B")
# print(f"hgx: model size = {model.num_parameters()}")

# print(type(model))

# del tokenizer
# del model

import transformers.models.qwen2.modeling_qwen2 as qwen2_module
from transformers.models.qwen2.modeling_qwen2 import Qwen2MLP
module_path = qwen2_module.__file__

print(f"Qwen2ForCausalLM 的源码文件路径是: {module_path}")
# from transformers import Seq2SeqTrainer
# module_path = qwen2_module.__file__

# for name, module in model.named_modules():
#     print(name)
#     continue
#     if name.endswith('mlp'):
#         assert(isinstance(module, Qwen2MLP))
#         layer_id = int(name.split('.')[2])
#         setattr(module, 'layer_id', layer_id)
#         print(name)

from transformers import Seq2SeqTrainer
import inspect
import os

print(f"Seq2SeqTrainer 的源码文件路径是: {inspect.getfile(Seq2SeqTrainer)}")