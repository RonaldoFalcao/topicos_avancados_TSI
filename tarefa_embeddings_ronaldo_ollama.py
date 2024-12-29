
import pandas as pd
import numpy as np
from langchain_community.embeddings import OllamaEmbeddings
from langchain_ollama import OllamaEmbeddings

# Cria um DataFrame com palavras sem categorias
palavras = ["Curso de graduação de Tecnologia em Sistemas para Internet - Modalidade a Distância"]

# Cria o DataFrame
df = pd.DataFrame({"Palavra": palavras})

# Define os documentos baseados nas palavras
documents = df["Palavra"].tolist()

# Define o modelo de embeddings
embeddings = OllamaEmbeddings(model="mxbai-embed-large")
document_embeddings = np.array(embeddings.embed_documents(documents))

# Mostra uma tabela com o nome e os embeddings
df["Embeddings"] = document_embeddings.tolist()
print(df[["Palavra", "Embeddings"]])

# Criar arquivo CSV com os embeddings
df.to_csv("embeddings.csv", index=False)

# Mostra o tamanho dos embeddings
embedding_size = len(document_embeddings[0])
print(f"Tamanho dos embeddings: {embedding_size}")

# Mostra o tipo dos embeddings
embedding_type = type(document_embeddings)
print(f"Tipo dos embeddings: {embedding_type}")