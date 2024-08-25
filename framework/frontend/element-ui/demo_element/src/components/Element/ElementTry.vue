<template>
  <!-- 绑定对象form -->
  <el-form :model="form" :rules="rules" ref="form" label-width="120px">
    <!-- 用prop对form的属性username进行验证 -->
    <el-form-item label="Username" prop="username">
      <el-input v-model="form.username"></el-input>
    </el-form-item>
    <!-- 对password进行验证 -->
    <el-form-item label="Password" prop="password">
      <el-input v-model="form.password"></el-input>
    </el-form-item>
    <!-- 对性别进行验证 -->
    <el-form-item label="Gender" prop="gender">
      <!-- 选择性别与v-model关联 -->
      <el-select v-model="form.gender" placeholder="Select">
        <el-option label="Male" value="male"></el-option>
        <el-option label="Female" value="female"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item>
      <!-- 提交表单 -->
      <el-button type="primary" @click="submitForm('form')">Register</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  data() {
    return {
      //定义表单结构
      form: {
        username: "",
        password: "",
        gender: "",
      },
      //验证方法
      rules: {
        username: [
          {
            required: true,
            message: "Please input your username",
            trigger: "blur",
          },
        ],
        password: [
          {
            required: true,
            message: "Please input your password",
            trigger: "blur",
          },
        ],
        gender: [
          {
            required: true,
            message: "Please input your gender",
            trigger: "blur",
          },
        ],
      },
    };
  },
  methods: {
    //进行提交表单的验证
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert("Form submittied!");
        } else {
          console.log("Error submitting form");
          return false;
        }
      });
    },
  },
};
</script>
