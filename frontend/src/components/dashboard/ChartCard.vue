<template>
    <div class="dashboard-card justify-between h-full w-full gap-4">
        <div class="flex gap-4 items-center">
            <div class="relative bg-primary w-8.5 h-8.5 rounded-lg">
                <img :src="Chart" class="absolute inset-0 m-auto"/>
            </div>
            <p class="text-black font-bold text-xl">Real-time Charts</p>
        </div>
        <div class="flex flex-col w-full h-full bg-bg-secondary rounded-3xl p-5 justify-between gap-5">
            <div class="flex justify-between items-center ">
                <div class="flex gap-4">
                    <img :src="Battery" />
                    <p class="text-black font-semibold text-xl">Battery Over Time</p>
                </div>
                <Status device="battery" :value="data.battery"/>
            </div>
            <Graph device="battery" :value="data.battery"/>
        </div>
        <div class="flex flex-col w-full h-full bg-bg-secondary rounded-3xl p-5 justify-between gap-5">
            <div class="flex justify-between items-center">
                <div class="flex gap-4">
                    <img :src="Motor" />
                    <p class="text-black font-semibold text-xl">Motor Load Over Time</p>
                </div>
                <Status device="motor" :value="data.motor"/>
            </div>
            <Graph device="motor" :value="data.motor"/>
        </div>
    </div>
</template>

<script setup>
import Chart from '../../assets/icons/dashboard/Chart.svg'
import Battery from '../../assets/icons/dashboard/Battery.svg'
import Motor from  '../../assets/icons/dashboard/Motor.svg'
import Status from './Status.vue';
import Graph from './Graph.vue';

const props = defineProps ({
    data: Object,
});
</script>