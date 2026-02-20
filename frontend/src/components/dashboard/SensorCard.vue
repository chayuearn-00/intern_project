<template>
    <div class="flex flex-col w-full bg-bg-secondary p-4 rounded-2xl justify-between h-full">
        <div class="flex gap-4 justify-center w-max">
            <img :src="Battery" />
            <p class="text-xl font-semibold">Battery</p>
        </div>
         <div class="w-full bg-white rounded-full h-3">
            <div
                class="bg-primary h-3 rounded-full"
                style="width: 75%;"
            >
            </div>
        </div>
        <p class="text-white text-base font-medium">Threshold: warn ≤ 35% • crit ≤ 20%</p>
    </div>
</template>

<script setup>
import Battery from '../../assets/icons/dashboard/Battery.svg'
import Motor from '../../assets/icons/dashboard/Motor.svg'
import Realtime from '../../assets/icons/dashboard/Realtime.svg'
import Sonar from '../../assets/icons/dashboard/Sonar.svg'
import Signal from '../../assets/icons/dashboard/Signal.svg'
</script>