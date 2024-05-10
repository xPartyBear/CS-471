//import './assets/main.css'

import { createApp } from 'vue'
import { globalCookiesConfig } from 'vue3-cookies'
import VueCookies from 'vue3-cookies'
import App from './App.vue'
import router from './router'

const app = createApp(App);

app.use(router);

globalCookiesConfig({
    expireTimes: "30d",
    path: "/",
    domain: "",
    secure: true,
    sameSite: "None",
});
app.use(VueCookies);



app.mount('#app');
