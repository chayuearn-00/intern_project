<template>
    <NavBar />
    <div class="container bg-background ">
        <div class="flex felx-col py-9 px-20 h-screen">
            <div class="flex w-full place-content-between h-min">
                <ConclutionCard />
                <ConclutionCard />
                <ConclutionCard />
                <ConclutionCard />
            </div>
            <div class="flex w-max gap-7.5">
                <Chart />
                <div class="flex flex-col w-1/2">
                    <DataTable />
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

</script>