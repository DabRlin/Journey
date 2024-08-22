//模块化 可复用的全局化管理

import Vue from "vue";

const DataFormatPlugin = {
  install(Vue) {
    //创建实例方法接收两个参数
    Vue.prototype.$formatData = function (date, format) {
      //设置格式 numeric是完整数字格式 long是完整名称显示
      const options = { year: "numeric", month: "long", day: "numeric" };
      //将日期转化为特定语言环境的字符串表示形式
      return new Date(date).toLocaleDateString(undefined, options); //undefined指定默认语言环境
    };
  },
};

Vue.use(DataFormatPlugin);
