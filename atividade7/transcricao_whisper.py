import whisper
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import torch
from my_module import MyCustomClass

obj = MyCustomClass()

torch.serialization.add_safe_globals(MyCustomClass)

model = whisper.load_model("large")

result = model.transcribe("teste_whisper copy.mp3") 

print(result['text'])

'''template = """Transcrição: {question}

Resposta: ."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.2-vision:latest", max_tokens=100)

chain = prompt | model

chain.invoke({"question": result['text']})'''
