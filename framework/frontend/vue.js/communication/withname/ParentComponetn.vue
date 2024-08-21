<template>
  <div>
    <h2>Parent Component</h2>
    <ChildComponent>
      <!-- 插入具名插槽中 -->
      <template v-slot:header>
        <h3>This is a header from parent.</h3>
      </template>
      <!-- 插入默认插槽中 -->
      <p>This content is passed to the default slot.</p>
    </ChildComponent>
  </div>
</template>

<script>
import ChildComponent from "./ChildComponent.vue";
import ChildComponent from "./ChildComponent.vue";

export default {
  components: {
    ChildComponent,
  },
};
</script>
