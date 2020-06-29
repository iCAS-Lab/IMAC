import java.util.LinkedList;

public class MaxOutputAccuracy implements DatasetAnalysis {
    LinkedList<Float> allAccuracy;
    float bestAccuracy = 0;
    float currentAccuracy = 0;
    int currentEpoch = 0;
    int currentCount = 0;
    public MaxOutputAccuracy(){
        this.allAccuracy = new LinkedList<>();
    }
    public void startEpoch()
    {
        currentCount = 0;
        currentAccuracy = 0;
        currentEpoch++;
    }
    public void analyzeLayer(float[] aLayer, float[] correctOutput)
    {
        float[] newOutput = new float[aLayer.length];
        int maxIndex = 0;
        for(int i=1; i<newOutput.length; i++)
            if(aLayer[i] > aLayer[maxIndex])
                maxIndex = i;
        newOutput[maxIndex] = 1;
        if(correctOutput[maxIndex]!=1)
            currentAccuracy+=1;
        currentCount++;
    }
    public void printResults()
    {
        float accuracy = 1 - (this.currentAccuracy / (float) currentCount);
        allAccuracy.add(accuracy);
        if(accuracy > bestAccuracy)
            bestAccuracy = accuracy;
        System.out.print("\tMaxOutAcc: " + accuracy);
    }
    public void saveToFile(String aFileName)
    {
        MatrixIO.saveToFile(allAccuracy, aFileName + "MaxOutAccuracy.txt");
    }
    public String appendToReadMe()
    {
        return "\tMax Output Accuracy\n\t   Best Accuracy: " + bestAccuracy;
    }
}
