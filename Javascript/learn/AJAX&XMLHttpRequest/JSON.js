//解析JSON
let jsonString = '{"name": "John", "age": 30}';
let jsonObject = JSON.parse(jsonString)

console.log(jsonObject.name)

//序列化JSON
let jsonObject1 = {name:"John",age:30}
let jsonString1 = JSON.stringify(jsonObject1)
console.log(jsonString1)