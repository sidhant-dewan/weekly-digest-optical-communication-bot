from llama_cpp import Llama

llm = Llama(
    model_path="models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",
    n_ctx=4096,
    n_threads=8,
    verbose=False
)

def run_llm(prompt: str) -> str:
    output = llm(
        prompt,
        max_tokens=512,
        temperature=0.1,
        stop=["}\n\n", "\n\n", "</json>"]
    )
    return output["choices"][0]["text"]
