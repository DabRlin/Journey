<template>
    <!-- input触发名为input的自定义事件 将evenet即输入框的值传递给父组件 -->
     <!-- event表示事件对象或者事件值 此处是input输入的值 作为事件的参数传递出去 被v-model接收绑定到对应的data -->
  <el-input
    :value="value"
    @input="$emit('input', $event)"
    placeholder="Custom input"
  >
    <template slot="append">
      <el-button @click="handleClick">Click me</el-button>
    </template>
  </el-input>
</template>

<script>
export default {
    //此处暴露接口 从而实现了v-model的自动绑定
  props: ["value"],
  methods: {
    handleClick() {
      this.$emit("custom-click");
    },
  },
};
</script>
