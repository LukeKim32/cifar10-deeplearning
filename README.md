# cifar10-deeplearning
Simple deep learning project, using cifar 10, Keras, worked on Google Colab

This project is for studying machine learning features.

1. Gradient Descent
 We'll update parameters(weight, bias) by backpropagation
  => For better performance, SGD(Stochastic Gradient Descent) used

2. Activation function
 Step function => Sigmoid for Gradient
 But Sigmoid function can cause several problems
 
  1) Low learning speed
   As derivative of cost function(Whent it's Quadratic!) involves the derivative of activation function,
   the learning rate can be extremely low when the outcome of sigmoid function get close to 0 or 1
     => Change activation function to "Cross-entropy", which determines its learning speed upon model output
     
  2) Vanishing Gradient Problem
  The earlier layer, the lower learning speed the model might get, as the gradient involves the derivative of sigmoid
     => Change activation function to "ReLU"
     
     
3. Overfitting
  Model is trained but too much adaptive to training sets not normal inputs. Even an input that is slightly different 
  from training set can result in failure.
  => Data augmentation, Dropout, Ensemble etc
   => We can also use CNN(Convolutional Neural network)
   
4. CNN
  Use Convolutional layer to extract featrues (from abstract to specific) by using "Local receptive field" filter
  The result "Feature Map" is max pooled
  and this process is iterated.
  After this, these feature maps are flattened for fully-connected layer
  but to prevent Overfitting, we can drop out some neurons (normally about 0.25)
  For the output layer, we can use "Soft-max" function to get relative outcome among all outcomes.
