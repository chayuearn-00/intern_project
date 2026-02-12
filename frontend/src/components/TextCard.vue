<script setup>
import logo_person from '../assets/icons/logo_person.png'
import Download from '../assets/icons/Download.svg'
import ArrowExplore from '../assets/icons/ArrowExplore.png'


</script>

<template>
    <div class="flex flex-col gap-11 items-start">
        <div class="flex items-center gap-4.5 mb-11">
            <img src="@/assets/icons/logo_person.png" class="w-10" />
            <p>#001</p>
            <p class="text-primary">USERNAME</p>
        </div>
        <h1 class="text-7xl font-bold leading-tight text-primary">
            Designed <br />
            <span class="text-gray-500 font-medium">to stay</span> <br />
            <span class="text-primary">essential</span>
        </h1>
        <div class="flex-auto">
            <div class="flex gap-6 mt-10">
                <button
                    class="bg-primary hover:bg-blue-700 text-white text-lg py-4 px-8.5 rounded-lg flex items-center gap-2 transition"
                >
                    Explore
                    <span class="transition-transform duration-300 hover:-rotate-45"
                        ><img :src="ArrowExplore" alt="arrow explore" />
                    </span>
                </button>

                <button
                    class="border border-gray-300 bg-white px-5 py-4 rounded-lg hover:bg-gray-100 transition flex items-center gap-2"
                >
                    Download Data
                    <span><img :src="Download" alt="download button" /></span>
                </button>
            </div>
        </div>
    </div>
</template>