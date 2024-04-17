package Java;

// EXERCISE - 1
// Try, catch, and finally block

// public class Lab5 {
//     public static void main(String[] args){
//         int[] arr = {1, 2, 3, 4, 5};
//         try{
//             for (int i = 0; i <= arr.length; i++){
//                 System.out.println(arr[i]);
//             }
//         } 
        
//         catch (ArrayIndexOutOfBoundsException e){
//             System.out.println("Array index out of bound exception");
//         } 
        
//         finally {
//             System.out.println("Finally block executed");
//         }
//     }
// }


// ------------------------------------------------------------------------------------------------------------------------------------------------


// EXERCISE - 2

// custom exception

// class CustomException extends Exception {
//     public CustomException(String s){
//         super(s);
//     }
// }

// public class Lab5 {
//     public static void main(String[] args){
//         try{
//             throw new CustomException("This is a custom exception");
//         } 
        
//         catch (CustomException e){
//             System.out.println("Caught");
//             System.out.println(e.getMessage());
//         }
//     }
// }


// ------------------------------------------------------------------------------------------------------------------------------------------------