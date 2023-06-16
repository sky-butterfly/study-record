import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class array {

    public static void main(String[] args){


        // 오름차순 정렬
        int[] arr = {1, 3, 5, 2, 4};
        Arrays.sort(arr);
        
        for( int a : arr ){
            System.out.print(a+", "); // 1, 2, 3, 4, 5,
        }

        System.out.println();

        // List 로 변환
        String[] strArr = {"a", "b", "c"};
        
        // 방법 1.
        List<String> strList = Arrays.asList(strArr);
        
        // 방법 2.
        strList = new ArrayList<>(Arrays.asList(strArr));

        // 방법 3.
        strList = Stream.of(strArr).collect(Collectors.toList());

        for(String s : strList){
            System.out.print(s+", "); // a, b, c,
        }

        System.out.println();

    }
}