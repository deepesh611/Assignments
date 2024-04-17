// # 3
// Exercise - 1

package Java;

// // create a class named 'person' with attributes such as 'name', 'age' and 'address' and also includes appropriate methods such as setters and getters

// class Person {
//     private String name;
//     private int age;
//     private String address;

//     public void setName(String name) {
//         this.name = name;
//     }
//     public String getName() {
//         return name;
//     }

//     public void setAge(int age) {
//         this.age = age;
//     }
//     public int getAge() {
//         return age;
//     }

//     public void setAddress(String address) {
//         this.address = address;
//     }
//     public String getAddress() {
//         return address;
//     }


//     public void display() {
//         System.out.println("Name: " + name);
//         System.out.println("Age: " + age);
//         System.out.println("Address: " + address);
//     }
// }


// public class Lab3 {
//     public static void main(String[] args){
//         Person person1 = new Person();
//         person1.setName("John");
//         person1.setAge(25);
//         person1.setAddress("123 Main St, New York, NY");
//         System.out.println("Name: " + person1.getName());
//         System.out.println("Age: " + person1.getAge());
//         System.out.println("Address: " + person1.getAddress());

//         Person person2 = new Person();
//         person2.setName("Jane");
//         person2.setAge(30);
//         person2.setAddress("456 Main St, New York, NY");
//         System.out.println("Name: " + person2.getName());
//         System.out.println("Age: " + person2.getAge());
//         System.out.println("Address: " + person2.getAddress());

//         // using display method
//         person1.display();
//         person2.display();
//     }
// }


//----------------------------------------------------------------------------------------------------------------------------------------------------------------------


// Exercise - 2


// class Vehicles{
//     private String model;
//     private int year;
//     private String color;

//     public void setModel(String model){
//         this.model = model;
//     }
//     public String getModel(){
//         return model;
//     }

//     public void setYear(int year){
//         this.year = year;
//     }
//     public int getYear(){
//         return year;
//     }

//     public void setColor(String color){
//         this.color = color;
//     }
//     public String getColor(){
//         return color;
//     }
// }


// class car extends Vehicles{
//     private int noOfDoors;
//     private float engineCapacity;
//     private String fuelType;

//     public void setNoOfDoors(int noOfDoors){
//         this.noOfDoors = noOfDoors;
//     }
//     public int getNoOfDoors(){
//         return noOfDoors;
//     }

//     public void setEngineCapacity(float engineCapacity){
//         this.engineCapacity = engineCapacity;
//     }
//     public float getEngineCapacity(){
//         return engineCapacity;
//     }

//     public void setFuelType(String fuelType){
//         this.fuelType = fuelType;
//     }
//     public String getFuelType(){
//         return fuelType;
//     }
// }


// public class Lab3{
//     public static void main(String[] args){
//         car car1 = new car();
//         car1.setModel("Nissan");                                            // Inherited Features
//         car1.setYear(2021);                                                  // Inherited Features
//         car1.setColor("Black");                                             // Inherited Features
//         car1.setNoOfDoors(4);                                                       
//         car1.setEngineCapacity(2.5f);
//         car1.setFuelType("Petrol");

//         System.out.println("Model: " + car1.getModel());
//         System.out.println("Year: " + car1.getYear());
//         System.out.println("Color: " + car1.getColor());
//         System.out.println("No of Doors: " + car1.getNoOfDoors());
//         System.out.println("Engine Capacity: " + car1.getEngineCapacity());
//         System.out.println("Fuel Type: " + car1.getFuelType());
//     }
// }


//----------------------------------------------------------------------------------------------------------------------------------------------------------------------


// Exercise - 3



// interface Shape{
//     public float calculateArea(float radius);
//     public float calculateArea(float length, float height);
// };

// class Circle implements Shape{
//     public float calculateArea(float radius){
//         return (float) (3.14 * radius * radius);
//     }
//     public float calculateArea(float length, float height){
//         return 0;
//     }
// }

// class Rectangle implements Shape{
//     public float calculateArea(float length){
//         return 0;
//     }
//     public float calculateArea(float length, float height){
//         return (float) (length * height);
//     }
// }

// class Triangle implements Shape{
//     public float calculateArea(float base, float height){
//         return (float) (0.5 * base * height);
//     }
//     public float calculateArea(float length){
//         return 0;
//     }
// }

// public class Lab3{
//     public static void main(String[] args){
//         Shape[] shapes = new Shape[3];
//         shapes[0] = new Circle();
//         shapes[1] = new Rectangle();
//         shapes[2] = new Triangle();

//         System.out.println("Area of Circle: " + shapes[0].calculateArea(5));
//         System.out.println("Area of Rectangle: " + shapes[1].calculateArea(5, 10));
//         System.out.println("Area of Triangle: " + shapes[2].calculateArea(5, 10));
//     }
// }



//----------------------------------------------------------------------------------------------------------------------------------------------------------------------


// Exercise - 4


// modify 'Person' class to encapsulate its data by making its attributes private and providing public methods to access and modufy the data

// class Person {
//     private String name;
//     private int age;
//     private String address;

//     public void setName(String name) {
//         this.name = name;
//     }
//     public String getName() {
//         return name;
//     }

//     public void setAge(int age) {
//         this.age = age;
//     }
//     public int getAge() {
//         return age;
//     }

//     public void setAddress(String address) {
//         this.address = address;
//     }
//     public String getAddress() {
//         return address;
//     }
// }

// // an abstract class 'Shape' with an abstract method for calculating  the area and perimeter

// abstract class Shape{
//     public abstract float calculateArea();
//     public abstract float calculatePerimeter();
// }

// class Circle extends Shape{
//     private float radius;

//     public Circle(float radius){
//         this.radius = radius;
//     }

//     public float calculateArea(){
//         return (float) (3.14 * radius * radius);
//     }

//     public float calculatePerimeter(){
//         return (float) (2 * 3.14 * radius);
//     }
// }

// class Rectangle extends Shape{
//     private float length;
//     private float breadth;

//     public Rectangle(float length, float breadth){
//         this.length = length;
//         this.breadth = breadth;
//     }

//     public float calculateArea(){
//         return (float) (length * breadth);
//     }

//     public float calculatePerimeter(){
//         return (float) (2 * (length + breadth));
//     }
// }

// public class Lab3{
//     public static void main(String[] args){
//         Circle circle = new Circle(5);
//         System.out.println("Area of Circle: " + circle.calculateArea());
//         System.out.println("Perimeter of Circle: " + circle.calculatePerimeter());
//         System.out.println();
//         Rectangle rectangle = new Rectangle(5, 10);
//         System.out.println("Area of Rectangle: " + rectangle.calculateArea());
//         System.out.println("Perimeter of Rectangle: " + rectangle.calculatePerimeter());
//     }
// }


//----------------------------------------------------------------------------------------------------------------------------------------------------------------------


// Exercise - 5

// class Animal{
//     public void makeSound(){
//         System.out.println("Animal makes a sound");
//     }
// }


// class Dog extends Animal{
//     public void makeSound(){
//         System.out.println("Dog barks");
//     }
// }

// class Cat extends Animal{
//     public void makeSound(){
//         System.out.println("Cat meows");
//     }
// }

// public class Lab3{
//     public static void main(String[] args){
//         Animal animal = new Animal();
//         animal.makeSound();
//         Dog dog = new Dog();
//         dog.makeSound();
//         Cat cat = new Cat();
//         cat.makeSound();
//     }
// }


//----------------------------------------------------------------------------------------------------------------------------------------------------------------------
