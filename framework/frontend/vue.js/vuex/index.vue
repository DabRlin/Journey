<template>
  <h1>你好</h1>
</template>

<script>
export default {
  computed: {
    todos() {
      //使用state
      return this.$store.state.todos;
    },
    filteredTodos() {
      //使用getters
      return this.$store.getters.filteredTodos;
    },
  },
  methods: {
    addTodo() {
      //调用mutations中的方法
      this.$store.commit("ADD_TODO", {
        text: this.newTodoText,
        compeleted: false,
      });
      this.newTodoText = "";
    },
    async fetchTodos() {
      const response = await fetch("api/todos");
      const todos = await response.json();
      //异步调用actions中的方法
      todos.forEach((todo) => this.$store.dispatch("addTodo", todo));
    },
  },
};
</script>
