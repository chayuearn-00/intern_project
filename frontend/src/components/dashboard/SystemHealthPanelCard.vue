<template>
    <div class="dashboard-card justify-between gap-7.5 w-full">
        <div class="flex place-content-between items-center">
            <div class="flex gap-4 items-center">
                <div class="relative bg-primary w-8.5 h-8.5 rounded-lg">
                    <img :src="Shield" class="absolute inset-0 m-auto"/>
                </div>
                <p class="text-black font-bold text-xl">System Health Panel</p>
            </div>
            <div class="bg-primary rounded-xl">
                <p class="text-white text-xs font-semibold px-2.5 py-1">4 modules</p>
            </div>
        </div>
        <div class="overflow-x-auto rounded-2xl">
            <table class="min-w-full border w-max border-bg-secondary">
                <thead class="bg-bg-secondary">
                    <tr>
                        <th class="table-topic">Module</th>
                        <th class="table-topic">Status</th>
                        <th class="table-topic">Detail</th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="hover:bg-gray-50 border border-bg-secondary">
                        <td class="px-4 text-base font-medium">Battery</td>
                        <td class="px-4">
                            <span class="inline-flex">
                                <Status />
                            </span>
                        </td>
                        <td class="px-4 py-2">6%</td>
                    </tr>
                    <tr class="hover:bg-gray-50 border border-bg-secondary">
                        <td class=" px-4 py-2 text-base font-medium">Motor</td>
                        <td class="px-4 py-2">
                            <span class="inline-flex">
                                <Status />
                            </span>
                        </td>
                        <td class="px-4 py-2">6%</td>
                    </tr>
                    <tr class="hover:bg-gray-50 border border-bg-secondary">
                        <td class=" px-4 py-2 text-base font-medium">Signal</td>
                        <td class="px-4 py-2">
                            <span class="inline-flex">
                                <Status />
                            </span>
                        </td>
                        <td class="px-4 py-2">6%</td>
                    </tr>
                    <tr class="hover:bg-gray-50 border border-bg-secondary">
                        <td class=" px-4 py-2 text-base font-medium">Sonar</td>
                        <td class="px-4 py-2">
                            <span class="inline-flex">
                                <Status />
                            </span>
                        </td>
                        <td class="px-4 py-2">6%</td>
                    </tr>
                </tbody>

            </table>
        </div>
    </div>
</template>

<script setup>
import Shield from '../../assets/icons/dashboard/Shield.svg';
import Status from '@/components/dashboard/Status.vue';
</script>