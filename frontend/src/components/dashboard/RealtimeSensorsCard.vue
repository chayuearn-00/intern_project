<template>
    <div class="dashboard-card gap-7.5 h-full max-h-100 ">
        <div class="flex place-content-between items-center">
            <div class="flex gap-4 justify-center">
                <div class="relative bg-primary w-8.5 h-8.5 rounded-lg">
                    <img :src="Realtime" class="absolute inset-0 m-auto"/>
                </div>
                <p class="text-black font-bold text-xl">Real-time Sensors</p>
            </div>
            <div class="bg-primary rounded-xl">
                <p class="text-white text-xs font-semibold px-2.5 py-1">4 modules</p>
            </div>
        </div>
        <div className="grid grid-cols-2 grid-rows-2 h-full w-full gap-7.5">
            <SensorCard device="battery" :value="data.battery"/>
            <SensorCard device="motor" :value="data.motor"/>
            <SensorCard device="signal" :value="data.signal"/>
            <SensorCard device="sonar" :value="data.sonar"/>
        </div>
    </div>
</template>

<script setup>
import Realtime from '../../assets/icons/dashboard/Realtime.svg'
import SensorCard from '../dashboard/SensorCard.vue'

const props = defineProps ({
    data: Object,
});
</script>
