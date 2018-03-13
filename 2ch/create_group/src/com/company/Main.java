package com.company;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;
import java.util.regex.*;
import java.io.*;
public class Main
{
    public static void main(String[] args) throws Exception {

        Document doc = null;
        try {
            java.net.URL url = new java.net.URL("http://menu.2ch.net/bbsmenu.html");
            doc = Jsoup.parse(url, 10000);
        } catch (Exception ex) {
            System.out.println("發生錯誤");
        }

        Elements board = doc.select("A");
        String f_name="category.txt";

        FileWriter fw = new FileWriter(f_name);
        BufferedWriter bw = new BufferedWriter(fw);

        for (int i = 0; i < board.size(); ++i)
        {
            String s = board.get(i).attr("HREF");
            bw.write(s + "\n");
            System.out.println(s + "\n\n");
        }
    }

}
