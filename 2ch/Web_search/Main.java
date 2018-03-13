package com.company;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;
import java.util.regex.*;
import java.io.*;
public class Main
{
    public static void main(String[] args) throws Exception
    {
        System.out.println("in");
        FileReader fr=new FileReader("link.txt");
        BufferedReader br=new BufferedReader(fr);
        String line;

        String dir_name="sources";
        File dir_file = new File(dir_name);	  /*路徑跟檔名*/
        dir_file.mkdir();

        int index=0;
        while((line=br.readLine())!=null)
        {
            String f_name=dir_name + "/source" + index + ".txt";
            System.out.println("from " + line + '\n');
            FileWriter fw = new FileWriter(f_name);
            BufferedWriter bw = new BufferedWriter(fw);
            bw.write(line);
            bw.newLine();
            Document doc;

            try
            {
                java.net.URL url = new java.net.URL(line);
                doc = Jsoup.parse(url, 10000);
            }
            catch (Exception ex)
            {
                System.out.println(line + "發生錯誤");
                continue;
            }

            Elements board=doc.select("a[target=body]");  //how many page


            for(int i=0;i<board.size();++i)
            {

                String get_s = board.get(i).attr("href");
                Pattern pattern=Pattern.compile(".*(/test.*).{3}"); //  ex: ../test/read.cgi/namazuplus/1486431967/
                Matcher matcher=pattern.matcher(get_s);

                if(matcher.find())
                {
                    get_s=matcher.group(1);
                    pattern=Pattern.compile("(http.//.*)/.*/");  // ex: http://potato.2ch.net/namazuplus/
                    matcher = pattern.matcher(line);
                    matcher.find();

                    bw.write(matcher.group(1)+get_s); // ex: http://potato.2ch.net/test/read.cgi/namazuplus/1486431967/
                    bw.newLine();
                }

            }
            bw.flush();
            bw.close();
            index++;
        }
    }
}
