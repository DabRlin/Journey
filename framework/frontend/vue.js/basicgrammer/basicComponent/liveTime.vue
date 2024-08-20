<template></template>

<script>
export default {
  data() {
    messag: "hello, vue!";
  },
  //组件实例被创建的时候调用
  created() {
    console.log("Component is created");
  },
  //组件被挂载到DOM时调用
  mounted() {
    console.log("Component is mounted");
  },
  //组件更新时调用
  updated() {
    console.log("Component is updated");
  },
  //组件销毁时调用
  destoryed() {
    console.log("Component is destoryed");
  },
};
</script>
