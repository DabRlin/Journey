import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    count: 0,
    users: [],
    user: {},
  },
  mutations: {
    increment(state) {
      state.count++;
    },
    //设置users
    setUsers(state, users) {
      state.users = users;
    },
    //设置user
    setUser(state, user) {
      state.user = user;
    },
  },
  actions: {
    increment({ commit }) {
      commit("increment");
    },
    //向后端发送请求获取全部users数据
    async fetchUsers({ commit }) {
      const response = await fetch("/api/users");
      const data = await response.json();
      commit("setUsers", data);
    },

    //向后端发送请求获取具体iduser数据
    async fetchUser({ commit }, id) {
      const response = await fetch(`api/users/${id}`);
      const data = await response.json();
      commit("setUser", data);
    },
  },
  getters: {
    count: (state) => state.count,
    users: (state) => state.users,
    user: (state) => state.user,
  },
});
