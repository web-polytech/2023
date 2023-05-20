import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '@/pages/HomePage.vue';
import AboutPage from '@/pages/AboutPage.vue';
import EntrancePage from '@/pages/EntrancePage.vue';
import NewsPage from '@/pages/NewsPage.vue';
import FeedbackPage from '@/pages/FeedbackPage.vue';
import SchoolLifePage from '@/pages/SchoolLifePage.vue';
import AuthPage from '@/pages/AuthPage.vue';
import ProfilePage from '@/pages/ProfilePage.vue';
import The404 from '@/components/The404.vue';


const router = createRouter({
  history: createWebHistory(
    import.meta.env.BASE_URL),
  routes: [{
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
    name: 'school-life',
    component: SchoolLifePage,
  },
  {
    path: '/feedback',
    name: 'feedback',
    component: FeedbackPage,
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfilePage,
  },
  {
    path: '/login',
    name: 'login',
    component: AuthPage,
    props: () => ({ auth: 'login' }),
  },
  {
    path: '/register',
    name: 'register',
    component: AuthPage,
    props: () => ({ auth: 'register' }),
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'error404',
    component: The404,
  },
  ],
});

export default router;
