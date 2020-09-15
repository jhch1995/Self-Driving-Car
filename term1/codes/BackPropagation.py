import numpy as np

# Calculate sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.array([0.5, 0.1, -0.2]) # define three inputs
target = 0.6
learnrate = 0.5

# There are two hidden layers, so the matrix is 3 by 2.
weights_input_hidden = np.array([[0.5, -0.6],
                                 [0.1, -0.2],
                                 [0.1, 0.7]])

# There are one output layer, so the matrix is 2 by 1.
weights_hidden_output = np.array([0.1, -0.3])

# Forward pass
hidden_layer_input = np.dot(x, weights_input_hidden)
hidden_layer_output = sigmoid(hidden_layer_input)

output_layer_in = np.dot(hidden_layer_output, weights_hidden_output)
output = sigmoid(output_layer_in)

# Backwards pass
# Calculate error,（y-y^)
error = target - output

# Calculate error gradient for output layer,δ=（y-y^)* f’(∑iwixi),f’(h)=f(h)*(1-f(h))
del_err_output = error * output * (1 - output)

# Calculate error gradient for hidden layer
del_err_hidden = np.dot(del_err_output, weights_hidden_output) * \
                 hidden_layer_output * (1 - hidden_layer_output)

# Calculate change in weights for hidden layer to output layer
delta_w_h_o = learnrate * del_err_output * hidden_layer_output

# Calculate change in weights for input layer to hidden layer
delta_w_i_h = learnrate * del_err_hidden * x[:, None]

print('Change in weights for hidden layer to output layer:')
print(delta_w_h_o)
print('Change in weights for input layer to hidden layer:')
print(delta_w_i_h)
