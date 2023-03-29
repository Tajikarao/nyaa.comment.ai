# nyaa.comment.ai

This Discord bot provides a prediction (positive/negative) for a comment from a user of Nyaa, a torrent file sharing platform. The prediction model is based on a neural network using the TensorFlow library.

## Usage
The bot can be used by using the /comment command on Discord. This command retrieves a random comment from Nyaa and displays a prediction for that comment. The user can then validate or invalidate the prediction by clicking on the "Positive" or "Negative" buttons. This validation is used to train the prediction model and improve the results.

## Code
The code is divided into several files located in the utils folder. The file model.py contains the Model class, which manages the prediction model and the training of the neural network. The file nyaa.py contains the Nyaa class, which handles the scraping of comments from Nyaa. The singleton.py file contains a utility class for implementing a singleton in Python.

The main app.py file creates a Discord bot using the py-cord library. It also defines a btnView class to create user interaction buttons, and a create_embed function to generate embed messages for comments.

## Dependencies
The code uses the following libraries:

1. py-cord (for interaction with Discord)
2. TensorFlow and Keras (for the prediction model and neural network training)
Configuration

The bot requires an API key to access the Discord API. This key must be placed at the end of the app.py file in the bot.run() function.



# Model

The model is an artificial neural network with three dense layers:

1. The first layer is a dense layer of 64 neurons with a **ReLU** activation function.

2. The second layer is a dense layer of 3 neurons with a **Softmax** activation function, which allows the data to be classified into several categories.

3. The third layer is a dense layer of 1 neuron with a **sigmoid** activation function, which predicts a continuous probability value in the interval [0,1].

4. The model is trained with the **Adam** algorithm which is a very efficient and popular stochastic gradient descent algorithm. The optimisation of this model is done using the binary loss function binary_crossentropy, which measures the difference between the predictions and the actual values. The evaluation metric of the model is accuracy.

# ReLu activation function

The **ReLU** (Rectified Linear Unit) activation function is a mathematical function widely used in artificial neural networks. It is often used as an activation function for hidden layers because it is simple, fast to compute and efficient in solving many problems.

The ReLU function is defined as follows:

> ```f(x) = max(0, x)```

This means that if the value of the input x is negative, the output of the function is 0, and if the value of x is positive, the output of the function is equal to x.

The ReLU function has several advantages. It is simple and does not require an exponential calculation, which makes it faster to calculate than other activation functions. It is also non-linear, which allows the model to solve complex problems by learning non-linear relationships between the input data and the expected output.

Finally, the ReLU function also solves the problem of gradient loss that can occur in deep neural networks. It keeps the information positive and the gradient non-zero for the neurons in the hidden layer, which facilitates learning and model optimisation.

# Softmax activation function

The **Softmax** activation function is a mathematical function that takes a vector of numbers and returns a new vector of the same dimension, where each element is between 0 and 1 and the sum of all elements is 1.

The softmax function is often used in artificial neural networks to calculate the probability of each class. It is used to obtain a probabilistic classification output from the last layer of a neural network.

The softmax function is very useful because it allows a neural network output to be transformed into probabilities, which greatly facilitates the interpretation of the results. It is commonly used in multi-class classification tasks, where there are several possible classes for each example and each example can only belong to one class.

# sigmoid activation function

The **sigmoid** activation function is a mathematical function that takes as input any real number and returns a value in the interval [0,1]. It is commonly used as an activation function for binary neural networks that perform binary classification (for example, predicting whether an image shows a cat or a dog).

The **sigmoid** function transforms the input values into a value between 0 and 1, which can be interpreted as the probability that the input belongs to the positive class in a binary classification problem. The larger the input value, the closer the output is to 1 and the higher the probability of belonging to the positive class. Conversely, the smaller the input value, the closer the output is to 0 and the greater the probability of belonging to the negative class.