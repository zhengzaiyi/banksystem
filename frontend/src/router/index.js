import Vue from 'vue'
import VueRouter from 'vue-router'
import home from '@/components/Home'
import list from "@/components/List";
import account from "@/components/Account";
import branch from "@/components/Branch";
import dept from "@/components/Dept";
import loan from "@/components/Loan";
import staff from "@/components/Staff";
import customer from "@/components/Customer";
import NotFound from "@/components/NotFound";

Vue.use(VueRouter)

export default new VueRouter({
    routes: [
        {
            path: '/',
            name: 'Home',
            component: home
        },
        {
            path: '/account',
            name: 'account',
            component: account
        },
        {
            path: '/list',
            name: 'list',
            component: list
        },
        {
            path: '/branch',
            name: 'branch',
            component: branch
        },
        {
            path: '/dept',
            name: 'dept',
            component: dept
        },
        {
            path: '/loan',
            name: 'loan',
            component: loan
        },
        {
            path: '/staff',
            name: 'staff',
            component: staff
        },
        {
            path: '/customer',
            name: 'customer',
            component: customer
        },
        {
            path: '/404',
            name: 'NotFound',
            component: NotFound
        },
        {
            path: '*',
            redirect: '/404'
        }
    ],
    mode: "history"
})