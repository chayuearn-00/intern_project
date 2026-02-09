<template>
    <div>
        <p class="text-sm mb-4">Password*</p>
        <div class="relative">
            <input 
                :type="show ? 'text' : 'password'"
                :value="modelValue"
                @input="$emit('update:modelValue', $event.target.value)"
                :class="inputClass"
                @blur.self="check_password"
            /> 
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
        </div>
        <p v-if="error" class="absolute error-text">please fill this field</p>
    </div>
</template>

<script setup>
import { ref, computed , watch } from 'vue';
import eyeOff from '@/assets/icons/eye-off.png';
import eyeOn from '@/assets/icons/eye-on.svg';

const show = ref(false)

const props = defineProps({
    type: {
        type: String,
        default: 'Password*'
    },
    modelValue: String,
    error: {
        type: Boolean,
        default: false
    }
});

const check_password = () => {
    if (!props.modelValue) {
        emit('update:error',true)
    };
}

const inputClass = computed(() => [
    'w-full rounded-lg px-4 py-2 pr-10 outline-none',
    props.error
    ? 'border border-red-500 focus:ring-2 focus:ring-red-500'
    : 'border border-gray-300 focus:ring-2 focus:ring-brand'
]);

watch(() => props.modelValue, () => {
  if (props.modelValue) {
    emit('update:error',false)
  }
});

const emit = defineEmits([
    'update:modelValue',
    'update:error'
])

</script>