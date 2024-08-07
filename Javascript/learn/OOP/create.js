//构造函数
let person = new Object();

person.name = "John";
person.age = 40;
person.greet = function () {
  console.log("Hello ~!");
};

console.log(person.name);
person.greet();

//对象字面量
let student = {
  name: "Alice",
  age: 30,
  greet: function () {
    console.log("Hellow");
  },
};

student.key = 100;
console.log(student.name);
student.greet();
console.log(student.key);

//对象的属性和方法
person = {
  name: "John",
  greet: function () {
    console.log("hello", this.name);
  },
};

person.greet();

//内置对象和方法
console.log(Object.keys(person));
console.log(Object.values(person));
console.log(Object.entries(person));
