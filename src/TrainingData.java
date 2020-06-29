import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

public class TrainingData {

    public static String imageToCSV(BufferedImage img)
    {
        int maxValue = 255;
        String ret = "";
        for(int x = 0; x<img.getWidth(); x++)
        {
            for(int y = 0; y < img.getHeight(); y++)
            {
                int value = img.getRGB(x, y);
                Color color = new Color(value);
                float avg = (float) (color.getRed() + color.getGreen() + color.getBlue()) / 3.0f;
                ret += ((avg) / (float) maxValue) + ",";
            }
        }
        return ret;
    }
}
