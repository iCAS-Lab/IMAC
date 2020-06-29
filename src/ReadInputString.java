import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadInputString {
    static String[][] readFromFile(String aFileName, int length)
    {
        if(aFileName==null)
        {
            System.out.println("[FATAL] Input file name is null");
            return null;
        }
        try {
            String[][] TrainingData = new String[length][2];
            System.out.println("Reading file: " + aFileName);
            Scanner fileScanner = new Scanner(new File(aFileName));
            int count = 0;
            String fileLine = fileScanner.nextLine();
            while(fileScanner.hasNext())
            {
                fileLine = fileScanner.nextLine();
                String[] splitLines = fileLine.split(",");
                String[] values = new String[2];
                values[0] = splitLines[1];
                values[1] = splitLines[2];
                if(count>=TrainingData.length) {
                    System.out.println("[WARNING] Reading stopped early. File is larger than specified");
                    break;
                }
                TrainingData[count] = values;
                count++;
            }
            fileScanner.close();
            return TrainingData;
        }catch(FileNotFoundException e){
            System.out.print("File '" + aFileName + "' does not exit");
        }catch (Exception e){
            System.out.println(e.getMessage());
        }
        return null;
    }
}
