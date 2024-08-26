import Vue from "vue";
import Router from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import UserList from "@/extension/test/UserList.vue";
import UserDetails from "@/extension/test/UserDetails.vue";

Vue.use(Router);

export default new Router({
  model: "history", //启用html5历史模式
  routes: [
    {
      path: "/Home",
      name: "Home",
      component: Home,
    },
    {
      path: "/about",
      name: "About",
      component: About,
    },
    {
      path: "/",
      name: "UserList",
      component: UserList,
    },
    {
      path: "/user/:id", //动态路径参数
      name: "UserDetails",
      component: UserDetails,
      // 启用props会自动将路由路径中的params作为props传递给组件
      props: true, //将路由参数作为props传递给组件
    },
  ],
});
