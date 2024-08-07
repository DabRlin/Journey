url = "https://example.com";

//GET请求
fetch("https://example.com")
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error("Errot:", error));

//POST请求
fetch("https://api.example.com/data", {
  method: "POST",
  header: {
    "Content-type": "application/json",
  },
  body: JSON.stringify({ key: "value" }),
})
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => console.error("Error:", error));

//处理响应
// fetch 返回的 Promise 对象包含一个 Response 对象，Response 对象代表服务器的响应。可以使用以下方法处理响应数据：

// response.json()：将响应体解析为 JSON 对象。
// response.text()：将响应体解析为文本。
// response.blob()：将响应体解析为 Blob 对象（用于处理二进制数据）。
// response.formData()：将响应体解析为 FormData 对象（用于处理表单数据）。
// response.arrayBuffer()：将响应体解析为 ArrayBuffer 对象（用于处理二进制数据）。
fetch("https://example.com")
  .then((response) => response.json())
  .then((data) => console.log(data));

//fetch错误处理
// fetch 只会在网络错误（如无法连接到服务器）时拒绝 Promise，
// 不会因为 HTTP 错误状态码（如 404 或 500）而拒绝 Promise。
// 因此，需要手动检查响应状态码：
fetch("httpss://example.com")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Newwork response was not ok");
    }
    return response.json();
  })
  .then((data) => console.log(data))
  .catch((error) => console.error("Error:", error));

//设置请求头
fetch("https://example.com", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: "Bearer token",
  },
  body: JSON.stringify({ key: "value" }),
})
  .then((response) => response.json())
  .then((data) => console.log(data));

//高级用法
//设置请求超时
// AbortController用于控制fetch请求的对象，允许通过AbortSignal取消一个请求
const controller = new AbortController();
//计时5s终止请求
const timeoutID = setTimeout(() => controller.abort(), 5000);

fetch("https://api.example.com/data", {
  signal: controller.signal,
})
  .then((response) => response.json())
  .then((data) => console.log(data))
  .catch((error) => {
    //如果是因为调用Abort导致的error
    if (error.name === "AbortError") {
      console.error("Request timed out");
    } else {
      console.error("Errot", error);
    }
    //清除计时器
  })
  .finally(() => clearTimeout(timeoutID));

//并行请求
Promise.all([
  fetch("https://api.example.com/data1").then((response) => response.json()),
  fetch("https://api.example.com/data2").then((response) => response.json()),
])
  .then(([data1, data2]) => {
    console.log(data1);
    console.log(data2);
  })
  .catch((error) => console.error("Error", error));
