//函数表达式
let greet = function (name) {
  return "Hello" + name;
};

console.log(greet("Alice"));

//箭头函数
let greet2 = (name) => {
  return "Hello," + name;
};

console.log(greet2("Bob"));

let greet3 = (name) => "Hello" + name;
console.log("Chris");

//在浏览器中运行
// callback 回调函数
function processUserInput(callback) {
  let name = prompt("Please enter your name");
  callback(name);
}

function greetname(name) {
  console.log("Hello," + name);
}

processUserInput(greetname);
