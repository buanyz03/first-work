package com.company;


import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;
import java.util.HashSet;
import java.util.Set;
import java.util.regex.*;
import org.json.*;
import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        Set<Character.UnicodeBlock> japaneseUnicodeBlocks = new HashSet<Character.UnicodeBlock>() {{
            add(Character.UnicodeBlock.HIRAGANA);
            add(Character.UnicodeBlock.KATAKANA);
            add(Character.UnicodeBlock.CJK_UNIFIED_IDEOGRAPHS);
        }};


        String folderPath = "sources";//資料夾路徑
        java.io.File folder = new java.io.File(folderPath);
        String[] list = folder.list();


        for (int c =42; c <=42; ++c) {

            String s_name=folderPath + "/source" + c + ".txt";
            FileReader fr = new FileReader(s_name);
            BufferedReader br = new BufferedReader(fr);
            br.readLine();

            String d_name="source" + c;
            int index=0;
            File dir_file = new File(d_name);
            dir_file.mkdir();  //create folder

            String line;
            while ((line = br.readLine()) != null) {

                String f_name = d_name + "/output" + index + ".json";
                File file = new File(f_name);
                BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file, false), "UTF-8"));
                String Title = "";

                JSONObject J_all;
                JSONObject J_title;
                JSONArray J_name;
                JSONArray J_context;

                J_all = new JSONObject();
                J_title = new JSONObject();
                J_context = new JSONArray();
                J_name = new JSONArray();

                J_all.put("Url", line);
                System.out.println("from " + line + '\n');
                Document doc;

                try {
                    java.net.URL url = new java.net.URL(line);
                    doc = Jsoup.parse(url, 10000);
                } catch (Exception ex) {
                    System.out.println(line + "發生錯誤");
                    continue;
                }

                Elements titles = doc.select("title");
                String get_s = titles.get(0).text();
                for (char ch : get_s.toCharArray()) {
                    if (japaneseUnicodeBlocks.contains(Character.UnicodeBlock.of(ch))) {
                        Title = get_s;
                        break;
                    }
                }

                Elements names = doc.select("dt>a,dt>font,div[class=name]");
                Elements dates = doc.select("dt,div[class=date]");
                Elements messages = doc.select("dd,div[class=message]");


                boolean is_NG;
                boolean title_create = false;
                for (int i = 0; i < messages.size(); ++i) {
                    Pattern pattern = Pattern.compile("([0-9]{4}/[0-9]{2}/[0-9]{2}).*");
                    Matcher matcher = pattern.matcher(dates.get(i).text());

                    is_NG = !matcher.find();
                    if (is_NG) {
                        continue;
                    }
                    if (!title_create) {
                        J_title.put("Title", Title);
                        J_title.put("date", matcher.group(1));
                        title_create = true;
                    }

                    JSONObject Name = new JSONObject();
                    Name.put("name", names.get(i).text());
                    Name.put("date", matcher.group(1));
                    J_name.put(Name);

                    JSONObject context = new JSONObject();
                    context.put("context", messages.get(i).text());
                    context.put("date", matcher.group(1));
                    J_context.put(context);

                }

                J_all.put("context_array", J_context);
                J_all.put("title", J_title);
                J_all.put("name_array", J_name);

                bw.write(J_all.toString());
                bw.flush();
                bw.close();
                index++;

            }
        }
    }
}
