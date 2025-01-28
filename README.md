# topicos_avancados_TSI
Repositório dedicado às atividades da disciplina Tópicos Avançados I do curso de TSI/IFRN

Atividade 3

Para executar corretamente o programa gerador de embeddings você precisará fazer primeiramente a instalação da ferramenta que permite rodar localmente os modelos de IA, essa ferramenta se chama Ollama e pode ser baixada em https://ollama.com/. Estamos usando o ollama 3.2.
Em seguida, você precisará baixar e instalar um modelo para geração embeddins, no nosso caso estamos usando modelo mxbai-embed-large, esse modelo está disponível em https://ollama.com/library/mxbai-embed-large e para instalação você deverá dar o seguinte comando no termnal de sua máquina 'ollama pull mxbai-embed-large'.
Além disso, usamos as bibliotecas Python pandas, numpy e langchain. Todas foram instaladas com o comando 'pip install nome_da_biblioteca'.

Atividade 7

Nesta atividade propõe-se um programa capaz de realizar transcrição de áudio e o texto transcrito ser tratado por um modelo de linguação capaz de interpretar o texto. Para transcrição foi usado o modelo Whisper e como modelo de linguagem para interpretação do texto gerado a partir do áudio foi usado o llama 3.2 vision. Ocorreram erros que não permitiram que o objetivo da transcrição fosse alcançado. 
