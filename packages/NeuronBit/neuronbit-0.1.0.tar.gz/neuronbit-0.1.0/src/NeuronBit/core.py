def activate(x: float) -> float:
    """Simple sigmoid activation function"""
    import math
    return 1 / (1 + math.exp(-x))

def greet(name: str) -> str:
    return f"Welcome to NeuronBit, {name}! 🧠⚡"