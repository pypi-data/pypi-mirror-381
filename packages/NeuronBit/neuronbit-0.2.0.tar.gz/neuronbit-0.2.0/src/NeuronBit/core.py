import numpy as np

def Neural(num_inputs, num_hidden, num_outputs, inputs_list, targets_list, default_setting=0.25):
    # Convert given lists into numpy arrays
    inputs = np.array(inputs_list, dtype=float)   # shape: (samples, features)
    targets = np.array(targets_list, dtype=float) # shape: (samples, outputs)

    # --------------- Biases (default = 0.25) ---------------
    B_hidden = np.full((num_hidden,), default_setting)              # shape: (hidden,)
    B_output = np.full((num_outputs,), default_setting)             # shape: (outputs,)

    # --------------- Weights (default = 0.25) ---------------
    W_inputs = np.full((num_hidden, num_inputs), default_setting)   # shape: (hidden × inputs)
    W_outputs = np.full((num_outputs, num_hidden), default_setting) # shape: (outputs × hidden)

    # --------------- Forward Pass (Vectorized) ---------------
    # Hidden layer: (samples × inputs) · (inputs × hidden)ᵀ → (samples × hidden)
    hidden_raw = np.dot(inputs, W_inputs.T) + B_hidden
    hidden_activations = np.maximum(0, hidden_raw)  # ReLU applied elementwise

    # Output layer: (samples × hidden) · (hidden × outputs)ᵀ → (samples × outputs)
    outputs = np.dot(hidden_activations, W_outputs.T) + B_output

    return outputs, targets