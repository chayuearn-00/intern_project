<template>
    <div class="flex flex-col gap-2.5 w-105 p-8 bg-white rounded-3xl">
        <div class="flex w-full items-center justify-between">
            <div class="flex gap-5 items-center">
                <div class="relative w-12.5 h-12.5 bg-status-low rounded-full">
                    <img :src="Battery" class="absolute inset-0 m-auto" />
                </div>
                <p class="text-xl font-bold ">{{texts.battery}}</p>
            </div>
            <div class="px-2.5 py-1 border border-status-bsafe bg-secondary rounded-3xl right-0 text-white">
                <p>SAVE</p>
            </div>
        </div>
        <p class="text-black text-2xl font-bold">6%</p>
    </div>
</template>

<script setup>
import Battery from '../../assets/icons/dashboard/Battery.svg';
import Motor from '../../assets/icons/dashboard/Motor.svg';
import Signal from '../../assets/icons/dashboard/Signal.svg';
import Sonar from '../../assets/icons/dashboard/Sonar.svg';

// const icon = devices.device;
// const text = texts.device;

// const props = defineProps ({
//     device: String,
//     status: String,
// })

const devices = {
    battery: Battery,
    moter: Motor,
    signal: Signal,
    sonar: Sonar
};

const texts = {
    battery: "Battery Level",
    moter: "Moter Load",
    signal: "Signal Strength",
    sonar: "Sonar Distance"
};

const color = {
    'red': {}
};
</script>