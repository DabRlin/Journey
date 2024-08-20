const state = {
  todos: [],
};

//multations需要提交来更改应用状态
const mutations = {
  ADD_TODO(state, todo) {
    state.todos.push(todo);
  },
};

const actions = {
  //这里的commit是用来触发mutation的方法
  //actions不直接修改状态，而是荣光提交mutation来间接修改状态
  addTodo({ commit }, todo) {
    //commit是解构写法，从context对象中提取commit方法
    commit("ADD_TODO,todo");
  },
};

const getters = {
  todos(state) {
    return state.todos;
  },
};

export default {
  state,
  mutations,
  actions,
  getters,
};
