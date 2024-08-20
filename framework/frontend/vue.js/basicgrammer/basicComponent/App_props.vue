<template>
  <div id="app">
    <!-- 通过name向子组件传递参数 -->
     <!-- 通过v-bind将userName的值传递给name -->
    <greeting :name="userName"></greeting>
  </div>
</template>

<script>
import Greeting from "./Greeting.vue";
export default {
  //注册greeting组件
  components: {
    Greeting,
  },
  data() {
    return {
      userName: "Alice",
    };
  },
};
</script>
