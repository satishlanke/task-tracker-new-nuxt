import { createApp } from 'vue'
import App from './App.vue'

import router from './router/index'
import VueSweetalert2 from 'vue-sweetalert2';
import axios from 'axios'
import VueAxios from 'vue-axios'


const app =createApp(App)
app.use(router)
app.use(VueAxios, axios)
app.use(VueSweetalert2)
app.mount('#app')
