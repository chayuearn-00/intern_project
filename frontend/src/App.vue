<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App"
}
</script>

<style>
* {
  font-family: "Inter", sans-serif !important;
}
 
#app {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  background-color: #f7f9fc !important;
  overflow: hidden;
  overflow-x: visible;
}
</style>