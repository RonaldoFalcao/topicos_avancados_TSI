
import torch

class MyCustomClass:
    def __init__(self):
        print("MyCustomClass inicializada!")

# Certifique-se de que safe_globals seja uma lista
safe_globals = [MyCustomClass]

torch.serialization.add_safe_globals(safe_globals)