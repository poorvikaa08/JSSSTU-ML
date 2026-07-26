# Write a Program to develop simple single layer perceptron to implement AND, OR Boolean functions. 

import numpy as np

# Sigmoid activation function
# Converts any value into a number between 0 and 1
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Function to train the perceptron
def train_perceptron(X, y):

    w = np.random.rand(2)
    b = np.random.rand()

    for _ in range(1000):
        for i in range(len(X)):

            # Output = sigmoid(X.W + b)
            out = sigmoid(np.dot(X[i], w) + b)

            # prediction error
            error = y[i] - out

            # New Weight = Old Weight + Learning Rate × Error × Input
            w += 0.1 * error * X[i]

            # Update bias
            b += 0.1 * error

    # Return learned weights and bias
    return w, b

X = np.array([[0,0],[0,1],[1,0],[1,1]])


y_and = np.array([0, 0, 0, 1])
y_or = np.array([0, 1, 1, 1])

w1, b1 = train_perceptron(X, y_and)
w2, b2 = train_perceptron(X, y_or)

print("AND Gate")

for x in X:
    output = sigmoid(np.dot(x, w1) + b1)   # Predict output
    print(x, "->", round(output)) # Round to 0 or 1


print("\nOR Gate")

for x in X:
    output = sigmoid(np.dot(x, w2) + b2)
    print(x, "->", round(output))
    
    
    
    
    
    
# class Perceptron:
#     def __init__(self):
#         self.weights = np.random.rand(2) # 2=input size
#         self.bias = np.random.rand()

#     def predict(self, x):
#         return sigmoid(np.dot(x, self.weights) + self.bias)

#     def train(self, X, y, epochs=1000, lr=0.1):
#         for _ in range(epochs):
#             for x, target in zip(X, y):
#                 error = target - self.predict(x)
#                 self.weights += lr * error * x
#                 self.bias += lr * error

# X = np.array([[0,0],[0,1],[1,0],[1,1]])
# Y = {"AND":[0,0,0,1], "OR":[0,1,1,1]}

# for gate, y in Y.items():
#     p = Perceptron()
#     p.train(X, np.array(y))

#     print(f"\n{gate} Gate")
#     for x in X:
#         print(x, "->", round(float(p.predict(x))))