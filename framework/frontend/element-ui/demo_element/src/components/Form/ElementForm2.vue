<!-- 使用Form和FormItem进行表单布局 -->

<template>
  <el-form :model="form" :rules="rules" ref="form" label-width="120px">
    <el-form-item label="Username" prop="username">
      <el-input v-model="form.username"></el-input>
    </el-form-item>
    <el-form-item label="Password" prop="password">
      <el-input v-model="form.password"></el-input>
    </el-form-item>
    <el-form-item label="Gender" prop="gender">
      <el-select v-model="form.gender">
        <el-option label="Male" value="male"></el-option>
        <el-option label="Female" value="female"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm('form')"></el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: "",
        password: "",
        gender: "",
      },
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
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert("Form submitted!");
        } else {
          console.log("Error submitting form");
          return false;
        }
      });
    },
  },
};
</script>
