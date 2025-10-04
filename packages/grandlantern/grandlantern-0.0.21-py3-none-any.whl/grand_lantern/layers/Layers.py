from grandlantern.matrix.Matrix import *
from grandlantern.layers.Activation import ActivationFunction


class Layer:
    parameters: list

    def __init__(self):
        self.parameters = []

    def get_parameters(self):
        return self.parameters

    def forward(self, X):
        pass

    def make_constant(self):
        for param in self.parameters:
            param.require_grad = False
        self.parameters = []
        return self

    def __str__(self):
        return f"Base Layer."


class LinearLayer(Layer):
    W: Matrix
    bias: Matrix
    n_neurons: int
    biased: bool
    activation: ActivationFunction

    def __init__(self, n_neurons, activation, biased=False):
        super().__init__()
        self.n_neurons = n_neurons
        self.activation = activation
        self.biased = biased
        self.W = None
        return

    def initialize_weights(self, n_inputs):
        self.W = Matrix.normal(shape=(n_inputs, self.n_neurons),
                               require_grad=True)
        self.parameters = [self.W]
        if self.biased:
            self.bias = Matrix.normal(shape=(1, self.n_neurons),
                                      require_grad=True)
            self.parameters = [self.W, self.bias]
        return

    def forward(self, X):
        if self.W is None:
            self.initialize_weights(X.shape[1])

        if self.biased:
            return self.activation(X @ self.W + self.bias)

        return self.activation(X @ self.W)

    def __str__(self):
        return f"Layer with n_neurons {self.n_neurons}, " \
               f"biased {self.biased}, " \
               f"activation {self.activation}."


class BatchNormLayer(Layer):
    gamma: Matrix
    beta: Matrix

    def __init__(self):
        super().__init__()
        self.gamma = None
        self.beta = None
        return

    def initialize_weights(self):
        self.gamma = Matrix(1., require_grad=True)
        self.beta = Matrix(0., require_grad=True)
        self.parameters = [self.gamma, self.beta]
        return

    def forward(self, X):
        if (self.gamma is None) or (self.beta is None):
            self.initialize_weights()

        mean = Matrix.mean(X, axis=0, keepdims=True)
        std = Matrix.std(X, axis=0, keepdims=True)

        X_normed = (X - mean) / (std ** 2 + 10e-3)

        return X_normed * self.gamma + self.beta

    def __str__(self):
        return f"Batch Norm Layer."


class Conv2DLayer(LinearLayer):
    kernel_size: np.array([int, int])
    dilation: np.array([int, int])

    def __init__(self, kernel_size, n_channels, activation, dilation=(1, 1), biased=False):
        super().__init__(n_channels, activation, biased)
        self.kernel_size = kernel_size
        self.dilation = dilation
        self.W = None
        return

    def initialize_weights(self, n_inputs):
        self.W = Matrix.normal(shape=(n_inputs, self.n_neurons, self.kernel_size[0], self.kernel_size[1]),
                               require_grad=True)
        self.parameters = [self.W]
        if self.biased:
            self.bias = Matrix.normal(shape=(self.n_neurons),
                                      require_grad=True)
            self.parameters = [self.W, self.bias]
        return

    def forward(self, X):
        if self.W is None:
            self.initialize_weights(X.shape[1])

        if self.biased:
            """
            need to fix
            """
            WX = Matrix.conv2d(X, self.W, self.dilation)
            for c in range(self.n_neurons):
                WX_bias = WX[:, c, :, :] + self.bias[c]

            return self.activation(WX_bias)

        return self.activation(Matrix.conv2d(X, self.W, self.dilation))

    def __str__(self):
        return f"Convolutional layer with kernel {self.kernel_size}, " \
               f"channels {self.n_neurons}, " \
               f"dilation {self.dilation}, " \
               f"biased {self.biased}, " \
               f"activation {self.activation}."


class RNNLayer(Layer):
    Wx: Matrix
    Wh: Matrix
    Wy: Matrix

    bias_h: Matrix
    bias_y: Matrix

    n_inner_neurons: int
    n_out_neurons: int
    biased: bool
    activation: ActivationFunction

    def __init__(self, n_inner_neurons, n_out_neurons, activation, biased=False):
        super().__init__()
        self.n_inner_neurons = n_inner_neurons
        self.n_out_neurons = n_out_neurons
        self.activation = activation
        self.biased = biased
        self.Wx = None
        self.Wh = None
        self.Wy = None
        return

    def initialize_weights(self, n_inputs):
        self.Wx = Matrix.normal(shape=(n_inputs, self.n_inner_neurons), require_grad=True)
        self.Wh = Matrix.normal(shape=(self.n_inner_neurons, self.n_inner_neurons), require_grad=True)
        self.Wy = Matrix.normal(shape=(self.n_inner_neurons, self.n_out_neurons), require_grad=True)
        self.parameters = [self.Wx, self.Wh, self.Wy]

        if self.biased:
            self.bias_h = Matrix.normal(shape=(1, self.n_inner_neurons), require_grad=True)
            self.bias_y = Matrix.normal(shape=(1, self.n_out_neurons), require_grad=True)
            self.parameters = [self.Wx, self.Wh, self.Wy, self.bias_h, self.bias_y]

    def forward(self, X):
        if self.Wx is None:
            self.initialize_weights(X.shape[1])

        h0 = Matrix.zeros(shape=(1, self.n_inner_neurons))
        H = [h0]
        Y = Matrix.zeros(shape=(X.shape[0], self.n_out_neurons))
        for i in range(X.shape[0]):
            if self.biased:
                Xi = X[i].reshape(shape=(1, -1))
                H.append(self.activation(Xi @ self.Wx + H[i] @ self.Wh + self.bias_h))
                Y[i] = H[i + 1] @ self.Wy + self.bias_y
            else:
                Xi = X[i].reshape(shape=(1, -1))
                H.append(self.activation(Xi @ self.Wx + H[i] @ self.Wh))
                Y[i] = H[i + 1] @ self.Wy
        return Y

    def __str__(self):
        return f"RNN Layer with n_inner_neurons {self.n_inner_neurons}, " \
               f"n_out_neurons {self.n_out_neurons}, " \
               f"biased {self.biased}, " \
               f"activation {self.activation}."


class FlattenLayer(Layer):
    input_shape: tuple

    def __init__(self):
        super().__init__()
        self.biased = False
        return

    def forward(self, X):
        self.input_shape = np.array(X.shape)
        X_reshaped = X.reshape(shape=(X.shape[0], np.prod(self.input_shape[1:])))
        return X_reshaped

    def __str__(self):
        return f"Flatten layer."
