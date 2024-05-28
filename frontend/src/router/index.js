import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import BuildPC from '../components/BuildPC.vue';
import Login from '../components/Login.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/build',
    name: 'BuildPC',
    component: BuildPC
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
