<template>
  <!-- 使用ref作为模板引用 可以通过this.$refs.form访问表单实例 -->
  <!-- ref给予唯一标识符 -->
  <el-form :model="form" :rules="rules" ref="form" label-width="80px">
    <el-form-item label="Name" prop="name">
      <!-- 输入绑定form.name -->
      <el-input v-model="form.name" />
    </el-form-item>
    <el-form-item label="Email" prop="email">
      <!-- 输入绑定form.email -->
      <el-input v-model="form.email" />
    </el-form-item>
    <el-form-item>
      <!-- 两个按钮 分别调用提交方法和验证方法 -->
      <el-button type="primary" @click="submitForm('form')">Submit</el-button>
      <el-button @click="resetForm('form')">Reset</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  data() {
    return {
      form: {
        name: "",
        email: "",
      },
      rules: {
        // trigger为触发时机 即失去焦点时认证
        name: [
          {
            required: true,
            message: "Please input your name",
            trigger: "blur",
          },
        ],
        // email验证的两样规则 是否填写
        email: [
          {
            required: true,
            message: "Please input your email",
            trigger: "blur",
          },
          // 是否是邮箱
          {
            type: "email",
            message: "Please input a valid email address",
            trigger: "blur",
          },
        ],
      },
    };
  },
  methods: {
    submitForm(formName) {
      // 使用refs调用表单的验证方法validate
      // validate接收回调函数 valid验证通过为true 失败为false
      this.$refs[formName].validate((valid) => {
        // 如果表单验证通过
        if (valid) {
          alert("submit!");
        } else {
          console.log("error submit!");
          return false;
        }
      });
    },
    // 使用refs调用表单的重置方法
    resetForm(formName) {
      // 调用resetFields方法重置表单字段
      this.$refs[formName].resetFields();
    },
  },
};
</script>
