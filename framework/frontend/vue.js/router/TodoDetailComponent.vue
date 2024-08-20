<template>
  <div>
    <h1>Todo Detail</h1>
    <p>Id:{{ todo.id }}</p>
    <p>Text:{{ todo.text }}</p>
  </div>
</template>

<script>
export default {
  name: "TodoDetailComponent",
  data() {
    return {
      todo: {},
    };
  },
  computed: {
    todoId() {
      return this.$route.params.id;
    },
  },
  created() {
    this.fetchTodo();
  },
  methods: {
    fetchTodo() {
      //这里可以发送htttp请求之类的获取数据
      const todoId = this.todoId;
      const todos = [
        { id: "1", text: "Learn Vue.js" },
        { id: "2", text: "Build a Vue app" },
      ];
      this.todo = todos.find(todo => todo.id=todoId)||{}//当找不到匹配的则通过||或操作返回空{}
    },
  },
};
</script>
