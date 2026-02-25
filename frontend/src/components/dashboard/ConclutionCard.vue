<template>
    <div class="dashboard-card  gap-2.5 w-105">
        <div class="flex w-full items-center justify-between">
            <div class="flex gap-5 items-center">
                <div class="relative w-12.5 h-12.5 bg-primary rounded-full">
                    <img :src="images[device]" class="absolute inset-0 m-auto" />
                </div>
                <p class="text-xl font-bold ">{{texts[device]}}</p>
            </div>
            <Status :device="device" :value="value"/>
        </div>
        <div class="flex gap-2 mx-2">
            <p class="text-black text-2xl font-bold">{{ value }}</p>
            <p v-if="!['sonar'].includes(device)" class="text-black text-2xl font-bold">%</p>
            <p v-if="['sonar'].includes(device)" class="text-black text-2xl font-bold">m</p>
        </div>
    </div>
</template>

<script setup>
import Battery from '../../assets/icons/dashboard/Battery.svg';
import Motor from '../../assets/icons/dashboard/Motor.svg';
import Signal from '../../assets/icons/dashboard/Signal.svg';
import Sonar from '../../assets/icons/dashboard/Sonar.svg';
import Status from './Status.vue';

const props = defineProps ({
    device: {
        type: String,
        defailt: 'battery'
    },
    value: {
        type: Number,
        default: '0'
    },
})

const texts = {
    battery: "Battery Level",
    motor: "Motor Load",
    signal: "Signal Strength",
    sonar: "Sonar Distance"
};

const images = {
    battery: Battery,
    motor: Motor,
    signal: Signal,
    sonar: Sonar
}
</script>