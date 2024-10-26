<template>
  <SignUp />
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
// npm run serve (start vue server)
// json-server --watch db.json (to start api)
import SignUp from './components/SignUp.vue'

export default {
  name: 'App',
  components: {
    SignUp
  }
}
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
