import Vue from "vue";
import App from "./App.vue";
//导入Vue和VueRouter
import VueRouter from "vue-router";

//导入相关组件
import CompletedTodosComponent from "./components/CompletedTodosComponent.vue";
import HomeComponent from "./components/HomeComponent.vue";
import TodosComponent from "./components/TodosComponent.vue";

Vue.config.productionTip = false;

//使用vue插件
Vue.use(VueRouter);

//定义路由规则 path对应应用路由 companent对应组件
const routes = [
  { path: "/", component: HomeComponent },
  { path: "/todos", component: TodosComponent },
  { path: "/completed", component: CompletedTodosComponent },
  //嵌套路由
];

//创建VueRouter实例将routes配置传递给它
const router = new VueRouter({
  routes,
});

//将router实例传递给Vue实例 使得Vue实例可以使用路由功能
new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
