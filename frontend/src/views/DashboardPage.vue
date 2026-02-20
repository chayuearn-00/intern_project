<template>
    <div class="dashboard-card gap-7.5">
        <div class="flex place-content-between">
            <div class="flex gap-4 justify-center">
                <div class="relative bg-primary w-8.5 h-8.5 rounded-lg">
                    <img :src="Realtime" class="absolute inset-0 m-auto"/>
                </div>
                <p class="text-black font-bold text-xl">Real-time Sensors</p>
            </div>
            <div class="bg-primary h-5 rounded-lg">
                <p class="text-white text-xs font-semibold px-2.5 py-1">4 modules</p>
            </div>
        </div>
        <div className="grid grid-cols-2 grid-rows-2 gap-7.5">
            <SensorCard />
            <SensorCard />
            <SensorCard />
            <SensorCard />
        </div>
    </div>
</template>

<script setup>
import Realtime from '../../assets/icons/dashboard/Realtime.svg';
import SensorCard from './SensorCard.vue';
</script>