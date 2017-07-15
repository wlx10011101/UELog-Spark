import Vue from 'vue'
import Router from 'vue-router'
import Sidebar from '@/components/Sidebar'
import Chart from '@/components/Chart'
import VueResource from 'vue-resource'

Vue.use(Router);
Vue.use(VueResource);
// Vue.http.options.emulateHTTP = true;
// Vue.http.options.emulateJSON = true;

export default new Router({
  routes: [
    {
      path: '/chart',
      name: 'chart',
      component: Chart
    }
  ]
})
