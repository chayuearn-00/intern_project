<template>
    <NavBar />
    <div class="container bg-background">
        <div class="flex felx-col gap-9 py-9 px-20">
            <div class="flex max-w-full">
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

</script>