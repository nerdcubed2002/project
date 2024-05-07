import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("stabilityai/stable-code-3b")
model = AutoModelForCausalLM.from_pretrained("stabilityai/stable-code-3b", torch_dtype="auto")
model.cuda()

input_text = "import torch\nimport torch.nn as nn"
inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
tokens = model.generate(inputs, max_new_tokens=48, temperature=0.2, do_sample=True)
generated_code = tokenizer.decode(tokens[0], skip_special_tokens=True)

print(generated_code)
