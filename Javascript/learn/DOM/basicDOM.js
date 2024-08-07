//dom api
//get title
let title = document.title
//get element with id
let element = document.getElementById("id")
//get element array with class
let elements = document.getElementsByClassName("myclass")
//get element with tagname
elements = document.getElementsByTagName("div")
//get element with css selector
element = document.querySelector(".myclass")
//get all element with css selector
elements = document.querySelectorAll(".myclass")
//add element
let newElement = document.createElement("div")
document.body.appendChild(newElement)
//remove element
let parentElement = document.getElementById("container")
parentElement.removeChild(parentElement.firstChild)


//dom operation
//updata text
element = document.getElementById("container")
element.textContent = "Next Text"
let text = element.textContent

//update innerHTML
element = document.getElementById("container")
element.innerHTML = "<p> New HTML content</p>"
let html = element.innerHTML

//update class
element = document.getElementById("container")
element.setAttribute("class","newClass")
let className = element.getAttribute("class")

//add
newElement = document.createElement("div")
newElement.textContent = "Hello world"
document.body.appendChild(newElement)

//delete
element = document.getElementById("container")
element.parentNode.removeChild(element)

//update
element = document.getElementById("container")
element.style.color = "red"
element.style.backgroundColor = "blue"

element.classList.add("newClass")
element.classList.remove("oldClass")
element.classList.toggle("toggleClass")