import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

class Perceptron:
    def __init__(self):
        self.weights = np.random.rand(2) # 2=input size
        self.bias = np.random.rand()

    def predict(self, x):
        return sigmoid(np.dot(x, self.weights) + self.bias)

    def train(self, X, y, epochs=1000, lr=0.1):
        for _ in range(epochs):
            for x, target in zip(X, y):
                error = target - self.predict(x)
                self.weights += lr * error * x
                self.bias += lr * error

X = np.array([[0,0],[0,1],[1,0],[1,1]])
Y = {"AND":[0,0,0,1], "OR":[0,1,1,1]}

for gate, y in Y.items():
    p = Perceptron()
    p.train(X, np.array(y))

    print(f"\n{gate} Gate")
    for x in X:
        print(x, "->", round(float(p.predict(x))))