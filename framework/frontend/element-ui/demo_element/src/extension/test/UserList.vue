<template>
  <div>
    <el-table :data="users">
      <el-table-column prop="name" label="Name"></el-table-column>
      <el-table-column prop="email" label="Email"></el-table-column>
      <el-table-column>
        <template slot-scope="scope">
          <el-button @click="viewDetails(scope.row)">View Details</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { mapActions } from "vuex";

export default {
  computed: {
    ...mapGetters(["users"]),
  },
  methods: {
    ...mapActions(["fetchUsers"]),
    viewDetail(user) {
      //使用vue router的push方法跳转到userdetails路由 并传递id参数
      // params必须与name一起使用 query可以与path一起使用
      this.$route.push({ name: "UserDetails", parms: { id: user.id } });
    },
  },
  //组件被创建的时候调用
  created() {
      this.fetchUsers();
    },
};
</script>
