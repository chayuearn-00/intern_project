<template>
    <div class="dashboard-card justify-between h-full w-full">
        <div class="flex gap-4 items-center">
            <div class="relative bg-primary w-8.5 h-8.5 rounded-lg">
                <img :src="Chart" class="absolute inset-0 m-auto"/>
            </div>
            <p class="text-black font-bold text-xl">Real-time Charts</p>
        </div>
        <div class="w-full bg-bg-secondary rounded-2xl">
            <div class="flex justify-between items-center p-5">
                <div class="flex gap-4">
                    <img :src="Battery" />
                    <p class="text-black font-semibold text-xl">Battery Over Time</p>
                </div>
                <Status />
            </div>
        </div>
        <div class="w-full bg-bg-secondary rounded-2xl">
            <div class="flex justify-between items-center p-5">
                <div class="flex gap-4">
                    <img :src="Motor" />
                    <p class="text-black font-semibold text-xl">Motor Load Over Time</p>
                </div>
                <Status />
            </div>
        </div>
    </div>
</template>

<script setup>
import Chart from '../../assets/icons/dashboard/Chart.svg'
import Battery from '../../assets/icons/dashboard/Battery.svg'
import Motor from  '../../assets/icons/dashboard/Motor.svg'
import Status from './Status.vue';
</script>