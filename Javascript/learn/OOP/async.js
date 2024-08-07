const { reject } = require("async");

//回调函数
function fetchaData(callback) {
  setTimeout(() => {
    const data = "Fetched Data";
    callback(data);
  }, 2000);
}

fetchaData((result) => {
  console.log(result);
});

//Promise
//一被创建就会被立即执行
//用于处理异步操作，成功和失败分别执行对应的情况
const fetchData = new Promise((resolve, reject) => {
  setTimeout(() => {
    const data = Math.random();
    if (data > 0.5) {
      reject(data);
    } else {
      resolve(data);
    }
  }, 2000);
});
//成功和失败分别的执行情况
fetchData
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.error(error);
  });

//链式调用
fetchData
  .then((result) => {
    console.log(result);
    return "new operation";
  })
  .then((newMessage) => {
    console.log(newMessage);
  })
  .catch((error) => {
    console.error(error);
  });

//async/await
//实现异步函数
function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const data = "Fetched Data";
      resolve(data);
    }, 2000);
  });
}

async function getData() {
  try {
    const result = await fetchData();
    console.log(result);
  } catch (error) {
    console.error(error);
  }
}
//实现异步操作
getData();
console.log("nihao");

//event loop
console.log("Start");

setTimeout(() => {
  console.log("Timeout");
}, 0);
// console.log("End")
// console.log("Start");：这条语句会立即执行，并输出“Start”。

// setTimeout(() => { console.log("Timeout"); }, 0);
// ：setTimeout 函数安排一个回调函数在指定的延迟（这里是0毫秒）之后执行。
// 即使延迟为0，回调函数仍然会被放入“任务队列”中，而不会立即执行。
// 它会等待当前执行栈中的代码执行完毕后再执行。

// // console.log("End");：这条语句会在 setTimeout 函数的回调被放入任务队列之前立即执行，并输出“End”。
