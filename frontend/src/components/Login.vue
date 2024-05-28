<template>
    <div class="login">
      <h2>Login</h2>
      <form @submit.prevent="login">
        <input type="text" placeholder="Username" v-model="username" />
        <input type="password" placeholder="Password" v-model="password" />
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Login',
    data() {
      return {
        username: '',
        password: ''
      }
    },
    methods: {
      login() {
        // Handle the login logic
        console.log(`Logging in with username: ${this.username} and password: ${this.password}`);
      }
    }
  }
  </script>
  
  <style scoped>
  .login form {
    display: flex;
    flex-direction: column;
  }
  .login input {
    margin-bottom: 10px;
    padding: 8px;
  }
  </style>
  