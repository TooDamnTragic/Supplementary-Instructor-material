public abstract class Animal {
    private String name;

    public Animal(String name) {
        this.name = name;
    }

    public abstract void makeSound();
}

// public class Dog extends Animal {
//     public Dog(String name) {
//         super(name);
//     }


// }


// public abstract class Vehicle {
//     public abstract void drive();
// }

// public class Tester {
//     public static void main(String[] args) {
//         Vehicle v = new Vehicle();  // Attempt to instantiate
//         v.drive();
//     }
// }

// public abstract class Shape {
//     public abstract double area();
// }

// public class Circle extends Shape {
//     private double radius;

//     public Circle(double radius) {
//         this.radius = radius;
//     }

//     // MISTAKE:
//     public double area(double extra) {
//         return Math.PI * radius * radius + extra;
//     }