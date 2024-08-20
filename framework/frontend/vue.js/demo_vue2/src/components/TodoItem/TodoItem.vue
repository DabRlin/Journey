<template>
    <!-- 绑定todo.completed -->
     <!-- 使用v-bind语法糖进行数据的绑定 如果是true，就是completed类-->
      <!-- 使用了vue的动态class绑定，如果todo.completed为真，则添加到元素上 -->
    <li: class="{completed:todo.completed}" @click="toggleComplete">
        {{ todo.text }}
        <button @click.stop="removeItem">Delete</button>
    </li:>
</template>

<script>
export default {
    //接收父组件传递过来的对象，进行组件的显示
    props: ['todo'],
    methods: {
        //触发事件向上冒泡被父组件进行处理
        toggleComplete() {
            this.$emit("toggle-complete", this.todo.id);

        },
        //同上
        removeItem() {
            this.$emit("remove", this.todo.id)
        }
    }
}
</script>

<!-- 通过class来对completed类进行处理 -->
<style scoped>
.completed{
    text-decoration: line-through;
}
</style>