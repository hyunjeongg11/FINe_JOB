import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
// import { useKakao } from 'vue3-kakao-maps/@utils';

const app = createApp(App)

// useKakao('92cf99384726016668fd96cff97383b1');
app.use(createPinia())
app.use(router)

app.mount('#app')
