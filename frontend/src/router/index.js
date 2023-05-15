import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/pages/HomePage.vue';
import AboutPage from '@/pages/AboutPage.vue';
import EntrancePage from '@/pages/EntrancePage.vue';
import NewsPage from '@/pages/NewsPage.vue';
import FeedbackPage from '@/pages/FeedbackPage.vue';
import SchoolLifePage from '@/pages/SchoolLifePage.vue';
import AuthPage from '@/pages/AuthPage.vue';


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
    {
      path: '/school-life',
      name: '/school-life',
      component: SchoolLifePage,
    },
    {
      path: '/feedback',
      name: 'feedback',
      component: FeedbackPage,
    },
    {
      path: '/auth',
      name: 'auth',
      component: AuthPage,
    },

  ],
});

export default router;
