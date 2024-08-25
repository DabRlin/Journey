<!-- 注册表单验证 -->

<template>
  <el-form :model="form" :rules="rules" ref="form" label-width="120px">
    <el-form-item label="Username" prop="username">
      <el-input v-model="form.username"></el-input>
    </el-form-item>
    <el-form-item label="Email" prop="email">
      <el-input v-model="form.email"></el-input>
    </el-form-item>
    <el-form-item label="Password" prop="password">
      <el-input type="password" v-model="form.password"></el-input>
    </el-form-item>
    <el-form-item label="Gender" prop="gender">
      <el-select v-model="form.gender" placeholder="Select">
        <el-option label="Male" value="male"></el-option>
        <el-option label="Female" value="female"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm('form')">Register</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: "",
        email: "",
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
          {
            min: 3,
            max: 10,
            message: "Length should be 3 to 10 characters",
            trigger: "blur",
          },
        ],
        email: [
          {
            required: true,
            message: "Please input your email address",
            trigger: "blur",
          },
          {
            type: "email",
            message: "Please input a valid email address",
            trigger: "blur",
          },
        ],
        password: [
          {
            required: true,
            message: "Please input your password",
            trigger: "blur",
          },
          {
            min: 6,
            message: "Password length should be at least 6 characters",
            trigger: "blur",
          },
        ],
        gender: [
          {
            required: true,
            message: "Please select your gender",
            trigger: "change",
          },
        ],
      },
    };
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert("Registration successful!");
        } else {
          console.log("Error during registration");
          return false;
        }
      });
    },
  },
};
</script>
