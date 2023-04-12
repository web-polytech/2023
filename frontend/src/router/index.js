import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../pages/HomePage.vue';
import AboutPage from '../pages/AboutPage.vue';
import EntrancePage from '../pages/EntrancePage.vue';
import NewsPage from '../pages/NewsPage.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage,
    },
    {
      path: '/about',
      name: 'about',
      component: AboutPage,
    },
    {
      path: '/entrance',
      name: 'entrance',
      component: EntrancePage,
    },
    {
      path: '/news',
      name: 'news',
      component: NewsPage,
    },
  ],
});

export default router;
