<template>
    <dl class="dashboard-card flex-col w-full divide-y divide-gray-500 ">
        <div class="flex place-content-between w-full items-center py-3">
            <dt class="flex text-xl font-bond items-center gap-4">
                <img :src="images.battery" class="bg-primary p-3 rounded-full w-12" alt="battery">
                Battery
            </dt>
            <Status :value="data.battery" />
        </div>
        <div class="flex place-content-between w-full items-center py-3 bg-background">
            <dt class="flex text-xl font-bond items-center gap-4">
                <img :src="images.motor" class="bg-primary p-3 rounded-full w-12" alt="battery">
                Motor
            </dt>
            <Status :value="data.motor" />
        </div>
        <div class="flex place-content-between w-full items-center py-3">
            <dt class="flex text-xl font-bond items-center gap-4">
                <img :src="images.signal" class="bg-primary p-3 rounded-full w-12" alt="battery">
                Signal
            </dt>
            <Status :value="data.signal" />
        </div>
        <div class="flex place-content-between w-full items-center py-3 bg-background">
            <dt class="flex text-xl font-bond items-center gap-4">
                <img :src="images.sonar" class="bg-primary p-3 rounded-full w-12" alt="battery">
                Sonar
            </dt>
            <Status :value="data.sonar" />
        </div>
    </dl>
</template>

<script setup>
import Battery from '../../assets/icons/dashboard/Battery.svg';
import Motor from '../../assets/icons/dashboard/Motor.svg';
import Signal from '../../assets/icons/dashboard/Signal.svg';
import Sonar from '../../assets/icons/dashboard/Sonar.svg';
import Status from './Status.vue';

const props = defineProps({
    data: Object,
});

const data = {
    battery: props.battery,
    motor: props.motor,
    signal: props.signal,
    sonar: props.sonar
};

const images = {
    battery: Battery,
    motor: Motor,
    signal: Signal,
    sonar: Sonar
};

</script>