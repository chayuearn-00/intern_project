import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router/index.js'
import { createApi } from './plugins/apiMethod'

const $api = createApi({
  baseURL: import.meta.env.VITE_APP_BASE_URL,
  router,
})

createApp(App)
    .use(router)
    .provide("api", $api)
    .mount('#app')

