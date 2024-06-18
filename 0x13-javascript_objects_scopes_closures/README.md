An object is a collection of related data and/or functionality. These usually consist of several variables and functions (which are called properties and methods when they are inside objects).

As with many things in JavaScript, creating an object often begins with defining and initializing a variable:

Creating an empty object:
const person = {};


an object is made up of multiple members, each of which has a name (e.g. name and age above), and a value (e.g. ['Bob', 'Smith'] and 32). Each name/value pair must be separated by a comma, and the name and value in each case are separated by a colon. The syntax always follows this pattern:

const objectName = {
  member1Name: member1Value,
  member2Name: member2Value,
  member3Name: member3Value,
};

Example of an object
const person = {
  name: ["Bob", "Smith"],
  age: 32,
  bio: function () {
    console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
  },
  introduceSelf: function () {
    console.log(`Hi! I'm ${this.name[0]}`)
  }
};

Dot notation
This is used to access the object's properties and methods.

Example
person.name

const person = {
  name: {
    first: "Bob",
    last: "Smith",
  },
  // …
};

To access these items you just need to chain the extra step onto the end with another dot:

person.name.first;
person.name.last;

Bracket notation:
Provides an alternative way to access object properties.:
person["age"];
person["name"]["first"];


Classes and constructors:
You can declare a class using the class keyword:
class Person {
    name;
    constructor(name) {
        this.name = name;
    }

    introduceSelf() {
        console.log(`Hi I'm ${this.name}`);
    }
}

This declares a class called Person, with:

    a name property.
    a constructor that takes a name parameter that is used to initialize the new object's name property
    an introduceSelf() method that can refer to the object's properties using this.


Inheritance:
We use the extends keyword to say that this class inherits from another class.

Example:
class Professor extends Person {
  teaches;

  constructor(name, teaches) {
    super(name);
    this.teaches = teaches;
  }

  introduceSelf() {
    console.log(
      `My name is ${this.name}, and I will be your ${this.teaches} professor.`,
    );
  }

  grade(paper) {
    const grade = Math.floor(Math.random() * (5 - 1) + 1);
    console.log(grade);
  }
}
