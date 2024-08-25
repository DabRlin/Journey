<template>
  <div>
    <!-- 选择框组件 创建一个下拉菜单 -->
    <el-select v-model="value" placeholder="Please select">
      <!-- label定义选项显示的文本 value定义选项的值 -->
      <el-option label="Option 1" value="1"></el-option>
      <el-option label="Option 2" value="2"></el-option>
      <el-option label="Option 3" value="3"></el-option>
    </el-select>
  </div>
</template>

<script>
export default {
  data() {
    return {
      value: "",
    };
  },
};
</script>
