public class MyClass {
    public static void main(String args[]) {
      
      int[][] data = {
          {1,2,6},
          {5,9,2},
          {7,1,4},
          {3,8,6}
      };
      
      for (int i = 0; i < data[i].length; i++){
          int total = 1;
          for(int j = 0; j < data.length; j++){
              total*= data[j][i];
          }
          System.out.println(total);
      }
    }
}
