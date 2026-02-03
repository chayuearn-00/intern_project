<template>
    <button
        type="button"
        @click="show = !show"
        class="absolute right-3 top-1/2 -translate-y-1/2 cursor-pointer select-none text-sm"
    > 
        <img 
            :src="show ? eyeOn : eyeOff" 
            class="w-5 h-5" 
            alt="eye icon"
        />
    </button>
</template>

<script>
import eyeOff from '../assets/icons/eye-off.png';
import eyeOn from '../assets/icons/eye-off.png';

const props = defineProps({
    show: {
        type: Boolean,
        default: false,
    },
})

</script>