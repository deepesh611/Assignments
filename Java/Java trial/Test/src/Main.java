

interface NewCircle {
    abstract class Banana {
        public abstract void Eat();
    }
}


class ExtendInterface extends NewCircle.Banana {
    public void Eat(){
        System.out.println("I am eating");
    }
}

class Main extends ExtendInterface{
    public static void main(String[] args) {
        ExtendInterface ei = new ExtendInterface();
        ei.Eat();

    }
}