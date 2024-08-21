<template>
  <div>
    <h1>Parent Component</h1>
    <!-- childcomponent中的内容会被slot插槽显示 -->
    <ChildComponent>
      <p>This content is passed from the parent.</p>
    </ChildComponent>
  </div>
</template>

<script>
import ChildComponent from "./ChildComponent.vue";
export default {
  components: {
    ChildComponent,
  },
};
</script>
