// Vuex的作用是实现全局的状态管理 炳简化组件之间的通信

import Vue from "vue";
import Vuex from "vuex";
import todos from "./modules/todos";

Vue.use(Vuex);

//创建了Store实例
//默认导出也是这个实例
export default new Vuex.Store({
  //存储数据 定义整个应用所需要1的全局状态数据
  state: {
    count: 0,
    todos: [
      {
        id: 1,
        text: "Learn Vue",
        done: true,
      },
      {
        id: 2,
        text: "Learn Vuex",
        done: false,
      },
    ],
  },
  //计算属性  基于state派生出新的数据
  getters: {
    doneTodos: (state) => {
      return state.todos.filter((todo) => todo.done);
    },
  },
  //修改Vuex state 相当于methods
  mutations: {
    increment(state) {
      state.count++;
    },
  },
  //异步操作，最终通过提交mutations修改最终状态
  //允许异步操作 相当于对mutations进行一个封装
  actions: {
    incrementAsync({ commit }) {
      setTimeout(() => {
        commit("increment");
      }, 1000);
    },
  },
  modules: {
    todos,
  },
});
