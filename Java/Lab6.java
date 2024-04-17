package Java;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

//----------------------------------------------------------------------------------------------------------------------------

// Exercise 1

// class ReadFile {
//     private String filePath;
//     public ReadFile(String filePath) {
//         this.filePath = filePath;
//     }

//     public String read() throws IOException {
//         StringBuilder content = new StringBuilder();
//         try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
//             String line;
//             while ((line = reader.readLine()) != null) {
//                 content.append(line).append("\n");
//             }
//         }
//         return content.toString();
//     }
// }

// class WriteFile {
//     private String filePath;
//     public WriteFile(String filePath) {
//         this.filePath = filePath;
//     }

//     public void write(String content) throws IOException {
//         try (FileWriter writer = new FileWriter(filePath)) {
//             writer.write(content);
//         }
//     }
// }

// public class Lab6 {
//     public static void main(String[] args) {
//         String file = ".\\Java\\file1.txt";
//         String file2 = ".\\Java\\file2.txt";
//         try {
//             ReadFile read = new ReadFile(file);
//             String content = read.read();
//             WriteFile write = new WriteFile(file2);
//             write.write(content);
//             System.out.println("File copied successfully.");
//         } catch (IOException e) {
//             System.out.println("An error occurred: " + e.getMessage());
//             e.printStackTrace();
//         }
//     }
// }

//----------------------------------------------------------------------------------------------------------------------------


// Exercise 2

// program to demonstrate serialization and deserialization of an object

import java.io.*;

class Student implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private int age;
    private String address;

    public Student(String name, int age, String address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }

    public String toString() {
        return "Name: " + name + "\nAge: " + age + "\nAddress: " + address;
    }
}

public class Lab6 {
    public static void main(String[] args) {
        String file = ".\\Java\\student.ser";
        Student student = new Student("John", 18, "123 Main St, New York, NY");
        try {
            FileOutputStream fileOut = new FileOutputStream(file);
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(student);
            out.close();
            fileOut.close();
            System.out.println("Serialized data is saved in " + file);
        } catch (IOException e) {
            e.printStackTrace();
        }

        Student student2 = null;
        try {
            FileInputStream fileIn = new FileInputStream(file);
            ObjectInputStream in = new ObjectInputStream(fileIn);
            student2 = (Student) in.readObject();
            in.close();
            fileIn.close();
        } catch (IOException e) {
            e.printStackTrace();
            return;
        } catch (ClassNotFoundException e) {
            System.out.println("Student class not found");
            e.printStackTrace();
            return;
        }
        System.out.println("Deserialized Student...");
        System.out.println(student2);
    }
}

//----------------------------------------------------------------------------------------------------------------------------