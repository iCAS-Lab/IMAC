/*
    By Brendan C. Reidy
    Created 12/10/2019
    Last Modified 12/18/2019
    Main class. "Driver"
 */

public class Main {
    public static void main(String[] args) {
        ///*
        float[][] inputData = MatrixIO.readTrainingData("trainX.csv", 60000);
        float[][] outputData = MatrixIO.readTrainingData("trainY.csv", 60000);
        // approx alexnet
        NeuralNetwork network = new NeuralNetwork();
        network.setTrainingData(inputData, outputData);
        network.addLayer(new PlaceHolder2D(28, 28));
        network.addLayer(new Conv2D(96,11,1,"relu"));
        network.addLayer(new MaxPoolLayer(2,1));
        network.addLayer(new Conv2D(256,5,1,"relu"));
        network.addLayer(new MaxPoolLayer(2,1));
        network.addLayer(new Conv2D(384,3,1,"relu"));
        network.addLayer(new Conv2D(384,3,1,"relu"));
        network.addLayer(new Conv2D(256,3,1,"relu"));
        network.addLayer(new MaxPoolLayer(2,1));
        network.addLayer(new FullyConnectedBinary(1024, "Reverse Sigmoid"));
        network.addLayer(new FullyConnectedBinary(1024, "Reverse Sigmoid"));
        network.addLayer(new FullyConnectedBinary(10, "Reverse Sigmoid"));
        network.setInput(inputData[0]);
        System.out.println("Performing feedforward");
        network.feedForward();
        System.out.println("Done");
    }
}
