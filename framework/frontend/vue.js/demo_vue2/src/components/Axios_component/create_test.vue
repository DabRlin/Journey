<template>
  <div>
    <ul>
      <li v-for="todo in todos" :key="todo.id">{{ todo.title }}</li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
export default {
  date() {
    return {
      todos: [],
    };
  },
  created() {
    axios
      .get("http://jsonplaceholder.typicode.com/todos")
      .then((response) => {
        this.todos = response.data;
      })
      .catch((error) => {
        console.error("There was an error fetching the todos:", error);
      });
  },
};
</script>
