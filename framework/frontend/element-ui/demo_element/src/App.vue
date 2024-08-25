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
import ElementButton from "./components/Element/ElementButton.vue";
import ElementUI from "./components/Element/ElementUI.vue";
import ElementInput from "./components/Element/ElementInput.vue";
import ElementDialog from "./components/Element/ElementDialog.vue";
import ElementForm from "./components/Element/ElementForm.vue";
import ElementTable from "./components/Element/ElementTable.vue";
import ElementTry from "./components/Element/ElementTry.vue";

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
