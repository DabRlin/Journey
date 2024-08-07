//变量
var x = 10//函数作用域
let y = 20//不能再次声明 块级作用域
const z = 30//声明后不能再赋值

//数据类型
let str = "1234"
let num = 123
let bool = true
let empty = null
let notDefined
let obj = {key:"value"}//对象。复杂数据类型
let arr = [1, 2, 3]
let sym = Symbol("id")
console.log(sym)

//类型转换
let str2 = Number(str)
console.log(str)
console.log(str2)

//基本运算
let sum = 5+10
let contat = "Hello" + "world"
let product = 5* 10
let quotient = 10/2
sum ++
console.log(true && false)
console.log(true || false)
console.log(!true)
console.log(5<=100)
console.log("5"===5)//严格相等
console.log(5=="5")


//JavaScript的分号不是必须的，但是建议显式的添加分号