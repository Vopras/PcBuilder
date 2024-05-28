<template>
    <div class="build-pc">
      <h2>Build Your PC</h2>
      <form>
        <label for="processor">Processor:</label>
        <select id="processor">
          <option value="intel">Intel</option>
          <option value="amd">AMD</option>
        </select>
  
        <label for="graphics">Graphics Card:</label>
        <select id="graphics">
          <option value="nvidia">Nvidia</option>
          <option value="amd">AMD</option>
        </select>
  
        <button type="submit">Submit Your Build</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'BuildPC',
    mounted() {
        console.log("aaaaaaaaaaa");
    }
  };
  </script>
  
  <style scoped>
  .build-pc {
    margin-top: 20px;
  }
  .build-pc form {
    display: flex;
    flex-direction: column;
  }
  .build-pc label {
    margin-top: 10px;
  }
  </style>
  