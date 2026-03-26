<template>
    <BaseAlert v-if="Invalide_backend" type="error" title="Invalide" message="Invalid email or password" />
    <div>
      <h2 class="whitespace-nowrap text-2xl font-bold text-black text-left md:text-5xl"
        >Welcome, back!
      </h2>
      <p class="text-xs mt-4 mb-6 text-slate-500">Let’s Get Started with MIIoT</p>
      <form @submit.prevent="submit" class="space-y-5">
        <div class="flex-col my-7">
          <p class="text-sm mb-4">Email*</p>
          <input 
            v-model="form.email" 
            type="email" 
            :class="inputClass"
            @blur.self="check_email"
            /> 
            <p v-if="error.email" class="absolute error-text">Please fill this feild</p>
            <p v-if="errorEmailForm && !error.email" class="absolute error-text">Invalid email format</p>
        </div>
        <PasswordInput v-model="form.password" v-model:error="error.password" />
        <button class="bg-blue-600 text-white rounded-lg px-4 py-4 w-full mt-6 hover:bg-blue-700">Login</button>
        <div class="text-sm my-6 text-left">
          <span>Don't have an account? </span>
          <router-link to="/Register" class="text-black underline">Register</router-link>
        </div>
        <div class="flex items-center w-full my-6 px-6">
          <div class="flex-1 h-px bg-gray-300"></div>
          <span class="px-3 text-gray-400">OR</span>
          <div class="flex-1 h-px bg-gray-300"></div>
        </div>
        <button @click="loginWithGoogle" 
          class="signin-google"
          >
            <img :src="googleImage" alt="Google Icon" class="w-5 h-5 mr-2">
            Login with Google
        </button>
      </form>
    </div>
</template>

<script setup>
import { ref, computed, inject, watch, reactive } from 'vue';
import { useRouter } from 'vue-router';
import PasswordInput from './PasswordInput.vue';
import BaseAlert from './BaseAlert.vue';
import googleImage from '../assets/icons/google-logo.png'
import axios from "axios";

const router = useRouter();
const api = inject('api');
const errorEmailForm =ref(false);
const Invalide_backend = ref(false);

const form = reactive ({
  email: '',
  password: ''
})

const error = reactive({
  email: false,
  password: false,
});

const inputClass = computed(() => [
  'w-full rounded-lg px-4 py-2 pr-10 outline-none',
  error.email || errorEmailForm.value
    ? 'border border-red-500 focus:ring-2 focus:ring-red-500'
    : 'border border-gray-300 focus:ring-2 focus:ring-brand'
]);

const check_email = () => {
  if (!form.email) {
    error.email = true
  }
}

watch(() => form.email, (newEmail) => {
  const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  // if (form.email) {
  //   errorEmailForm.value = !pattern.test(newEmail.trim());
  // }

  (form.email) ? (errorEmailForm.value = !pattern.test(newEmail.trim()) ,error.email = false)
  : 
    (errorEmailForm.value = !pattern.test(newEmail.trim()),
    error.email = true)

  // if (!form.email) {
  //   errorEmailForm.value = !pattern.test(newEmail.trim());
  //   error.email = true;
  // }
});

const loginWithGoogle = () => {
  window.location.href = "http://localhost:8000/auth/google"
};

// const payload = computed(() => ({ email: email.value, password: password.value }));

// const submit = async () => {
//   try {
//     const response = await fetch('http://127.0.0.1:8000/login', {
//       method: 'POST',
//       headers: { 'Content-Type': 'application/json' },
//       body: JSON.stringify(payload.value)
//     });
//     const data = await response.json();
//     if (!response.ok) {
//       error.value = data.detail || 'Invalid email or password';
//     } else {
//       console.log('Login successful', data);
//       // Handle successful login, e.g., store token
//     }
//   } catch (e) {
//     error.value = 'Invalid email or password'
//   }
// }

const submit = async () => {
  Object.keys(error).forEach(key => {
    (form[key].trim()) 
    ? null
    : error[key] = true
  });

  const hasErrors = Object.values(error).some(error => error);
  
  if (!hasErrors) {
    const response = await api.post('/login', {
      email: form.email,
      password: form.password
    }, 
    {
      withCredentials: true
    });

    // console.log("status code", response.data.status_code)
    if (response.data.status_code === 200) {
      Invalide_backend.value = true
      setTimeout(() => {
        Invalide_backend.value = false
      }, 5000);
    } else {
      router.push('/HomePage')
      // localStorage.setItem("access_token", response.data.access_token);
    };
  }
}
</script>