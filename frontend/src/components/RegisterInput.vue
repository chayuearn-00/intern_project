<template>
    <div class="flex flex-col md:px-5 gap-3 text-left col-span-2">
        <p class="text-sm md:text-base font-medium">
            {{ topic }}*
        </p>  
        <div class="relative">
            <input
                :type="type === 'password' ? (show ? 'text' : 'password') : type"
                :placeholder="topic"
                class="input-box-register"
                :class="{ 'input-box-register': !error && !error_authen && !error_email_form && !passwordWarning,
                          'input-error': error || error_authen || error_email_form || passwordWarning }"
                :value="modelValue" @input="$emit('update:modelValue', $event.target.value)" required="true"
                :readonly="type === 'email' ? readonly : false"
                >
                <div v-if="type === 'password'">
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
            <p v-if="error" class="absolute error-text">Please fill this feild.</p>
            <p v-if="error_email_form && (!error)" class="absolute error-text">Invalid email format</p>
        </div>
    </div>
</template>

<script setup>
import { readonly, ref } from 'vue';
import eyeOff from '../assets/icons/eye-off.png';
import eyeOn from '../assets/icons/eye-on.svg';

const show = ref(false)

const props = defineProps({
    topic: String,
    error: {
        type: Boolean,
        default: false,
    },
    type: {
        type: String,
        default: 'text'
    },
    modelValue: String,
    error_authen: Boolean,
    error_email_form: Boolean,
    passwordWarning: Boolean,
    readonly: {
        type: Boolean,
        default: false
    },
}
)
</script>