from llama_cpp import Llama
import json

prompt = input('Prompt????????')

# Load the model - change the path to where you saved the file
llm = Llama(
    model_path="yourModelName.gguf",
    n_ctx=2048, #Context window..
    n_threads=4,
    verbose=False,
)

# Simple test
response = llm(
    f"<|user|>\n{prompt}<|end|>\n<|assistant|>",
    max_tokens=1000, # Maximum nr of tokens on response!
    stop=["Q:", "\n"],
)

print(response["choices"][0]["text"])
#print(json.dumps(response, indent=2))
