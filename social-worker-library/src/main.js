import Vue from 'vue'
import axios from './plugins/axios'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import api from '@/api';
const G6 = require('@antv/g6')
Vue.prototype.$G6 = G6
Vue.prototype.$api = api;
import VueAxios from 'vue-axios'
// Vue.use(VueAxios, axios)

Vue.config.productionTip = false

new Vue({
  router,
  vuetify,
  axios,
  VueAxios,
  render: h => h(App)
}).$mount('#app')
