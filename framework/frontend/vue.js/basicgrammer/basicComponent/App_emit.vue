<template>
  <div id="app">
    <button-component @button-clicked="handleButtonClick"></button-component>
  </div>
</template>

<script>
import ButtomComponent from "./ButtomComponent.vue";

//导出组件供其他组件或实例使用
export default {
  components: {
    ButtomComponent,
  },
  methods:{
    handleButtonClick(){
        alert("Button was clicked")
    }
  }
};
</script>
