<template>
    <!-- <div class="container bg-background h-screen overflow-y-auto"> -->
    <div class="container bg-background">
        <NavBar />
        <div class="flex flex-col py-6 px-10 sm:px-20 justify-between gap-6">
            <div class="hidden lg:flex">
              <div class="flex w-full place-content-between h-min">
                  <ConclutionCard device="battery" :value="data.battery"/>
                  <ConclutionCard device="motor" :value="data.motor"/>
                  <ConclutionCard device="signal" :value="data.signal"/>
                  <ConclutionCard device="sonar" :value="data.sonar"/>
              </div>
            </div>
            <div class="flex lg:hidden max-w-full">
              <SMConclutionCard :data="data" />
            </div>
            <div class="flex flex-col lg:grid lg:grid-cols-2 w-full h-full justify-between gap-6 lg:gap-7.5">
                <div class="w-full h-full">
                    <Chart :data="data"/>
                </div>
                <div class="flex flex-col w-full h-full gap-6">
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
import SMConclutionCard from '../components/dashboard/SMConclutionCard.vue';

const router = useRouter();

const data = ref({
  battery: 0,
  motor: 0,
  sonar: 0,
  signal: 0
})

//เชื่อม web socket จาก path
const ws = new WebSocket(`${import.meta.env.VITE_WS_URL}/ws/dashboard`)

//ดักฟังอัตโนมัติเมื่อมีค่าส่งมา (event.data คือข้อมูลที่มันส่งมา เก็บไว้ในตัวแปร data) + แปลงข้อมูลเป็น JSON
ws.onmessage = (event) => {
  data.value = JSON.parse(event.data)
}


//เมื่อการเชื่อมต่อหยุดลง หรือเกิดการผิดพลาด จะเกิด event
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