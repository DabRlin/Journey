<template>
  <li>{{ todo.text }}</li>
</template>

<script>
export default {
  props: ["todo"],
  //生命周期钩子
  create(){
    console.log("this is ")
  },
  mounted(){
    console.log("this is ")
  },
  beforeCreate(){
    console.log("this is ")
  },
  beforeMount(){
    console.log("this is ")
  },
  updated(){
    console.log("this is ")
  },
  beforeUpdate(){
    console.log("this is ")
  },
  destoryed(){
    console.log("this is ")
  },
  beforeDestoryed(){
    console.log("this is ")
  }
};
</script>

<style scoped>
li {
  list-style: none;
}
</style>
