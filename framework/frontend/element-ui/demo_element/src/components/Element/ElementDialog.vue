<template>
  <div>
    <!-- 触发对话框的按钮 -->
    <!-- type是样式类型 -->
    <el-button type="text" @click="dialogVisible = true">Open Dialog</el-button>

    <!-- 对话框组件 -->
    <!-- visible.sync修饰符双向绑定dialogVisable属性 控制对话显示与隐藏 -->
    <el-dialog title="Dialog" :visible.sync="dialogVisible">
      <!-- 对话框内容 -->
      <p>This is a dialog</p>

      <!-- 对话框的底部区域 -->
      <!-- slot是vue.js的功能 插槽 用于在组件中插入自定义的内容 此处插入对话框底部 -->
      <span slot="footer" class="dialog-footer">
        <!-- 取消按钮 -->
        <el-button @click="dialogVisible = false">Cancel</el-button>

        <!-- 确认按钮 -->
        <el-button type="primary" @click="dialogVisible = false"
          >Confirm</el-button
        >
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dialogVisible: false,
    };
  },
};
</script>
