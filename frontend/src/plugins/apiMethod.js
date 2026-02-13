import axios from "axios"

export const createApi = (options = {}) => {
  // API headers
  const baseURL = options.baseURL || import.meta.env.VITE_BASE_URL
  const router = options.router
  const loginPath = options.loginPath || "/Login"
 
  const apiClient = axios.create({
    baseURL,
    headers: {
      "Content-Type": "application/json",
    }, withCredentials: true,
  })
 
  apiClient.interceptors.request.use(
    (config) => {
      if (config.url.includes("Login")) {
        return config
      }
 
      const token = localStorage.getItem("accessToken")
      if (token) {
        config.headers.Authorization = `Bearer ${token}`
      }
      //   else if (router) {
      //   router.push(loginPath)
      // }
      return config
    },
    (error) => Promise.reject(error),
  )
 
  apiClient.interceptors.response.use(
    (response) => response,
    (error) => {
      if (error.config.url.includes("Login")) {
        return Promise.reject(error)
      }
 
      if (error.response?.status === 401) {
        console.log("Invalid action, redirecting to login")
        localStorage.removeItem("accessToken")
        localStorage.removeItem("member")
        localStorage.removeItem("menuPermission")
        if (router) {
          router.push(loginPath)
        }
      }
 
      return Promise.reject(error)
    },
  )
 
  return apiClient
}
 