<template>
  <router-link :to="to">
    <button class="nav-button">
      <slot></slot>
    </button>
  </router-link>
</template>

<script>
export default {
  props: ["to"],
};
</script>

<style>
.nav-button {
  background-color: #42b983;
  border: none;
  color: white;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 4px;
}

.nav-button:hover {
  background-color: #357a38;
}
</style>