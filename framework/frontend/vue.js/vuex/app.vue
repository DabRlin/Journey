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
  //使用store的getter部分的filteredTodos来获取筛选的的列表
    filteredTodos() {
      return this.$store.getters.filteredTodos;
    },
  },
  methods: {
    //添加Todo
    addTodo() {
      if (this.newTodo.trim()) {
        this.$store.dispatch("addTodo", { text: this.newTodo, compeleted: false });
        this.newTodo=""
      }
    },
    //移除Todo
    removeTodo(index)({
        this.$store.dispatch("removeTodo",index)
    })
    //筛选Todo
    setFilter(filter){
        this.$store.dispatch("setFilter",filter)
    }
  },

};
</script>
