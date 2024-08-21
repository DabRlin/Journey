<template>
  <!-- 阻止提交事件并调用formData输出到控制台 -->
  <form @sumbit.prevent="submitForm">
    <!-- 传入子组件的label参数 -->
     <!-- 此处的v-model="formData.username相当于两段代码" -->
      <!-- :value="formData.username和@input="formData.username=$event.value" -->
       <!-- 实现了父子组件数据的双向绑定 -->
    <InputField v-model="formData.username" label="Username"></InputField>
    <InputField v-model="formData.email" label="Email"></InputField>
    <button type="submit">Sumbit</button>
  </form>
</template>

<script>
import InputField from "./InputField.vue";
import InputField from "./InputField.vue";
import InputField from "./InputField.vue";

export default {
  components: {
    InputField,
  },
  data() {
    return {
      formData: {
        username: "",
        email: "",
      },
    };
  },
  methods: {
    submitForm() {
      console.log(this.formData);
    },
  },
};
</script>
