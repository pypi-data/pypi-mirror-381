import numpy as np

def Neural(num_inputs, num_hidden, num_outputs, inputs_list, targets_list, outputAnswer=1, Threshold=0.01, default_setting=0.25, lr=0.1, max_epochs=10000, print_every=500):
    # Convert inputs and targets
    inputs = np.array(inputs_list, dtype=float).reshape(-1, num_inputs)
    targets = np.array(targets_list, dtype=float).reshape(-1, num_outputs)
    
    # Random weight initialization
    W_inputs = np.random.uniform(-0.5, 0.5, (num_hidden, num_inputs))
    W_outputs = np.random.uniform(-0.5, 0.5, (num_outputs, num_hidden))
    B_hidden = np.random.uniform(-0.5, 0.5, num_hidden)
    B_output = np.random.uniform(-0.5, 0.5, num_outputs)
    
    # Training loop
    for epoch in range(max_epochs):
        # Forward pass
        hidden_raw = np.dot(inputs, W_inputs.T) + B_hidden
        hidden_activations = np.maximum(0, hidden_raw)  # ReLU
        outputs = np.dot(hidden_activations, W_outputs.T) + B_output
        
        # Loss (mean squared error)
        loss = np.mean((targets - outputs) ** 2)
        
        # Stop if loss is below threshold
        if loss < Threshold:
            break
        
        # Backpropagation
        error_output = outputs - targets
        grad_W_outputs = np.dot(error_output.T, hidden_activations) / inputs.shape[0]
        grad_B_output = np.mean(error_output, axis=0)
        
        error_hidden = np.dot(error_output, W_outputs) * (hidden_activations > 0)
        grad_W_inputs = np.dot(error_hidden.T, inputs) / inputs.shape[0]
        grad_B_hidden = np.mean(error_hidden, axis=0)
        
        # Update weights and biases
        W_outputs -= lr * grad_W_outputs
        B_output -= lr * grad_B_output
        W_inputs -= lr * grad_W_inputs
        B_hidden -= lr * grad_B_hidden
        
        # Optional progress printing
        if epoch % print_every == 0:
            print(f"Epoch {epoch}, Loss: {loss:.6f}, Outputs: {outputs}")
    
    # Success metrics
    if outputAnswer == 1:
        error = np.mean(np.abs(outputs - targets))
        max_val = np.max(np.abs(targets)) if np.max(np.abs(targets)) != 0 else np.max(np.abs(outputs))
        if max_val == 0:
            max_val = 1
        success_rate = max(0, min(100, 100 * (1 - (error / max_val))))
        print("\nFinal Outputs:\n", outputs)
        print("Targets:\n", targets)
        print(f"Average error: {error:.6f}")
        print(f"Success rate: {success_rate:.2f}%")
        return outputs, targets, success_rate
    else:
        return outputs, targets