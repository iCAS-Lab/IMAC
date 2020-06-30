# In-Memory Analog Computing
In this project, we show how magnetic-random access memory (MRAM) technology can be utilized to implement synapses and neurons, and how they can realize an ultra high speed DNN circuit.

# Java Deep Neural Network Program
The Java DNN Program can be used to train models using Binary Neural Networks (BNN) and Ternary Neural Networks (TNN)

# Getting started
Download the src files as well as the training data found [here](https://drive.google.com/drive/folders/1J6ewbqCr7DQLb0cTMlcBu4TsGlBXPnEh?usp=sharing)

Once you have downloaded the src files and training data, you can create a new main file in any IDE to create a neural network, or you can use the sample main as a template

## Loading Files
Files in CSV format are loaded into two dimensional floating point arrays using the MatrixIO object
Example:
```
float[][] trainingData = MatrixIO.readTrainingData("FILE_NAME", NUM_LINES); // Loads csv file to trainingData variable
```


## Creating a Neural Network
In order to create a Neural Network, start by creating a Neural Network object:

```
NeuralNetwork network = new NeuralNetwork(); // Initializes object
```
Next you want to set the training and validation (test) data for the network:
```
network.setTrainingData(trainingData, trainLabels);
network.setTestingData(testingData, testLabels);
```
Next you can begin definining the topology of the Network. Start with the input layer:
```
network.addLayer(new Input2D(28, 28)); // Creates input layer; MNIST's dimensions are 28x28
```
Next you can begin defining the intermediate layers (you can define as many or as few as you like):
```
network.addLayer(new FullyConnectedBinary(16, "reverse sigmoid")); // Creates a hidden layer with 16 hidden neurons and uses 'reverse sigmoid' as the activation function (see 'Activation functions')
```
Next define the output layer:
```
network.addLayer(new FullyConnectedBinary(10, "reverse sigmoid")); // 10 neurons, reverse sigmoid activation
```

## Running a Neural Network
Now that the neural network hsa been created, you can run the network for one epoch with:
```
network.train();
```
Run for multiple epochs with:
```
for(int i=0; i<numEpochs; i++) {
    network.train();
}
```

## Getting accuracy
You can find the validation accuracy by adding the following line before running the train method:
```
network.addDatasetAnaylsisModel(new MaxOutputAccuracy());
```

## Saving results
You can save the neural network to a file using the following:
```
network.saveToFile("OUTPUT_DIRECTORY_NAME/");
```
This will auto generate a README with info about the network, a file with the training and validation cost over time, and all of the floating point and ternary/binary weights and biases throughout the network

## Activation functions
The in circuit Neural Network uses 'reverse sigmoid' as the activation function, which is why it is used in training as well.
