<template>
  <div>
    <el-button type="primary" @click="showMessage">Show message</el-button>
    <el-button type="success" @click="showNotification"
      >Show Notification</el-button
    >
    <el-button type="warning" @click="showConfirmBox"
      >Shwo Confirm Box</el-button
    >
  </div>
</template>

<script>
export default {
  methods: {
    showMessage() {
      //使用message组件
      this.$message({
        message: "This is a message",
        type: "success",
      });
    },
    showNotification() {
      //使用Notification组件
      this.$notify({
        title: "Success",
        message: "This is a notificaton message.",
        type: "success",
      });
    },
    showConfirmBox() {
      //使用messageBox组件
      this.$confirm("Are you sure to delete this item?", "Warning", {
        //封装好 点击ConfirmButton进行成回调 点击CalcelButton进行失败回调
        confirmButtonText: "Yes",
        cancelButtonText: "No",
        type: "warning",
      })
        .then(() => {
          this.$message({
            type: "success",
            message: "Delete completed!",
          });
        })
        .catch(() => {
          this.message({
            type: "info",
            message: "Delete canceld",
          });
        });
    },
  },
};
</script>
