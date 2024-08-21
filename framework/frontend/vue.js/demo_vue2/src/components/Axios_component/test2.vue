<template>
  <div>
    <li v-for="todo in todos" :key="todo.id">{{ todo.title }}</li>
  </div>
  <button @click="loadmore">Load More</button>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      todos: [],
      page: 1,
    };
  },
  methods: {
    loadMore() {
      //使用axios发送http请求并获取数据到data的todos
      axios
        .get(`http://jsonplaceholder.typicode.com/todos?page=${this.page}`)
        .then((response) => {
          //使用...展开运算符  ...展开运算符将数组中的每一个元素展开
          //此处是展开元素来组成数组 ...是ES6的语法
          this.todos = [...this.todos, ...response.data];
          this.page++;
        })
        .catch((error) => {
          console.error("There was an error fetchhing more todos:", error);
        });
    },
  },
  //再创建实例时调用loadMore方法
  created() {
    this.loadMore();
  },
};
</script>
