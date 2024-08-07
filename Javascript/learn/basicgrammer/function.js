//基本函数
function greet(name) {
  return `Hello ${name}!`;
}

console.log(greet("Alice"));

//函数表达式
const add = function (a, b) {
  return a + b;
};
console.log(add(1, 9));

//命名函数表达式
const multiply = function multiply(a, b) {
  return a * b;
};
console.log(multiply(9, 8));

//箭头函数
const substract = (a, b) => a - b;
console.log(substract(8, 9));

//多行箭头函数
const divide = (a, b) => {
  if (b === 0) {
    throw new Error("cannot divide by zero");
  }
  return a / b;
};

console.log(divide(6, 2));

//函数参数和返回值
function greet(name = "Guest") {
  return `Hello, ${name}!`;
}

console.log(greet());

function getRectangleArea(width, height) {
  return width * height;
}

const area = getRectangleArea(5, 9);
console.log(`Area:${area}`);

//全局作用域
let globalVar = "I am global";
function showGlobalVar() {
  console.log(globalVar);
}

showGlobalVar();

//函数作用域
function myFunction() {
  let localVar = "I am local";
  console.log(localVar);
}

myFunction();

//块级作用域
if (true) {
  let blockVar = "I am inside block";
  console.log(blockVar);
}
//会报错
// console.log(blockVar)

//函数闭包
function outerFunction() {
  let outerVar = "I am outer";
  function innerFunction() {
    console.log(outerVar);
  }
  return innerFunction;
}

const closure = outerFunction();
closure();
