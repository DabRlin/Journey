<template>
  <div>
    <el-button @click="increment">Increment</el-button>
    <p>Count:{{ count }}</p>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  computed: {
    ...mapGetters(["count"]),
  },
  methods: {
    ...mapActions(["increment"]),
  },
};
</script>
