<template>
    <div class="flex flex-col w-full bg-bg-secondary p-4 rounded-2xl justify-between h-full">
        <div class="flex gap-4 justify-center w-max">
            <img :src="images[device]" />
            <p class="text-xl font-semibold">{{text[device]}}</p>
        </div>
         <div class="w-full bg-white rounded-full h-3">
            <div
                v-if="device !== 'sonar'"
                class="bg-primary h-3 rounded-full"
                :style="{ width: props.value + '%' }"
            >
            </div>
            <div
                v-if="device == 'sonar'"
                class="bg-primary h-3 rounded-full"
                :style="{ width: sonar_percent.value + '%' }"
            >
            </div>
        </div>
        <p class="text-white text-base font-medium">Threshold: {{threshold[device]}}</p>
    </div>
</template>

<script setup>
import Battery from '../../assets/icons/dashboard/Battery.svg'
import Motor from '../../assets/icons/dashboard/Motor.svg'
import Realtime from '../../assets/icons/dashboard/Realtime.svg'
import Sonar from '../../assets/icons/dashboard/Sonar.svg'
import Signal from '../../assets/icons/dashboard/Signal.svg'
import { computed } from 'vue'

const props = defineProps ({
    device: String,
    value: Number,
});

const images = {
    battery: Battery,
    motor: Motor,
    signal: Signal,
    sonar: Sonar
}

const sonar_percent = computed(() => {
    if (props.value < 200) return 50;
    return 100
})

const text = {
    battery: "Battery",
    motor: "Motor",
    signal: "Signal",
    sonar: "Sonar"
}

const threshold = {
    battery: "warn ≤ 35% • crit ≤ 20%",
    motor: "warn ≤ 35% • crit ≤ 20%",
    signal: "warn ≤ 35% • crit ≤ 20%",
    sonar: "warn ≤ 200 m"
}
</script>