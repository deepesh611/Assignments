package Java;

// Exercise 1

// Program to demosntrate the use of multiple threads

// public class Lab7 {
//     public static void main(String[] args) {
//         Thread t1 = new Thread(new Runnable() {
//             public void run() {
//                 for (int i = 0; i < 5; i++) {
//                     System.out.println("Hello from thread 1");
//                     try {
//                         Thread.sleep(1000);
//                     } catch (InterruptedException e) {
//                         System.out.println("An error occurred: " + e.getMessage());
//                         e.printStackTrace();
//                     }
//                 }
//             }
//         });

//         Thread t2 = new Thread(new Runnable() {
//             public void run() {
//                 for (int i = 0; i < 5; i++) {
//                     System.out.println("Hello from thread 2");
//                     try {
//                         Thread.sleep(1000);
//                     } catch (InterruptedException e) {
//                         System.out.println("An error occurred: " + e.getMessage());
//                         e.printStackTrace();
//                     }
//                 }
//             }
//         });

//         t1.start();
//         t2.start();
//     }    
// }

//----------------------------------------------------------------------------------------------------------------------------


// Exercise 2

// A program that shows the importance of synchronization in multithreading

// class Counter {
//     private int count = 0;

//     public synchronized void increment() {
//         count++;
//     }

//     public int getCount() {
//         return count;
//     }
// }

// class Lab7_2 {
//     public static void main(String[] args) {
//         Counter c = new Counter();

//         Thread t1 = new Thread(new Runnable() {
//             public void run() {
//                 for (int i = 0; i < 1000; i++) {
//                     c.increment();
//                 }
//             }
//         });

//         Thread t2 = new Thread(new Runnable() {
//             public void run() {
//                 for (int i = 0; i < 1000; i++) {
//                     c.increment();
//                 }
//             }
//         });

//         t1.start();
//         t2.start();

//         try {
//             t1.join();
//             t2.join();
//         } catch (InterruptedException e) {
//             System.out.println("An error occurred: " + e.getMessage());
//             e.printStackTrace();
//         }

//         System.out.println("Count: " + c.getCount());
//     }
// }

//----------------------------------------------------------------------------------------------------------------------------