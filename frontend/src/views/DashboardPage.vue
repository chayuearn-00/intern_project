<template>
    <NavBar />
    <div class="container bg-background ">
        <div class="flex flex-col py-9 px-20 h-screen gap-7.5">
            <div class="flex w-full place-content-between h-min">
                <ConclutionCard />
                <ConclutionCard />
                <ConclutionCard />
                <ConclutionCard />
            </div>
            <div class="flex w-full gap-7.5">
                <div class="w-1/2">
                    <Chart />
                </div>
                <div class="flex flex-col w-1/2 gap-7.5">
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
</script>