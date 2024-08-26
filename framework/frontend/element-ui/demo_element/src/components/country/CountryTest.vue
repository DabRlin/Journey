<template>
  <div>
    <el-button @click="changeLanguage('en')">English</el-button>
    <el-button @click="changeLanguage('zh')">中文</el-button>
    <p>{{ $t("message.hello") }}</p>
  </div>
</template>

<script>
export default {
  methods: {
    changeLanguage(lang) {
      this.$i18n.locale = lang;
    },
  },
};
</script>
