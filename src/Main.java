/*
    By Brendan C. Reidy
    Created 12/10/2019
    Last Modified 12/18/2019
    Main class. "Driver"
 */

public class Main {
    public static void main(String[] args) {
        int numEpochs = 3;
        float[][] trainingData = MatrixIO.readTrainingData("trainX.csv", 60000);
        float[][] testingData = MatrixIO.readTrainingData("testX.csv", 10000);
        float[][] trainLabels = MatrixIO.readTrainingData("trainY.csv", 60000);
        float[][] testLabels = MatrixIO.readTrainingData("testY.csv", 10000);

        NeuralNetwork network = new NeuralNetwork();
        network.setTrainingData(trainingData, trainLabels);
        network.setTestingData(testingData, testLabels);
        network.addLayer(new Input2D(28, 28));
        network.addLayer(new FullyConnectedBinary(16, "reverse sigmoid"));
        network.addLayer(new FullyConnectedBinary(16, "reverse sigmoid"));
        network.addLayer(new FullyConnectedBinary(10, "reverse sigmoid"));
        network.setLearningRate(0.1f);
        network.addDatasetAnaylsisModel(new MaxOutputAccuracy());

        for(int i=0; i<numEpochs; i++) {
            network.train();
            network.saveToFile("TernaryReverseSigmoid/");
        }
    }

    public static int fromOneHotToNumber(float[] oneHot)
    {
        for(int i=0; i<oneHot.length; i++)
        {
            if(oneHot[i]==1)
                return i;
        }
        return -1;
    }
}
