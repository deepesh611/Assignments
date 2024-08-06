
// interface Area{
//     final static float pi = 3.14F;
//     float compute(float x, float y);
// }

// class Rectangle implements Area{
//     public float compute(float x, float y){
//         return (x*y);
//     }
// }

// class Circle implements Area{
//     public float compute(float x){
//         return (pi*x*x);
//     }
// }

// class main{
//     public static void main (String[] args){
//         Rectangle rect = new Rectangle();
//         Circle cir = new Circle();
//         System.out.println("Area of Rectangle : " + rect.compute(2.5F,3.5F));
//         System.out.println("\nArea of Circle : " + cir.compute(1F));
//     }
// }



// 10.2 Debugging Exercise

// interface FamousLine{
//     void ShowLine();
// }

// class Novel1 implements FamousLine{
//     public void ShowLine(){
//         System.out.println("To be, or not to be");
//     }
// }

// class Novel2{
//     public void Author(){
//         System.out.println("Shakesphere");
//     }
// }

// public class UseInterface{
//     public static void main(String [] args){
//         Novel1 hamlet = new Novel1();
//         Novel2 juliet = new Novel2();
//         hamlet.ShowLine();
//         juliet.Author();
//     }
// }




// 10.3


interface NewCircle {
    abstract class Banana {
        public abstract void Eat();
    }  
}


class ExtendInterface implements NewCircle.Banana{
    public void Eat(){
        System.out.println("hello");
    }
}

class Main extends ExtendInterface{
    public static void main(String[] args) {
        ExtendInterface ei = new ExtendInterface();
        ei.Eat();

    }
}