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
            <div class="flex max-w-full">
                <Chart />
                <div class="flex flex-col">
                    <DataTable />
                    <DataLine />
                </div>
            </div>
        </div>
    </div>

</template>

<script setup>
import NavBar from '../components/NavBar.vue';
import ConclutionCard from '../components/dashboard/ConclutionCard.vue';

</script>