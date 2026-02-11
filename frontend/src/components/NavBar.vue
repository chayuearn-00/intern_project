<template>
    <nav class="navbar">
        <div class="navbar-card">
            <a href="/homepage"><img src="../assets/icons/Logo.svg"  alt="Logo" /></a>
            <ul class="hiden-item gap-24 text-sm font-medium">
                <li>
                    <a href="#" class="navbar-item">
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
                        <div class="relative overflow-hidden h-7 cursor-pointer">
                            <span 
                                class="block transition-transform duration-300"
                                :class="{ '-translate-y-full': open }"
                            >
                                Pages
                            </span>
                            <span 
                                class="block absolute top-full left-0 transition-transform duration-300"
                                :class="{ '-translate-y-full': open }"
                            >
                                Pages
                            </span>
                        </div>
                        <svg class="w-4 h-4 transition-transform"
                            :class="{ 'rotate-180': open }"
                            fill="none" stroke="currentColor"
                            viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                stroke-width="2"
                                d="M19 9l-7 7-7-7" />
                        </svg>
                    </button>
                    <Transition
                        enter-active-class="animate-dropbox-open"
                        leave-active-class="animate-dropbox-close"
                    > 
                        <div class="absolute w-max">
                            <Dropdown v-if="open" class="mt-5 -translate-x-1/2" />
                        </div>
                    </Transition>
                </li> 
                    <a href="/" class="navbar-item">Pricing</a>
                    <a href="/" class="navbar-item">Blog</a>
            </ul>
            <div class="hiden-item gap-6">
                <img :src="HomePageVector" alt="multi menu" />
                <button class="button-login bg-secondary px-8" @click="logOut">
                    <div class="flex gap-2">
                        Logout  
                        <img :src="Logout" alt="logout logo"/>
                    </div>
                </button>
            </div>
        </div>
        
        <!-- Mobile Menu Icon --> 
        <div class="mobile-menu-icon">
            <a href="/homepage">
                <img src="../assets/icons/Logo.svg" class="shrink-0" alt="Logo">
            </a>
            <div>
                <button @click="burger = !burger" class="cursor-pointer">
                    <img :src="MenuButton" alt="menu button" class="h-9" />
                </button>
            </div>
        </div>
        <div
            class="absolute top-full left-0 w-full bg-white shadow-xl origin-top transform transition-transform duration-300 ease-in-out overflow-hidden"
            :class="burger ? 'scale-y-100' : 'scale-y-0'"
        >
            <BurgerNavbar />
        </div>
    </nav>
</template>

<script setup>
import { ref } from 'vue';
import MenuButton from '../assets/icons/MenuButton.svg';
import Logout from '../assets/icons/Logout.svg';
import HomePageVector from '../assets/icons/HomePage-Vector.svg';
import Dropdown from './Dropdown.vue';
import BurgerNavbar from './BurgerNavbar.vue';
import { useRouter } from 'vue-router';

const open = ref(false);
const router = useRouter();
const burger = ref(false);

const pages = [
  { name: 'About Us', link: '/about' },
  { name: 'Contact', link: '/contact' },
  { name: 'Dashboard', link: '/dashboard' },
]

const logOut = () => {
    return router.push('/login')
}

</script>

<style>
.custom_gap {
    gap: 96px;
}

</style>