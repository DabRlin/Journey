<template>
  <div>
    <el-card>
      <h3>{{ user.name }}</h3>
      <p>{{ user.email }}</p>
    </el-card>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  computed: {
    ...mapGetters(["user"]),
  },
  //created钩子 在组件被创建的时候调用
  created() {
    this.$store.dispatch("fetchUser", this.$route.params.id);
  },
};
</script>
