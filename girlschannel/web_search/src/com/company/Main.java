package com.company;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

import javax.swing.plaf.synth.SynthEditorPaneUI;
import java.util.regex.*;
import java.io.*;
public class Main
{
    public static void main(String[] args) throws Exception
    {
        FileReader fr=new FileReader("category.txt");
        BufferedReader br=new BufferedReader(fr);
        String line;

        String dir_name="sources";
        File dir_file = new File(dir_name);	  /*路徑跟檔名*/
        dir_file.mkdir();

        while((line=br.readLine())!=null)
        {
            String[] tokens = line.split(" ");
            String title=tokens[0];
            String link=tokens[1];

            link+="1";

            String f_name=dir_name + "/" + title + ".txt";
            System.out.println("from " + link  + '\n');

            FileWriter fw = new FileWriter(f_name);
            BufferedWriter bw = new BufferedWriter(fw);

            boolean finish=true;
            while(finish)
            {
                Document doc;
                try
                {
                    java.net.URL url = new java.net.URL(link);
                    doc = Jsoup.parse(url, 10000);
                }
                catch (Exception ex)
                {
                    System.out.println("發生錯誤");
                    continue;
                }

                Elements all_P = doc.select("li[class=\"flc\"]");
                for(int i=0; i<all_P.size();++i)
                {
                    Elements get_link= all_P.get(i).select(">a");
                    String L=get_link.attr("href");
                    L="http://girlschannel.net"+L;
                    bw.write(L);
                    bw.newLine();
                }
                bw.flush();
                Elements next = doc.select("link[rel=\"next\"]");
                if(next==null)
                {
                    finish=false;
                }
                link=next.attr("href");
                System.out.println(link);
            }

            bw.close();
        }
    }
}
