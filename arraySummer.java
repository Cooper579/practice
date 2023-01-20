public class MyClass {
    public static void main(String args[]) {
        int[][] thingy = {{1,2,6},{5,9,2},{7,1,4},{3,8,6}};
        MyClass.calculateRowSums(thingy);
    }
    public static void calculateRowSums(int[][] array){
        for (int i = 0; i < array.length; i ++){
            int sum = 0;
            for(int x = 0; x < array[0].length; x ++){
                sum+=array[i][x];
            }
            System.out.println(sum);
        }
    }
}
