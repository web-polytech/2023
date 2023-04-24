import { createApp } from 'vue';
import { createPinia } from 'pinia';

import App from './App.vue';
import router from './router';
import components from '@/components/UI';

const app = createApp(App);


app.use(createPinia());
app.use(router);

components.forEach(c => { app.component(c.name, c); });

app.mount('#app');
