<template>
    <div class="dashboard-card justify-between h-full w-full gap-4">
        <div class="flex gap-4 items-center">
            <div class="relative bg-primary w-8.5 h-8.5 rounded-lg">
                <img :src="Chart" class="absolute inset-0 m-auto"/>
            </div>
            <p class="text-black font-bold text-xl">Real-time Charts</p>
        </div>
        <!-- <div class="flex flex-col w-full h-full bg-bg-secondary rounded-3xl p-5 justify-between gap-5"> -->
        <div class="flex flex-col w-full h-full bg-bg-secondary rounded-3xl p-5 gap-5">
            <div class="flex justify-between items-center ">
                <div class="flex gap-4">
                    <img :src="Battery" />
                    <p class="text-black font-semibold text-xl">Battery Over Time</p>
                </div>
                <Status device="battery" :value="data.battery"/>
            </div>
            <Graph 
                device1="battery" :value1="data.battery" 
                device2="motor" :value2="data.motor"/>
            <!-- <Graph :devices="devices" :initialRecords="records" /> -->
            <!-- <Graph :devices="devices" /> -->
            <div class="flex justify-between p-4">
                <button 
                    class="show-graph" 
                    @click="show_graph.battery.value = !show_graph.battery.value"
                    >Battery
                </button>
                <button 
                    class="show-graph"
                    @click="show_graph.motor.value = !show_graph.motor.value"
                    >Motor
                </button>
                <button 
                    class="show-graph"
                    @click="show_graph.signal.value = !show_graph.signal.value"
                    >Signal
                </button>
                <button 
                    class="show-graph"
                    @click="show_graph.sonar.value = !show_graph.sonar.value"
                    >Sonar
                </button>
            </div>
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
import { computed, ref } from 'vue';

const props = defineProps ({
    data: Object,
});

const show_graph = {
    battery: ref(true),
    motor: ref(true),
    signal: ref(true),
    sonar: ref(true),
};

// make devices a computed property so updates propagate
const devices = computed(() => {
  const list = [];

  if (show_graph.battery.value) {
    list.push({ name: "battery", value: props.data.battery });
  }
  if (show_graph.motor.value) {
    list.push({ name: "motor", value: props.data.motor });
  }
  if (show_graph.signal.value) {
    list.push({ name: "signal", value: props.data.signal });
  }

  return list;
});
</script>