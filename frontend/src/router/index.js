import { createRouter, createWebHistory } from "vue-router"

const routes = [
  {
    path: "/Login",
    name: "login",
    component: () => import("../views/LoginPage.vue"),
    meta: { title: "Login" },
  },
  {
    path: "/",
    redirect: "/Login",
  },
  {
    path: "/Register",
    name: "register",
    component: () => import("../views/RegisterPage.vue"),
    meta: { title: "Register" },
  },
  {
    path: "/Homepage",
    name: "HomePage",
    component: () => import("../views/HomePage.vue"),
    meta: { title: "HomePage" },
  },
]

const router = createRouter({
  history: createWebHistory('/'),
  routes,
})

// setting Title Page
const DEFAULT_TITLE = import.meta.env.VITE_APP_DEFAULT_TITLE || "ARC CU"
router.afterEach((to) => {
  document.title = to.meta.title || DEFAULT_TITLE
})

export default router