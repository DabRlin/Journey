//控制流语句
let x = 10
if (x>4){
    console.log("x is greater than 4")
}

if (x > 5){
    console.log("x us greater than 5")
}else{
    console.log("x is smaller than 5")
}

if (x == 5){
    console.log("x is 5")
}else if (x > 5){
    console.log("x is bigger than 5")
}else{
    console.log("x is smaller than 5")
}

let day = 7
let dayName

switch (day) {
    case 1:
        dayName = "Monday";
        break;
    case 2:
        dayName = "Tuesday";
        break;
    default:
        dayName = "Invalid day";
}


console.log("the %d is %s",day,dayName);


//遍历
for(let i = 0; i < 5 ;i++){
    console.log("Hello world")
}


//while循环
let i = 1
while (i < 5) {
    console.log(i);
    i ++;
}

//do-while循环
do{
    console.log("你好")
    i++
}while(i < 10)

//return
function add(a,b){
    return a+b;
}
let result = add(5,6)
console.log(result)
//continue
for (let index = 0; index < 10 ;index++) {
    if(index % 2 == 0){
        continue;
    }    
    console.log(i);
}

//break
for (let index = 0; index < 10; index++) {
    if(index == 5){
        break;
    }
    console.log(i)
}