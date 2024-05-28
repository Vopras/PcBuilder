<template>
    <div class="Navbar"> 
        <div class="navbar_buttons">
            <h1> hello there</h1>
            <router-link to="/">Home</router-link>
            <router-link to="/build">Build a PC</router-link>
            <button></button>
        </div>
        <div class="login-zone">
            <button> Login </button>
            <button> Register </button>
        </div>
    </div>
    
</template>

<script>
  export default {
    


  }
</script>

<style>


    .login-zone {
        float: right;
        margin-left: 3px; /* Space between buttons */
    }

</style>
