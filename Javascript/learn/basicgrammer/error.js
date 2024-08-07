//基本的异常处理
try {
    let result = 10/0
} catch (error) {
    console.error("An errot occured:",error)    
}


try {
    let result = 10/0
    console.log(result)
} catch (error) {
    console.error("An errorr occured",error)
}finally{
    console.log("This well always run")
}

//抛出异常
function divide(a,b){
if (b === 0){
    throw new Error("Cannot divide by zero")
}
return a/b
}

try{
    let result= divide(10,0)
    console.log(result)
}catch(error){
    console.error("An error occured:",error.message)
}

//自定义异常类
class DividionByZeroError extends Error{
    constructor(message){
        super(message)
        this.name = "DivisionByZeriError"
    }
}

function divide(a,b){
    if (b === 0) {
        throw new DividionByZeroError("Cannot divide by zero")
    }
    return a/b
}

try {
    let result = divide(10,0)
    console.log(result)
} catch (error) {
    if (error instanceof DividionByZeroError) {
        console.error("Custom error:",error.message)
    }else{
        console.error("General error",error.message)
    }
}