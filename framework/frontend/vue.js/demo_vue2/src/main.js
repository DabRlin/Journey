import Vue from "vue";
import App from "./App.vue";
//导入Vue和VueRouter
import VueRouter from "vue-router";
//导入vuex插件
import Vuex from "vuex";
//javascript会默认寻找目录中的index.js
import store from "./store";

//导入相关组件
import CompletedTodosComponent from "./components/CompletedTodosComponent.vue";
import HomeComponent from "./components/HomeComponent.vue";
import TodosComponent from "./components/TodosComponent.vue";

//导入插件
import MyPlugin from "./my-plugin";

Vue.config.productionTip = false;

//是不必要的操作  因为在store/index.html的文件夹中已经注册过了
//注册vue插件
Vue.use(Vuex);
//使用vue插件
Vue.use(VueRouter);

//全局注册自定义指令
Vue.directive("focus", {
  //当绑定元素插入DOM中执行
  inserted: function (el) {
    el.focus();
  },
});

const MyPlugin = {
  //vue表示实例 options传递插件配置信息如api地址等
  install(Vue, options) {
    //添加全局方法
    Vue.myGlobalMethod = function () {
      console.log("This is a global method");
    };
    //添加全局指令
    Vue.directive("my-directive", {
      bind(el, binding, vnode) {
        el.style.color = binding.value;
      },
    });
    //添加实例方法
    //此处的methodOptions是可在调用时候额外传递的配置和数据
    Vue.prototype.$myMethod = function (methodOptions) {
      console.log("This is an instance method");
    };
  },
};

//注册安装插件
Vue.use(MyPlugin);

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
  store,
  router,
  render: (h) => h(App),
  // //调用插件的实例方法
  // created() {
  //   this.$myMethod();
  // },
}).$mount("#app");
