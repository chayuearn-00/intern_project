<script setup>
import logo_person from '../assets/icons/logo_person.png'
import Download from '../assets/icons/Download.svg'
import ArrowExplore from '../assets/icons/ArrowExplore.png'
import InformationCard from './InformationCard.vue';
import { useRouter } from 'vue-router';

const router = useRouter();

function dashboard() {
    router.push('/Dashboard');
}

</script>

<template>
    <div class="flex flex-col w-[70%] lg:w-auto gap-5 place-self-center lg:gap-11 lg:items-start">
        <div class="flex items-center gap-4.5 lg:mb-11">
            <img :src="logo_person" class="w-10" />
            <p>#001</p>
            <p class="text-primary">USERNAME</p>
        </div>
        <h1 class="hidden lg:block text-7xl font-bold leading-tight text-primary">
            Designed <br />
            <span class="text-gray-500 font-medium">to stay</span> <br />
            <span class="text-primary">essential</span>
        </h1>
        <InformationCard class="lg:hidden max-w-full" />
        <div class="flex-auto self-center">
            <div class="flex gap-6 mt-4 lg:mt-10 place-items-center ">
                <button
                    class="bg-primary hover:bg-blue-700 text-white text-sm lg:text-lg py-3 lg:py-4 px-8.5 rounded-lg flex items-center gap-2 transition"
                    @click="dashboard"
                >
                    Dashboard
                    <span class="transition-transform duration-300 hover:-rotate-45"
                        ><img :src="ArrowExplore" alt="arrow explore"  class="w-5 h-5" />
                    </span>
                </button>

                <button
                    class="border border-gray-300 bg-white px-5 py-3 lg:py-4 rounded-lg hover:bg-gray-100 transition flex items-center gap-2 text-sm lg:text-lg"
                >
                    Download Data
                    <span><img :src="Download" alt="download button" class="w-5 h-5" /></span>
                </button>
            </div>
        </div>
    </div>
</template>