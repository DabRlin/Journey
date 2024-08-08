//本地存储
localStorage.setItem("name", "John");

let name = localStorage.getItem("name");
console.log(name);

localStorage.removeItem("name");

//清空本地存储
localStorage.clear();

//会话存储
sessionStorage.setItem("sessionName", "Alice");

let sessionName = sessionStorage.getItem("sessionName");
console.log(sessionName);

sessionName.removeItem("sessionName");

sessionStorage.clear();
