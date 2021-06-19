import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VCharts from 'v-charts'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(VCharts)

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
