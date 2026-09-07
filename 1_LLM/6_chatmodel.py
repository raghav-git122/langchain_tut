from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id = "nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-NVFP4-DFlash",
    task = 'text-generation',
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("what is the capital of india?")
print(result.content)