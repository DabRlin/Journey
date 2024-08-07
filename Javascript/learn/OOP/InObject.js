let now = new Date()
console.log(now)

let specificDate = new Date("2024-08-07")
console.log(specificDate)

console.log(now.getDate())
console.log(now.getMonth())
console.log(now.getFullYear())
console.log(now.toLocaleDateString())

//Math
console.log(Math.max(1,2,4))
console.log(Math.min(1,2,3))
console.log(Math.random())
console.log(Math.floor(1.9))

//String
let str = "Hello,World!"

console.log(str.length);
console.log(str.substring(0,3))
console.log(str.replace("World","Javascript"))
console.log(str.toLowerCase())
console.log(str.toUpperCase())
