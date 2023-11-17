import Vue from 'vue'
import UserDetails from '@/components/UserDetails.vue';
import AccountCreation from '@/components/AccountCreation.vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/user-details',
    name: 'UserDetails',
    component: UserDetails,
  },
  {
    path: '/account-creation',
    name: 'AccountCreation',
    component: AccountCreation,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
