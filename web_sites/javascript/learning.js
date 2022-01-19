//variables - var, let and const
// var - used less often, is a global scope
// let - can be changed throughout program
// const - can't change

let age = 30;
age = 31; 
console.log(age);

let name = 'Rainey';
console.log(name);


// data types - string, numbers, boolean, null, undefined, symbol
// string
const name = 'Rainey';
const age = 30;
const rating = 4.5;
const isCool = true;
const x = null;
const y = undefined;
let z;

console.log(typeof(rating)); //name of variable)//)

// concatentaion of strings
let real_name = 'John'
console.log(`Hi, my name is ${real_name}.`)

// finding the length of string
const s = 'Hello World';
console.log(s.length);

// uppercase and lowercase
const s = 'Hello World';
console.log(s.toUpperCase());
console.log(s.toLowerCase());

// substring
const s = 'Hello World';
console.log(s.substring(0, 5));
// you can combined 
console.log(s.substring(0, 5).toUpperCase());

// arrays
// split by letter
const s = 'Hello World';
console.log(s.split(''));

// split by word
const s = 'tech, computers, code, program';
console.log(s.split(', '));

let fruits = ['apples', 'oranges', 'pears'];
console.log(fruits);
// if you want an item within the array
console.log(fruits[1]);
//add an item to the array
fruits[3] = 'grapes';
// if you dont know the length of the array you can use push
fruits.push('mangos');
// if you want to add an item to the beginning of the array
fruits.unshift('strawberries'); 
// find the index
console.log(fruits.indexOf('oranges'));
console.log(fruits);

const todos = [
    {
        id: 1,
        text: 'Take out trash',
        isCompleted:true
    },
    {
        id: 2,
        text: 'Meeting with Boss',
        isCompleted:true
    },
    {
        id: 3,
        text: 'Doctor Apt',
        isCompleted:false
    },
];
// to find meeting with boss
console.log(todos[1].text);

// converting to JSON and sending to a server
const todoJSON = JSON.stringify(todos);
console.log(todoJSON);



// object literals
const person = {
    firstName: 'Rainey',
    lastName: 'Schafer',
    age: 32, 
    hobbies: ['music', 'movies', 'sports'],
    address: {
        street: '123 Main St.',
        city: 'Boston',
        state:'MA'
    }
}
// to find movies
console.log(person.hobbies[1]);
// to find the city
console.log(person.address.city);
// destructuring
const {firstName, lastName, address: {city}} = person;
console.log(firstName);
console.log(city);
// add item to person
person.email = 'rainey@gmail.com'
console.log(person);

// for loop
for(let i = 0; i < 10; i++) {
    console.log(i);
}
// for loop on an array
for(let x of todos){
   console.log(x.text)
}

// while loop
let i = 0;
while (i<10) {
    console.log(`While loop number: ${i}`);
    i++;
}

// array methods - forEach, map, filter
// ForEach
todos.forEach(function(todo) {
    console.log(todo.text);
});
// map
const todoText = todos.map(function(todo) {
    return todo.text;
});
console.log(todoText);
// filter
const todoCompleted = todos.filter(function(todo) {
    return todo.isCompleted == true;
});
console.log(todoCompleted);
// combining them
const todoCompleted = todos.filter(function(todo) {
    return todo.isCompleted == true;
}).map(function(todo) {
    return todo.text;
})
console.log(todoCompleted);

// conditionals
const x = 10;
if(x==10) {
    console.log('x is 10');
} else if (x>10) {
    console.log('x is greater than 10');
} else {
    console.log('x is less than 10');
}

// ternary operator or shorthand if statement
// ? = then 
// : = else
const x = 10;
const color = x > 10 ? 'red': 'blue';
console.log(color)

// switches
const x = 10;
const color = x > 10 ? 'red': 'blue';
switch(color) {
    case 'red':
        console.log('color is red');
        break;
    case 'blue':
        console.log('color is blue');
        break;
    default:
        console.log('color is not red or blue');
        break;
}

// functions
function addNums(num1, num2) {
    return num1+num2;
}
console.log(addNums(5, 4));

// constructor function
function Person(first, last, dob) {
    this.first = first;
    this.last = last;
    this.dob = new Date(dob);
}

// instantiate
let person1 = new Person('John', 'Smith', '2/23/80');
let person2 = new Person('Mary', 'Brown', '1/15/01');
console.log(person1);
console.log(person2.first);

// class
class Person {
    constructor(first, last, dob) {
        this.first = first;
        this.last = last;
        this.dob = new Date(dob);
    }

    getBirthYear() {
        return this.dob.getFullYear();
    }

    getFullName () {
        return `${this.first} ${this.last}`;
    }
}
// instantiate
let person1 = new Person('John', 'Smith', '2/23/1980');
let person2 = new Person('Mary', 'Brown', '1/15/2001');
console.log(person1.getFullName());
console.log(person2.getBirthYear);