<template>
    <div class="dashboard-card justify-between  w-full gap-4">
        <div class="flex gap-4 items-center">
            <div class="relative bg-primary w-8.5 h-8.5 rounded-lg">
                <img :src="Chart" class="absolute inset-0 m-auto"/>
            </div>
            <p class="text-black font-bold text-xl">Real-time Charts</p>
        </div>
        <!-- <div class="flex flex-col w-full h-full bg-bg-secondary rounded-3xl p-5 justify-between gap-5"> -->
        <div class="flex flex-col w-full h-full bg-bg-secondary rounded-3xl p-5 gap-5">
            <div class="flex justify-between items-center">
                <div class="flex gap-4">
                    <img :src="Battery" />
                    <p class="text-black font-semibold text-xl">Battery Over Time</p>
                </div>
                <Status device="battery" :value="data.battery"/>
            </div>
            <div class="">
                <Graph 
                    :devices="allDevices"
                    :initialRecords="initialRecords"
                    :latestData="latestData"
                    :visibleDevices="visibleDevices"
                />
            </div>
            <!-- <div class="flex justify-between p-4">
                <button 
                    :class="(show_graph.battery.value) ? 'show-graph' : 'hide-graph'" 
                    @click="show_graph.battery.value = !show_graph.battery.value"
                    >Battery
                </button>
                <button 
                    :class="(show_graph.motor.value) ? 'show-graph' : 'hide-graph'" 
                    @click="show_graph.motor.value = !show_graph.motor.value"
                    >Motor
                </button>
                <button 
                    :class="(show_graph.signal.value) ? 'show-graph' : 'hide-graph'" 
                    @click="show_graph.signal.value = !show_graph.signal.value"
                    >Signal
                </button>
                <button 
                    :class="(show_graph.sonar.value) ? 'show-graph' : 'hide-graph'" 
                    @click="show_graph.sonar.value = !show_graph.sonar.value"
                    >Sonar
                </button>
            </div> -->
        </div>
        <!-- <div class="flex flex-col w-full h-full bg-bg-secondary rounded-3xl p-5 justify-between gap-5">
            <div class="flex justify-between items-center">
                <div class="flex gap-4">
                    <img :src="Motor" />
                    <p class="text-black font-semibold text-xl">Motor Load Over Time</p>
                </div>
                <Status device="motor" :value="data.motor"/>
            </div>
            <Graph device1="motor" :value1="data.motor"/>
        </div> -->
    </div>
</template>

<script setup>
import Chart from '../../assets/icons/dashboard/Chart.svg'
import Battery from '../../assets/icons/dashboard/Battery.svg'
import Motor from  '../../assets/icons/dashboard/Motor.svg'
import Status from './Status.vue';
import Graph from './Graph.vue';
import { computed, ref, onMounted } from 'vue';

const props = defineProps ({
    data: Object,
});

const show_graph = {
    battery: ref(true),
    motor: ref(true),
    signal: ref(true),
    sonar: ref(false),
};

// All possible devices
const allDevices = [
    { id: "battery", name: "Battery" },
    { id: "motor", name: "Motor" },
    { id: "signal", name: "Signal" },
    { id: "sonar", name: "Sonar" },
];

// Devices to show (by id)
const visibleDevices = computed(() => {
    return allDevices
        .filter(dev => show_graph[dev.id]?.value)
        .map(dev => dev.id);
});

// Initial records for each device (fetch from backend)
const initialRecords = ref({
    battery: [],
    motor: [],
    signal: [],
    sonar: [],
});

onMounted(async () => {
    try {
        const res = await fetch('http://localhost:8000/api/dashboard/latest?limit=20');
        const data = await res.json();
        initialRecords.value = {
            battery: data.map(d => ({ time: d.time, value: d.battery })),
            motor: data.map(d => ({ time: d.time, value: d.motor })),
            signal: data.map(d => ({ time: d.time, value: d.signal })),
            sonar: data.map(d => ({ time: d.time, value: d.sonar })),
        };
    } catch (err) {
        console.error('Failed to fetch sensor data:', err);
    }
});

// Latest data for each device (should be provided by parent or fetched)
const latestData = computed(() => {
    // Example: { battery: { time, value }, ... }
    // Replace with actual latest data logic
    return {
        battery: { time: '', value: props.data.battery },
        motor: { time: '', value: props.data.motor },
        signal: { time: '', value: props.data.signal },
        sonar: { time: '', value: props.data.sonar },
    };
});
</script>