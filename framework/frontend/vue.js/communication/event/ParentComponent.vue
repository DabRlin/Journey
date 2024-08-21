<template>
  <div>
    <!-- 此处的@child-clicked会把消息一并传递给handleChildClick -->
    <!-- 而handleChildClick会输出消息 -->
    <!-- 子组件事件冒泡被父组件捕获 -->
    <ChildComponent @child-clicked="handleChildClick"></ChildComponent>
  </div>
</template>

<script>
import ChildComponent from "./ChildComponent.vue";
import ChildComponent from "./ChildComponent.vue";

export default {
  components: {
    ChildComponent,
  },
  methods: {
    handleChildClick(message) {
      console.log(message); //输出子组件的消息
    },
  },
};
</script>
