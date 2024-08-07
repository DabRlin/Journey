let number1 = [1, 2, 3, 4, 5];

console.log(number1[3]);

//数组构造函数
let number = new Array(1, 2, 3, 4, 5, 6);
console.log(number[0]);

number[3] = 10;
console.log(number[3]);

//常用数组方法
let numbers = [1, 2, 3, 4, 5, 6];

//添加元素
numbers.push(7);
console.log(numbers);

//删除最后一个元素
numbers.pop();
console.log(numbers);

//删除第一个元素
numbers.shift();
console.log(numbers);

//在开头添加元素
numbers.unshift(4);
console.log(numbers);

let doubled = numbers.map(function (num) {
  return num * 2;
});
