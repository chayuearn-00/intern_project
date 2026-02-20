<template>
    <NavBar class="sticky top-0 z-50" />
    <div class="container bg-background h-screen overflow-y-auto">
        <div class="flex flex-col py-9 px-20 h-full justify-between gap-7.5">
            <div class="flex w-full place-content-between h-min">
                <ConclutionCard />
                <ConclutionCard />
                <ConclutionCard />
                <ConclutionCard />
            </div>
            <div class="grid grid-cols-2 w-full h-full justify-between gap-7.5">
                <div class="h-full">
                    <Chart />
                </div>
                <div class="flex flex-col w-full h-full justify-center gap-7.5">
                    <SystemHealthPanelCard />
                    <RealtimeSensorsCard />
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
import Chart from '../components/dashboard/Chart.vue';
</script>