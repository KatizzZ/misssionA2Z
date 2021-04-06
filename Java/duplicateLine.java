import java.io.*;
import java.lang.*;
import java.util.HashSet;

class Solution{
    public static void main(String[] args) throws IOException|FileNotFoundException{
        //input.txt output.txt
        BufferedReader br = new BufferedReader(new FileReader("input.txt"));
        PrintWriter pw = new PrintWriter("output.txt");
        HashSet<String> hs = new HashSet<String>();
        String line = br.readLine();
        while(line){
            if(hs.add(line)){
                pw.println(line);
            }
            line = br.readLine();
        }
        pw.flush();
        br.close();
        pw.close();
    }
    static void naive() throws Exception{
        BufferedReader br = new BufferedReader(new FileReader("input.txt"));
        PrintWriter pw = new PrintWriter("output.txt");
        String line = br.readLine();
        Boolean flag = false;
        while(line){
            BufferedReader br2 = new BufferedReader(new FileReader("output.txt"));
            String line2 = br2.readLine();
            flag = true;
            while(flag && line2){
                if(line.equals(line2))
                    flag = false;
                line2 = br2.readLine();
            }
            if(flag){
                pw.println(line);
                pw.flush()
            }
            line = br.readLine();
            br2.close();
        }
        br.close();
        pw.close();
    }
}