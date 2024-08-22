const MyPlugin = {
  install(Vue, options) {
    //定义全局方法
    Vue.myGlobalMethod = function () {
      console.log("This is a global method");
    };
    //定义实例方法
    Vue.prototype.$myMethod = function (methodOptions) {
      console.log("This is an instance method");
    };
  },
};

//定义导出
export default MyPlugin;
