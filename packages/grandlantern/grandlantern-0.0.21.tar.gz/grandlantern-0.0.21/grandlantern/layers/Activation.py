import numpy as np
from grandlantern.matrix.Matrix import Matrix


class ActivationFunction:

    def __call__(self, X):
        pass

    def __str__(self):
        return f"Base"


class Linear(ActivationFunction):

    def __call__(self, X):
        return X

    def __str__(self):
        return f"Linear"


class Sigmoid(ActivationFunction):

    def __call__(self, X):
        sigmoid = Matrix.sigmoid(X)
        return sigmoid

    def __str__(self):
        return f"Sigmoid"


class Tanh(ActivationFunction):

    def __call__(self, X):
        tanh = Matrix.tanh(X)
        return tanh

    def __str__(self):
        return f"Tanh"


class ReLU(ActivationFunction):

    def __call__(self, X):
        return Matrix.relu(X)

    def __str__(self):
        return f"ReLU"


class LReLU(ActivationFunction):
    alpha: float

    def __init__(self, alpha=0.01):
        self.alpha = alpha

    def __call__(self, X):
        return Matrix.lrelu(X, alpha=self.alpha)

    def __str__(self):
        return f"LReLU"


class PReLU(ActivationFunction):
    p_alpha: Matrix

    def __init__(self):
        self.p_alpha = Matrix.uniform(shape=(1), low=0, high=1., require_grad=True)

    def __call__(self, X):
        return Matrix.lrelu(X, alpha=self.p_alpha)

    def __str__(self):
        return f"PReLU"


class SiLU(ActivationFunction):

    def __call__(self, X):
        return X * Matrix.sigmoid(X)

    def __str__(self):
        return f"SiLU"


class SoftMax(ActivationFunction):

    def __call__(self, X):
        return Matrix.safe_softmax(X)

    def __str__(self):
        return f"SoftMax"
