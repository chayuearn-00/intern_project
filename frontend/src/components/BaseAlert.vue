<template>
    <Transition name="fade-slide">
        <div
        v-if="visible" class="base-alert" :class="alertClass">
        <!-- Icon -->
        <span class="text-2xl leading-none self-center">
        {{ icon }}
    </span>
    <!-- Content -->
    <div class="flex-1 text-lg">
        <p class="font-medium">
            {{ title }}
        </p>
        <p class="opacity-90">
            {{ message }}
        </p>
    </div>
    <!-- Close
    <button
    class="opacity-60 hover:opacity-100 transition"
    @click="close"
    >
    ✕
</button> -->
</div>
</Transition>
</template>

<script setup>
import { ref, computed} from 'vue'

const alertClass = computed(() => styles[props.type])
const icon = computed(() => icons[props.type])

const props = defineProps({
    type: {
        type: String,
        default: 'info',
    },
    title: String,
    message: String,
    //   duration: {
        //     type: Number,
        //     default: 3000,
        //   },
    })
    
const visible = ref(true)
    
const styles = {
  success: 'bg-green-100 text-green-800',
  warning: 'bg-yellow-100 text-yellow-800',
  error: 'bg-red-100 text-red-800',
  info: 'bg-blue-100 text-blue-800',
}

const icons = {
  success: '✅',
  warning: '⚠️',
  error: '❌',
  info: 'ℹ️',
}

</script>
