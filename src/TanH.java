public class TanH implements ActivationFunction {
    String name = "TanH";
    public float tanh(float x){
        return (float) (Math.tanh(x));
    }
    public float tanhError(float x){
        return (float) (1 - Math.tanh(x)*Math.tanh(x));
    }
    public float[] activate(float[] input)
    {
        for(int i=0; i<input.length; i++)
        {
            input[i] = tanh(input[i]);
        }
        return input;
    }
    public float[] activationError(float[] input)
    {
        for(int i=0; i<input.length; i++)
        {
            input[i] = tanhError(input[i]);
        }
        return input;
    }
    public String getName()
    {
        return name;
    }
    public String toString() { return  "Hyperbolic Tangent";}
}
