import Vue from "vue";
import App from "./App.vue";
import VueI18n from "vue-i18n";
//引入Element-ui
import ElementUI from "element-ui";
//引入element-ui样式
import "element-ui/lib/theme-chalk/index.css";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;

//注册使用vueI18n插件
Vue.use(VueI18n);

//注册使用element-ui
Vue.use(ElementUI, { i18n: (key, value) => i18n.t(key, value) });

const messages = {
  en: {
    message: {
      hello: "hello world",
    },
  },
  zh: {
    message: {
      hello: "你好，世界",
    },
  },
};

const i18n = new VueI18n({
  locale: "en", // set locale
  messages, // set locale messages
});

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
