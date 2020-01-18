# Java: The Basics

## Comments

Single line comments are used for describing code functionality.

Multi line comments are used to describe a full method in code.

~~~java
//Java program to show single line comments
class SingleComment
{
    /*Multi-line comment describes
    a full method in code, 
    ex: main() method*/
    public static void main(String args[])
    {
        // Single line comment here
        System.out.println("Single line comment above");
    }
}
~~~

## Declaration/Initialization

Declaring and initializing primitive types and objects.

~~~java
// 1. Declaration vs Initialization for Primitives

// Declaration is defining the variable with type & name
int id;

// Initialization is assigning a value
id = 1;

// 2. Declaration for Objects
// Custom Objects originate from classes, such as User class
public class User implements {
    private String name;
    private int id;

    // constructor, getters, setters
}

// Declare and initialize a new User object to reference type User
@Test
public void whenInitializedWithNew_thenInstanceIsNotNull() {
    User user = new User();

    assertThat(user).isNotNull();
}

// 3. Initialization for Objects (Creating Objects)
// Trigger Initialization using new keyword, which allocates memory
// for the new object through a constructor, which initializes
// instance variables representing the main properties of the object

// Add a constructor to User class
public class User implements {
    private String name;
    private int id;

    // constructor
    public User(String name, int id) {
        this.name = name;
        this.id = id;
    }
}
// Use constructor to create object with initial values for its properties
User user = new User("Alice", 1)

// 4. Instance and Class Variables
// Don't require us to initialize them since once they are declared,
// they are auto given default value
@Test
public void whenValuesAreNotInitialized_thenUserNameAndIdReturnDefault() {
    User user = new User();
  
    assertThat(user.getName()).isNull();
    assertThat(user.getId() == 0);
}

// 5. Local Variables
// Must be initialized before use, they don't have default value
public void print() {
    int i;
    System.out.println(i);
}

// 6. Final keyword
// Once applied to a field, the field's value can't be changed
// after initialization, which is the way to define constants
// Constants must be initialized when they're declared or in constructor

// Add a constant to our User class
public class User implements {
    private static final int YEAR = 2000;
    private String name;
    private int id;

    // constructor
    public User(String name, int id) {
        this.name = name;
        this.id = id;
    }
}

// 7. Initializers
// a block of code with no name or data type association
// Java offers two types of initializers: static and instance

// Instance Initilializer
{
    id = 0;
}

// Static Initialization Block - block of code to init static fields
private static String forum;
static {
    forum = "java";
}

// 9. Order of Initialization
// - static variables and static initializers in order
// - instance variables and instance initializers in order
// - constructors
~~~

- [A Guide to Creating Objects in Java](https://www.baeldung.com/java-initialization) link includes a look at various ways to initialize primitype types and objects in Java

## Data Types

Eight primitive data types

- boolean: true or false
- char: 16-bit Unicode characters
- arithmetic types: byte, short, int, long
- float-point types: float, double

| Type        | Description  | Default     | Size        | Ex Literals   |
| ----------- | -----------  | ----------- | ----------- | -----------   |
| boolean      | true or false  | false    | 1 bit       | true, false   |
| byte   | twos complement int  | 0        | 8 bits      | (none)        |
| char   | Unicode character    | \u0000   | 16 bits     | 'a', '\u0041' |
| short  | twos complement int  | 0        | 16 bits     | (none)        |
| int    | twos complement int  | 0        | 32 bits     | -2,-1,0,1,2   |
| long   | twos complement int  | 0        | 64 bits     | -2L,-1L,0L,1L |
| float  | IEEE 754 float point | 0        | 32 bits     | 1.23e100f,.3f |
| double | IEEE 754 float point | 0        | 64 bits     | 1.23456e300d  |

~~~java
boolean result = true;
char capitalC = 'C';
byte b = 100;
short s = 10000;
int i = 100000;
long creditCardNumber = 1234_5678_9012_3456L;
double d1 = 123.4;
float f1  = 123.4f;
~~~

- [Primitive Data Types](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html) link looks at the 8 primitve data types in Java


## Simple Logging

~~~Java
// Logger and Log Level in descending order
// - SEVERE (highest)

// - WARNING

// - INFO

// - CONFIG

// - FINE

// - FINER

// - FINEST (lowest level)

public class LoggerExample {
 
    private static final Logger LOGGER = Logger.getLogger(LoggerExample.class.getName());
    public static void main(String[] args) throws SecurityException, IOException {
 
        LOGGER.info("Logger Name: "+LOGGER.getName());
         
        LOGGER.warning("Can cause ArrayIndexOutOfBoundsException");
         
        //An array of size 3
        int []a = {1,2,3};
        int index = 4;
        LOGGER.config("index is set to "+index);
         
        try{
            System.out.println(a[index]);
        }catch(ArrayIndexOutOfBoundsException ex){
            LOGGER.log(Level.SEVERE, "Exception occur", ex);
        }
         
 
    }
 
}
~~~

- [java.util.logging Example](https://examples.javacodegeeks.com/core-java/util/logging/java-util-logging-example/) link looks at more in depth view on Java Logging


## Conditionals

~~~java
int a = 4;

if (a == 4) {
    System.out.println("Ohhh! So a is 4!");
} else {
    System.out.println("a is not 4!");
}
~~~

- [Conditionals](https://www.learnjavaonline.org/en/Conditionals) link includes in depth info on Java Conditionals

## Loops

While loop example:

~~~java
// Java program to illustrate while loop 
class whileLoopDemo 
{ 
    public static void main(String args[]) 
    { 
        int x = 1; 
  
        // Exit when x becomes greater than 4 
        while (x <= 4) 
        { 
            System.out.println("Value of x:" + x); 
  
            // Increment the value of x for 
            // next iteration 
            x++; 
        } 
    } 
} 
~~~

For loop example:

~~~java
// Java program to illustrate for loop. 
class forLoopDemo 
{ 
    public static void main(String args[]) 
    { 
        // for loop begins when x=2 
        // and runs till x <=4 
        for (int x = 2; x <= 4; x++) 
            System.out.println("Value of x:" + x); 
    } 
} 
~~~

Do while loop example:

~~~java
// Java program to illustrate do-while loop 
class dowhileloopDemo 
{ 
    public static void main(String args[]) 
    { 
        int x = 21; 
        do
        { 
            // The line will be printed even 
            // if the condition is false 
            System.out.println("Value of x:" + x); 
            x++; 
        } 
        while (x < 20); 
    } 
} 
~~~

- [Loops in Java](https://www.geeksforgeeks.org/loops-in-java/) link includes in-depth info loops

## Functions

All function definitions must be inside classes.

- functions: foo(), bar(), bar2(), main()

~~~java
public class Main {
    public static void foo() {
        // Do something here
    }
    // all arguments to methods are passed by value
    public void bar(int num1, int num2) {
        ...
    }

    // same for if arguments were objects
    public void bar2(Student s1, Student s2) {
        ...
    }

    public static void main(String args[])
    {
        // primitive int data type
        int a = 3;
        int b = 5;
        bar(a, b);

        // object Student data type
        Student bruce = new Student("Bruce");
        Student chuck = new Student("Chuck");
        bar2(bruce, chuck);
    }
}
~~~

- [Functions](https://www.learnjavaonline.org/en/Functions) link includes in depth info on Functions in Java

## Classes

Everything in Java is associated with classes and objects along with its attributes and methods.

set up a basic class with constructor, method

~~~java
// Create a Person
public class Person {
  String name = 'James'
  int age = 25;
  // Constructor
  public Person(String name, int age) {
      this.name = name;
      this.age = age;
  }

  public birthday() {
      this.age += 1;
  }

  //Create an Object from a class
  public static void main(String[] args) {
    MyClass james = new Person();
    james.birthday(); // turned 26
    System.out.println(james.age);
  }
}

// Create other class, create object from previous class in new class
class Car {
  public static void main(String[] args) {
    MyClass chris = new Person('Chris', 25);
    System.out.printf("Car owner is %s", chris.name);
  }
}
~~~