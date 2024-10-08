// https://www.biko.kr/problem/1517

import java.io.*;

public class bi1517_2 {
    public static void main(String[] args) throws Exception {
        Reader reader = new InputStreamReader(System.in);
        while(true) {
            char c = (char)reader.read();
            if(c == '\n') break;
            System.out.print(c);
        }
        reader.close();

        System.out.println();
        System.out.println("Hello");
    }
}
