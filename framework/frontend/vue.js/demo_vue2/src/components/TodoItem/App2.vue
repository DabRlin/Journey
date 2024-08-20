<template>
    <div>
      <!-- 回车进行代办事件添加 -->
      <input v-model="newTodo" @keyup.enter="addTodo" placeholder="Add a new task" />
      <ul>
          <!-- 监听removeTodo冒泡和toggleComplete冒泡 -->
           <!-- todo和item进行绑定 进行父组件向子组件的传值，从而实现了子组件的显示 -->
            <!-- 这里的remove和toggle-completed都接收了事件传递的参数 -->
        <todo-item
          v-for="item in todos"
          :key="item.id"
          :todo="item"
          @remove="removeTodo"
          @toggle-complete="toggleComplete">
        </todo-item>
      </ul>
    </div>
  </template>
  
  <script>
  import TodoItem from './TodoItem.vue';
  
  export default {
    components: { TodoItem },
    //data是一个函数
    data() {
      return {
        newTodo: '',
        todos: []
      };
    },
    //method是一个对象
    methods: {
      addTodo() {
        //去掉空格字段来判断是否有效输入
        if (this.newTodo.trim()) {
          //插入todo 具有id text compeleted三个字段
          this.todos.push({ id: Date.now(), text: this.newTodo, completed: false });
          this.newTodo = '';
        }
      },
      removeTodo(id) {
        //filiter函数会遍历数组
        //使用filiter函数建立新数组 满足条件进入 不满足条件的被筛除
        this.todos = this.todos.filter(todo => todo.id !== id);
      },

      //从子组件发射的事件接收id参数 vue自己封装好的方法
      toggleComplete(id) {
        //使用find查找对应的元素
        const todo = this.todos.find(todo => todo.id === id);
        if (todo) {
          todo.completed = !todo.completed;
        }
      }
    }
  };
  </script>
  