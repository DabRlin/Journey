//routes是一个数组，包含所有路由的配置对象
//在router-link中使用动态路由 router-link可以生成带有参数的url
{
  /* <router-link :to="`/todo/${todo.id}`">View Details</router-link> */
}

const routers = [
  //会匹配todo/1 todo/2等不同的url 并将id参数传递给TodoDetailComponent
  { path: "/todo/:id", component: TodosComponent },
];

//嵌套路由
const routes = [
  {
    path: "/todos",
    component: TodosComponent,
    //children数组，定义todos路径下的嵌套路由
    children: [
      { path: "", component: AllTodosComponent },
      { path: "active", component: ActiveTodosComponent },
      { path: "completed", component: CompletedTodosComponent },
    ],
  },
];

export default {
  data() {
    return {
      todo: null,
    };
  },
  computed: {
    //todoId是一个计算属性，用来返回当前路由id参数值
    todoId(){
        return this.$route.params.id
    }
  },
  //在组件实例被创建后立即调用
  created() {
    //获取路由中传递的id参数
    const todoId = this.$route.params.id;
    //调用fetchTodoDetail方法并传入参数
    this.fetchTodoDetail(todoId);
  },
  methods: {
    fetchTodoDetail(id) {
      //假设fetchTodoById是一个API请求函数
      fetchTodobyId(id).then((response) => {
        this.todo = response.data;
      });
    },
  },
};
