<template>
    <!-- 点击按钮触发自定义事件 -->
    <button @click="notifyParent">Click me!</button>
</template>

<script>
export default {
  methods: {
    // 定义自定义事件
    notifyParent() {
      this.$emit("child-clicked", "Button clicked in child component");
    },
  },
};
</script>
