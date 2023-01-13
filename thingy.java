import java.util.Scanner;
/* Online Java Compiler and Editor */
public class HelloWorld{

     public static void main(String []args){
         int[] data = {8,7,2,5,3,1};
         
        Scanner input = new Scanner(System.in);
        
        System.out.println("What number do you want to find");
        int num = input.nextInt();
        
        end:
        for (int i = 0; i < data.length; i++){
            for (int x = 0; x < data.length; x++){
                if (x == i){
                    break;
                }
                if (data[i] + data[x] == num){
                    System.out.println("Pair found at index " + i + " and " + x + " (" + data[i] + " + " + data[x] + ")");
                }
            }
        }
     }
}
