<template>
    <!-- <div class="container bg-background h-screen overflow-y-auto"> -->
    <div class="container bg-background h-full overflow-y-auto">
        <NavBar class="sticky top-0 z-50" />
        <div class="flex flex-col py-9 px-20 h-full justify-between gap-7.5">
            <div class="flex w-full place-content-between h-min">
                <ConclutionCard device="battery" :value="data.battery"/>
                <ConclutionCard device="motor" :value="data.motor"/>
                <ConclutionCard device="signal" :value="data.signal"/>
                <ConclutionCard device="sonar" :value="data.sonar"/>
            </div>
            <div class="flex flex-col lg:grid lg:grid-cols-2 w-full h-full justify-between gap-4 lg:gap-7.5">
                <div class="w-full h-full">
                    <Chart :data="data"/>
                </div>
                <div class="flex flex-col w-full h-full justify-center gap-7.5">
                    <SystemHealthPanelCard :data="data"/>
                    <RealtimeSensorsCard :data="data"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import NavBar from '../components/NavBar.vue';
import ConclutionCard from '../components/dashboard/ConclutionCard.vue';
import RealtimeSensorsCard from '../components/dashboard/RealtimeSensorsCard.vue';
import SystemHealthPanelCard from '../components/dashboard/SystemHealthPanelCard.vue';
import Chart from '../components/dashboard/ChartCard.vue';
import { ref } from "vue"
import { useRouter } from 'vue-router';

const router = useRouter();

const data = ref({
  battery: 0,
  motor: 0,
  sonar: 0,
  signal: 0
})

const ws = new WebSocket(`${import.meta.env.VITE_WS_URL}/ws/dashboard`)

ws.onmessage = (event) => {
  data.value = JSON.parse(event.data)
}

ws.onclose = (event) => {
  // 1008 = policy violation (auth fail)
  if (event.code === 1008) {
    router.push("/login")
  }
}

ws.onerror = () => {
  router.push("/login")
}
</script>