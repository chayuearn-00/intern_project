<template>
    <div :class="classes">
        <span class="m-0">{{ status }}</span>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const props = defineProps ({
    device: {
        type: String,
        defailt: 'null'
    },
    value: Number,
});

function checkStatus(device, value) {
    if (device !== "sonar") {
        if(value < 20) return "LOW";
        else if(value < 50) return "WARN";
        else return "OK";
    } else if (device == "sonar") {
        if(value < 200) return "WARN";
        else return "SAVE";
    }
}

const status = computed(() => {
  return checkStatus(props.device, props.value)
})

const classes = computed(() => [
    'px-2.5 py-1 rounded-3xl right-0 text-white',
    (status.value == 'OK') 
        ? 'border border-status-bok bg-status-ok'
        : (status.value == 'SAVE')
            ? 'border border-status-bsafe bg-secondary'
            : (status.value == 'WARN')
                ? 'border border-status-bwarn bg-status-warn'
                : 'border border-status-blow bg-status-low'
]);


</script>