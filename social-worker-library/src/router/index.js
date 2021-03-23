import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About'
import Antv from '../views/antv'
import Test from '../views/test'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    component: About
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },{
    path: '/antv/',
    name: 'Antv',
    component: Antv
  },{
    path: '/test/',
    name: 'Test',
    component: Test
  }
]

const router = new VueRouter({
  routes
})

export default router
