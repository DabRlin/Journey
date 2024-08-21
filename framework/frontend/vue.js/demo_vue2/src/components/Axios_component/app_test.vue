<template>
  <div>
    <input v-model="newTode" @keyup.enter="addTodo" placeholder="Add a new Todo"
  </div>
  <ul>
    <!-- 遍历显示todo的title -->
    <li v-for="(todo, index) in todos" :key="index">
      {{ todo.title }}
      <button @click="removeTodo(index)">Remove</button>
    </li>
  </ul>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      todos: [],
      newTodo: "",
    };
  },
  methods: {
    //发送http请求，接收返回数据到Todos
    fetchTodo() {
      axios
        .get(`https://jsonplaceholder.typicode.com/todos`)
        .then((response) => {
          this.todos = response.data.slice(0, 10);
        })
        .catch((error) => {
          console.error("There was an error fetching the todos:", error);
        });
    },
    //添加todo
    addTodo() {
      if (this.newTodo.trim()) {
        this.todos.push({ title: this.newTodo, completed: false });
        this.newTodo = "";
      }
    },
    //删除todo
    removeTodo() {
      this.todos.splice(index, 1);
    },
  },
  created() {
    this.fetchTodo();
  },
};
</script>
