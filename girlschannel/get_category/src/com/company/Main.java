package com.company;
import org.jsoup.*;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

import java.util.*;
import java.io.*;
public class Main {

    public static void main(String[] args) throws Exception
    {
        Document doc=null;
        String index = "http://girlschannel.net";
        try
        {
            java.net.URL url= new java.net.URL(index);
            doc=Jsoup.parse(url,1000);
        }
        catch (Exception e)
        {
            System.out.println( "發生錯誤");
        }

        String f_name="category.txt";
        FileWriter fw = new FileWriter(f_name);
        BufferedWriter bw = new BufferedWriter(fw);


        Elements board = doc.select("ul[class=\"category flc\"]"); //how many page 
        Elements pages = board.select("a");
        for(int i=0;i < pages.size(); ++i)
        {
            String link = pages.get(i).attr("href");
            String title = pages.get(i).text();
            link = index + link;
            bw.write(title + " " + link);
            bw.newLine();
        }
        bw.flush();
        bw.close();

    }
}
