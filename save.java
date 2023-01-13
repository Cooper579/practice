/* Online Java Compiler and Editor */
public class HelloWorld{

     public static void main(String []args){
        int[] data = {6,0,8,2,3,0,4,0,1};
        
        for (int i = 0; i < data.length; i++){
            if (data[i] == 0){
                for (int g = i; g < data.length; g++){
                    if (g == (data.length - 1)){
                        break;
                    }
                    else{
                        data[g] = data[g+1]; 
                    }
                }
                data[data.length - 1] = 0;
            }
        }
        
        for(int i = 0; i < data.length; i ++){
            System.out.print(data[i] + ", ");
        }
     }
}
