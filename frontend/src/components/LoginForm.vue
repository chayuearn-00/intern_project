<template>
    <div>
      <h2 class="whitespace-nowrap text-2xl font-bold text-black text-left md:text-5xl"
        >Welcome, back!
      </h2>
      <p class="text-xs mt-4 mb-6 text-slate-500">Let’s Get Started with MIIoT</p>
      <form @submit.prevent="submit" class="space-y-5">
          <p class="text-sm mb-4">Email*</p>
          <input 
            v-model="email" 
            type="email" 
            :class="inputClass"
          /> 
          <PasswordInput v-model="password" :error="!!error" />
          <p v-if="error" class="text-sm text-red-500">{{ error }}</p>
          <button class="bg-blue-600 text-white rounded-lg px-4 py-4 w-full mt-6 hover:bg-blue-700">Login</button>
          <div class="text-sm my-6 text-left">
            <span>Forgot your password? </span>
            <a href="../views/ResetPassword.vue" class="text-black underline">Reset</a>
          </div>
          <div class="flex items-center w-full my-6 px-6">
            <div class="flex-1 h-px bg-gray-300"></div>
            <span class="px-3 text-gray-400">OR</span>
            <div class="flex-1 h-px bg-gray-300"></div>
          </div>
          <button @click="$router.push('/Register')" 
            class="bg-white text-black border border-gray-300 rounded-lg shadow-md py-4 px-4 w-full mt-6 hover:bg-gray-100"
            >Sign up
          </button>
      </form>
    </div>
</template>

<script setup>
import { ref, computed, inject, onMounted } from 'vue';
import PasswordInput from './PasswordInput.vue';

const email = ref('');
const password = ref('');
const error = ref(null);
const api = inject('api');

const inputClass = computed(() => [
    'w-full rounded-lg px-4 py-2 mb-4 pr-10 outline-none',
    error.value
        ? 'border border-red-500 focus:ring-2 focus:ring-red-500'
        : 'border border-gray-300 focus:ring-2 focus:ring-brand'
]);

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
  try {
    const response = await api.post('/login', {
      email: email.value,
      password: password.value
    });

    const data = response.data;
    console.log('Login successful', data);

  } catch (e) {
    error.value = 'Invalid email or password'
  }
}


</script>

<style>

</style>