<template>
  <div>
    <nav>
      <!-- 直接使用router-link标签 -->
      <router-link to="/">Home</router-link>
      <router-link to="/todos">All Todos</router-link>
      <router-link to="/completed">Completed Todos</router-link>
      <!-- 使用函数式编程进行导航 -->
      <button @click="goToHome">Home</button>
      <button @click="goToTodos">All Todos</button>
      <button @click="goToCompleted">Completed Todos</button>
      <!-- 使用自定义按钮组件 -->
      <custom-button to="/">Click</custom-button>
      <button @click="navigateTo('/')">Click Me!</button>
      <router-link to="/todos">
        <!-- 事件冒泡 -->
        <button>Click Me!</button>
      </router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
import CustomButton from "./components/CustomButton.vue";

export default {
  name: "App",
  components: {
    CustomButton,
  },
  methods: {
    goToHome() {
      //this.router.push是vue router提供的一个功能
      //this 指的是vue实例
      //及说一个路由路径作为参数 导航到指定路径
      this.$router.push("/");
    },
    goToTodos() {
      this.$router.push("/todos");
    },
    goToCompleted() {
      this.$router.push("/completed");
    },
    replaceWithHome() {
      //replace同push的区别是replace不会留下记录，会替换当前的记录 适用于重定向等
      this.$router.replace("/");
    },
    //使用路由参数
    goToUserProfile(userId) {
      this.$router.push({ path: `/user/${userId}` });
    },
    //返回当前路由信息
    currtentPath() {
      return this.$router.currtentRoute.path;
    },
    navigateTo(path) {
      this.$router.push(path);
    },
  },
};
</script>
