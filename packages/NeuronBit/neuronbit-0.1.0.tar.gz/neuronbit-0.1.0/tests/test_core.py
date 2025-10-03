from neuronbit import activate, greet

def test_activate():
    assert round(activate(0), 2) == 0.5

def test_greet():
    assert "NeuronBit" in greet("Tester")
