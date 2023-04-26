import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';
import components from '@/components/UI';
import YmapPlugin from 'vue-yandex-maps';
const app = createApp(App);

const settings = {
  apiKey: '343c1fe6-63fe-4963-bb72-b23c992e47b2',
  lang: 'ru_RU',
  coordorder: 'latlong',
  enterprise: false,
  version: '2.1',
};
components.forEach(c => { app.component(c.name, c); });

app.use(YmapPlugin, settings);
app.use(createPinia());
app.use(router);


app.mount('#app');
