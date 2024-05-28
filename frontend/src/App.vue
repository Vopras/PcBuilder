<template>
    <div id="app">
      <Navbar />
      <router-view/>
      <!-- <Greeting/> -->
      <!-- <Selector></Selector> -->
    </div>
  </template>
  
  <script>
  import Greeting from './components/Greetings.vue'
  import Selector from './components/Selector.vue';
  import Navbar from './components/Navbar.vue';
  // import BuildPC from './components/BuildPC.vue';
  // import Home from './components/Home.vue';
  // import Login from './components/Navbar.vue';
  
  export default {
    name: 'App',
    components: {
      Greeting,
      Selector,
      Navbar,
      // BuildPC,
      // Home,
      // Login,
    }
  }
  </script>
  
  <style>
  /* Global styles for your app */
  </style>
  