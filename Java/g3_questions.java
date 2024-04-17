
package Java;


// // A program to create a simple java calculator

// public class g3_questionss {
//     public static void main(String[] args) {
//         Scanner input = new Scanner(System.in);
//         System.out.println("Enter the first number: ");
//         int num1 = input.nextInt();
//         System.out.println("Enter the second number: ");
//         int num2 = input.nextInt();
//         System.out.println("Enter the operator: ");
//         char operator = input.next().charAt(0);
//         input.close();
//         int result = 0;
//         switch (operator) {
//             case '+':
//                 result = num1 + num2;
//                 break;
//             case '-':
//                 result = num2 - num1;
//                 break;
//             case '*':
//                 result = num1 * num2;
//                 break;
//             case '/':
//                 result = num2 / num1;
//                 break;
//             default:
//                 System.out.println("Invalid operator");
//         }
//         System.out.println("The result is: " + result);
//     }
// }




// // A Java Program for fibonacci series

// public class g3_questionss {
//     public static void main(String[] args) {
//         Scanner input = new Scanner(System.in);
//         System.out.println("Enter the number of terms: ");
//         int num = input.nextInt();
//         input.close();
//         int a = 0;
//         int b = 1;
//         int c;
//         System.out.println("The fibonacci series is: ");
//         System.out.print(a + " " + b);
//         for (int i = 2; i < num; i++) {
//             c = a + b;
//             System.out.print(" " + c);
//             a = b;
//             b = c;
//         }
//     }
// }



// // A Java Program to find the factorial of a number

// public class g3_questionss {
//     public static void main(String[] args) {
//         Scanner input = new Scanner(System.in);
//         System.out.println("Enter the number: ");
//         int num = input.nextInt();
//         input.close();
//         int fact = 1;
//         for (int i = 1; i <= num; i++) {
//             fact = fact * i;
//         }
//         System.out.println("The factorial of " + num + " is: " + fact);
//     }
// }


// // A Java Program to check whether a number is prime or not

// public class g3_questionss {
//     public static void main(String[] args) {
//         Scanner input = new Scanner(System.in);
//         System.out.println("Enter the number: ");
//         int num = input.nextInt();
//         input.close();
//         boolean flag = false;
//         for (int i = 2; i <= num / 2; i++) {
//             if (num % i == 0) {
//                 flag = true;
//                 break;
//             }
//         }
//         if (!flag) {
//             System.out.println("The number is prime");
//         } else {
//             System.out.println("The number is not prime");
//         }
//     }
// }


