//添加事件监听器
let button = document.getElementById("myButton");
button.addEventListener("click", function (evenet) {
  alert("button clicked");
});

//删除事件监听器
function handleClick(evenet) {
  alert("Buton clicked!");
}

button - document.getElementById("myButton");
button.addEventListener("click", handleClick);

//删除事件监听器
button.removeEventListener("click", handleClick);

//事件对象
document
  .getElementById("myButton")
  .addEventListener("click", function (evenet) {
    console.log("Event type", evenet.type);
    console.log("Event target", evenet.target);
    evenet.preventDefault();
    evenet.stopPropagation();
  });

//事件冒泡和捕获
//事件冒泡
document
  .getElementById("parentDiv")
  .addEventListener("click", function (evenet) {
    console.log("Parent div cliked");
  });
document
  .getElementById("myButton")
  .addEventListener("click", function (evenet) {
    console.log("Button clicked");
  });
//会先出发按钮的事件监听器，然后触发div的事件监听器

//事件捕获
document.getElementById("parentDiv").addEventListener(
  "click",
  function (evenet) {
    console.log("parent div clicked");
  },
  true
);
document
  .getElementById("myButton")
  .addEventListener("click", function (evenet) {
    console.log("Button clicked");
  });

//事件委托
document.getElementById("mylist").addEventListener("click", function (evenet) {
  if (evenet.target.tagName === "LI") {
    alert("Item clicked" + evenet.target.textContent);
  }
});
