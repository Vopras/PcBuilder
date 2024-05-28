// Import the createApp function from the Vue package
import { createApp } from 'vue';
// Import the root component App from the same directory
import App from './App.vue';
import router from './router'; // import the router

// Create a new application instance by calling createApp(), and pass the root component App
// Then call mount() on the application instance and specify the DOM element to mount to, using its ID
createApp(App)
    .use(router)
    .mount('#app');
