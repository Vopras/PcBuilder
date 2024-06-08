<template>
  <div class="build-pc">
    <h1>Build Your PC</h1>
    <div class="input-group" v-for="item in items" :key="item.label">
      <label :for="item.label">{{ item.label }}</label>
      <input type="text" :id="item.label" v-model="item.value" @input="updateSuggestions2(item)" />
      <ul v-if="item.suggestions.length">
        <li v-for="suggestion in item.suggestions" :key="suggestion" @click="selectSuggestion(item, suggestion)">
          {{ suggestion }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'BuildPC',
  data() {
    return {
      items: [
        { label: 'CPU', value: '', suggestions: [] },
        { label: 'Motherboard',  value: '', suggestions: [] },
        { label: 'GPU', value: '', suggestions: [] },
        { label: 'Memory',  value: '', suggestions: [] },
        { label: 'Power Supply',  value: '', suggestions: [] },
        { label: 'Storage',  value: '', suggestions: [] },
        { label: 'Case',  value: '', suggestions: [] },
        { label: 'CPU Cooler',  value: '', suggestions: [] },
      ],
    };
  },
  methods: {
    updateSuggestions2(item) {
  // Clear suggestions immediately when input changes
  item.solutions = [];

  if (!item.value) {
    return; // No further action if input is empty
  }

  let url = ''; // Default URL
  // Determine the URL based on item.label
  switch (item.label) {
    case 'CPU Cooler':
      url = `http://127.0.0.1:5000/search/cpu-cooler/${item.value}`;
      break;
    case 'GPU':
      url = `http://127.0.0.1:5000/search/video-card/${item.value}`;
      break;
    case 'Storage':
      url = `http://127.0.0.1:5000/search/internal-hard-drive/${item.value}`;
      break;
    case 'Power Supply':
      url = `http://127.0.0.1:5000/search/power-supply/${item.value}`;
      break;
    default:
      url = `http://127.0.0.1:5000/search/${item.label.toLowerCase()}/${item.value}`;
      break;
  }

  // Execute the API request
  axios.get(url)
    .then(response => {
      console.log('Type of response.data:', typeof response.data); // Check the type
      if (typeof response.data === 'string') {
        // Parse if it's a string
        response.data = JSON.parse(response.data);
      }
      if (Array.isArray(response.data)) {
        item.suggestions = response.data.map(obj => obj.name);
      } else {
        console.error('Data format is incorrect:', response.data);
        item.suggestions = [];
      }
    })
    .catch(error => {
      console.error('Error fetching suggestions:', error);
      item.suggestions = [];
    });
},
    selectSuggestion(item, suggestion) {
      item.value = suggestion;
      item.suggestions = [];
    }
  }
}
</script>

<style scoped>
.input-group {
  margin-bottom: 20px;
}
.input-group ul {
  list-style: none;
  padding: 0;
}
.input-group li {
  cursor: pointer;
  padding: 5px;
  background-color: #eee;
}
.input-group li:hover {
  background-color: #ddd;
}
</style>
