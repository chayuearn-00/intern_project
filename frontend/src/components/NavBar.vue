<template>
    <nav class="navbar">
        <div class="navbar-card">
            <a href="/homepage"><img src="../assets/icons/Logo.svg"  alt="Logo" /></a>
            <ul class="hiden-item gap-24 text-sm font-medium">
                <li>
                    <a href="/homepage" class="navbar-item">
                        Home
                    </a>
                </li>  
                <li
                    class="relative"
                    @click="open = !open"
                    >
                    <button
                        class="flex items-center gap-1 text-xl text-foreground hover:text-black"
                    >
                        Pages
                        <svg class="w-4 h-4 transition-transform"
                            :class="{ 'rotate-180': open }"
                            fill="none" stroke="currentColor"
                            viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                stroke-width="2"
                                d="M19 9l-7 7-7-7" />
                        </svg>
                    </button>

                    <!-- Dropdown Box -->
                    <div
                        v-show="open"
                        class="absolute left-0 mt-3 w-48 rounded-xl bg-white shadow-lg border p-2"
                    >
                        <a
                            v-for="item in pages"
                            :key="item.name"
                            :href="item.link"
                            class="block px-4 py-2 rounded-lg text-gray-600 hover:bg-gray-100 hover:text-black"
                        >
                            {{ item.name }}
                        </a>
                    </div>
                </li> 
                    <a href="/" class="navbar-item">Pricing</a>
                    <a href="/" class="navbar-item">Blog</a>
            </ul>
            <div class="hiden-item gap-6">
                <img src= "../assets/icons/HomePage-Vector.svg" alt="multi menu" />
                <button class="button-login bg-secondary px-8" @click="$router.push('/login')">Logout</button>
            </div>
        </div>

        <!-- Mobile Menu Icon --> 
         <div class="mobile-menu-icon">
            <a href="/homepage">
                <img src="../assets/icons/Logo.svg" class="shrink-0" alt="Logo">
            </a>
            <div class="relative">
                <button @click="burger = !burger">
                    <img :src="MenuButton" alt="menu button" class="h-9" />
                </button>

                <!-- burger dropbox -->
                <div
                    v-show="burger"
                    class="absolute right-0 mt-1 w-48 rounded-xl bg-white shadow-lg border p-2"
                >
                    <a
                        v-for="item in main_pages"
                        :key="item.name"
                        :href="item.link"
                        class="drop-box"
                    >
                        {{ item.name }}
                    </a>
                    <a 
                        @click="$router.push('/login')"
                        class="drop-box"
                    >
                        Logout
                    </a>
            </div>
            </div>
         </div>
    </nav>
            
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import MenuButton from '../assets/icons/MenuButton.svg';

const open = ref(false);
const burger = ref(false);

const pages = [
  { name: 'About Us', link: '/about' },
  { name: 'Contact', link: '/contact' },
  { name: 'Dashboard', link: '/dashboard' },
]

const main_pages = [
  { name: 'Home', link: '/homepage' },
  { name: 'Pricing', link: '/' },
  { name: 'Blog', link: '/' },
]

</script>

<style>
.custom_gap {
    gap: 96px;
}

</style>