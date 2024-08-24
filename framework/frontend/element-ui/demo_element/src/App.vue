<template>
  <div id="app">
    <element-button></element-button>
    <element-u-i></element-u-i>
    <element-input></element-input>
    <element-dialog></element-dialog>
    <element-form></element-form>
    <element-table></element-table>
    <element-try></element-try>
  </div>
</template>

<script>
import ElementButton from "./components/ElementButton.vue";
import ElementUI from "./components/ElementUI.vue";
import ElementInput from "./components/ElementInput.vue";
import ElementDialog from "./components/ElementDialog.vue";
import ElementForm from "./components/ElementForm.vue";
import ElementTable from "./components/ElementTable.vue";
import ElementTry from "./components/ElementTry.vue";

export default {
  name: "App",
  components: {
    ElementUI,
    ElementButton,
    ElementInput,
    ElementDialog,
    ElementForm,
    ElementTable,
    ElementTry,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
