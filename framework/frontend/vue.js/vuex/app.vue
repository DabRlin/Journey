<template>
  <div>
    <input
      v-model="newTodo"
      @keyup.enter="addTodo"
      placeholder="Add a new Todo"
    />
    <!-- 按照不同的条件进行筛选 -->
    <button @click="setFilter('all')">All</button>
    <button @click="setFilter('active')">Active</button>
    <ul>
      <!-- 遍历展示所有Todo的内容 -->
      <li v-for="(todo, index) in filteredTodos" :key="index">
        {{ todo.text }}
        <button @click="removeTodo(index)">Remove</button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newTodo: "",
    };
  },
  computed: {
    // 使用 store 的 getter 部分的 filteredTodos 来获取筛选的列表
    filteredTodos() {
      return this.$store.getters.filteredTodos;
    },
  },
  methods: {
    // 添加 Todo
    addTodo() {
      if (this.newTodo.trim()) {
        this.$store.dispatch("addTodo", {
          text: this.newTodo,
          completed: false,
        });
        this.newTodo = "";
      }
    },
    // 移除 Todo
    removeTodo(index) {
      this.$store.dispatch("removeTodo", index);
    },
    // 筛选 Todo
    setFilter(filter) {
      this.$store.dispatch("setFilter", filter);
    },
  },
};
</script>
