<template>
  <div>
    <!-- 设置按钮调出dialog界面 -->
    <el-buton type="primary" @click="dialogVisible = true"
      >Show Dialog</el-buton
    >
    <!-- dialog内容 -->
    <el-dialog
      title="Confirm"
      :visible="dialogVisible"
      width="30%"
      @close="handleClose"
      ><span>This is a dialog.</span>
      <el-button @click="dialogVisible = false">Cancel</el-button>
      <el-button type="primary" @click="handleConfrim">Confirm</el-button>
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
  methods: {
    handleClose() {
      console.log("Dialog closed");
    },
    handleConfrim() {
      console.log("Dialog confrimed");
      this.dialogVisible = false;
    },
  },
};
</script>
