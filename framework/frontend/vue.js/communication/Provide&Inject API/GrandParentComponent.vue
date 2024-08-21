<template>
  <div>
    <ParentComponent></ParentComponent>
  </div>
</template>

<script>
import ParentComponent from "./ParentComponent.vue";

export default {
  components: {
    ParentComponent,
  },
  //使用provide将数据传递给后代组件
  provide(){
    return{
        shareData:'This is data from GrandParent'
    }
  }
};
</script>
