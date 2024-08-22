import Vue from "vue";

Vue.directive("random-bg", {
  bind(el) {
    const randomColor = "#" + Math.floor(Math.random() * 16777215).toString(16);
    el.style.backgroundColor = randomColor;
  },
});
