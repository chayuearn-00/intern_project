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
    component: () => import("../views/RegisterForm.vue"),
    meta: { title: "Register" },
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