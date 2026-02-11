<script setup>
import { ref } from 'vue';
import Dropdown from './Dropdown.vue';
import Arrow from '../assets/icons/Arrow.svg';

const open = ref(false);
</script>

<template>
    <div class="relative flex flex-col gap-6 px-6 py-8 text-lg">
        <a href="#">Home</a>
        <div>
            <button
                @click="open = !open" 
                class="flex items-center gap-1 text-xl text-foreground"
            >
                <div class="overflow-hidden h-7 group cursor-pointer">
                    <span 
                        class="block transition-transform duration-300"
                        :class="{ '-translate-y-full': open }"
                    >
                        Pages
                    </span>
                    <span 
                        class="block top-full left-0 transition-transform duration-300"
                        :class="{'-translate-y-full': open }"
                    >
                        Pages
                    </span>
                </div>
                <div class="">
                    <img src="" alt="">
                </div>
                <div 
                    class="w-4 h-4 transition-transform"
                    :class="{ 'rotate-180': open }"
                >
                    <img :src="Arrow" alt="arrow" />
                </div>
            </button>
        </div>
        <transition
            enter-active-class="animate-dropbox-open"
            leave-active-class="animate-dropbox-close"
        >   
            <div v-if="open" class="max-w-[90%] w-full mx-auto place-self-center ">
                <Dropdown />
            </div>
        </transition>
        <a href="#">Pricing</a>
        <a href="#">Blog</a>
    </div>
</template>
