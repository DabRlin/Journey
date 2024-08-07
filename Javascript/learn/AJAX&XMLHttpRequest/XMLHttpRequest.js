//基本操作
let xhr = new XMLHttpRequest();

xhr.open("GET", "https://example.com", true);
xhr.send();
//处理响应数据
xhr.onreadystatechange = function () {
  if (xhr.readyState === 4 && xhr.status === 200) {
    let data = JSON.parse(xhr.responseText);
    console.log(data);
  } else {
    console.error("Error", xhr.statusText);
  }
};
//设置请求头
xhr.setRequestHeader("Content-Type", "application/json");
//发送请求
//GET
xhr.send();
//POST
xhr.send(JSON.stringify({ key: "Value" }));

//GET请求示例
let xhr = new XMLHttpRequest();
xhr.open("GET", "https://example.com", true);

xhr.onreadystatechange = function () {
  if (xhr.readyState === 4 && xhr.status === 200) {
    let data = JSON.parse(xhr.responseText);
    console.log(data);
  }
};

xhr.send();

//POST请求示例
let xhr = new XMLHttpRequest();
xhr.open("POST", "https://example.com");
xhr.setRequestHeader("Content-type", "applicaton/json");

xhr.onreadystatechange = function () {
  if (xhr.readyState === 4 && xhr.status === 200) {
    let data = JSON.parse(xhr.responseText);
    console.log(data);
  }
};

let postData = JSON.stringify({ key: "value" });

xhr.send(postData);