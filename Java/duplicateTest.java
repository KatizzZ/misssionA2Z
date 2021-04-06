import java.io.*;
import java.lang.*;
import java.util.*;

class Solution{
    public static void main(String[] args) throws IOException{
        String inputPath = args[0];
        String outputPath = args[1];
        BufferedReader br = new BufferedReader(new FileReader(inputPath));
        Set<String> hs = new HashSet<String>();
        List<String> dupList = New ArrayList<String>();

        String line = br.readLine();
        while(line!=null){
            if(hs.add(line)){
                dupList.add(line);
            }
            line = br.readLine();
        }
        br.close();
        writeDuplicate(dupList,outputPath);
        // pw.flush();
        // PrintWriter pw = new PrintWriter(outputPath);
        // pw.close();
    }
    public static void writeDuplicate(ArrayList<String> dupList, String outputPath) throws IOException{
        FileWriter fw = new FileWriter(outputPath);
        for(String str: dupList){
            fw.write(str);
        }
        fw.close();
    }
}