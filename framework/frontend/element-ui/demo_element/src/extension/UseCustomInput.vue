<template>
  <div>
    <custom-input
      v-model="inputValue"
      @custom-click="handelCustomClick"
    ></custom-input>
    <p>Input value:{{ inputValue }}</p>
  </div>
</template>

<script>
import CustomInput from "./CustomInput.vue";

export default {
  data() {
    return {
      inputValue: "",
    };
  },
  components: {
    customInput,
  },
  method: {
    handelCustomClick() {
      alert("Button clicked!");
    },
  },
};
</script>
