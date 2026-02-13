<template>
    <div class="container bg-background flex flex-col gap-10 md:gap-4 place-content-center">
        <BaseAlert v-if="errorAuthen" type="error" title="Error" message="Email already registered" />
        <BaseAlert v-if="success" type="success" title="Success" message="register successful" />
        <div class="card-register">
            <form novalidate class="form-register grid grid-cols-2 gap-y-4 md:gap-y-6" @submit.prevent="handleSubmit">
                <div class="flex flex-col col-span-2 gap-2 place-self-center">   
                    <h1 class="text-3xl md:text-5xl tracking-wide text-primary font-semibold">
                        Register
                    </h1>
                    <p class="text-xs md:text-sm font-regular">Sign up to start</p>
                </div>    
                <RegisterInputBox v-model="form.firstName" topic="First Name" :error="errors.firstName" class="sm:col-span-1"/>
                <RegisterInputBox v-model="form.lastName" topic="Last Name" :error="errors.lastName" class="sm:col-span-1"/>
                <RegisterInputBox v-model="form.username" topic="Username" :error="errors.username" />
                <RegisterInputBox v-model="form.email" topic="Email" :error="errors.email" :error_authen="errorAuthen" type="email" :error_email_form="errorEmailForm" />
                <div class="col-span-2">
                    <RegisterInputBox 
                        v-model="form.password" 
                        topic="Password" 
                        type="password" 
                        :error="errors.password" 
                        :passwordWarning="showPasswordWarning" 
                    />
                    <CheckPassword 
                        ref="checkPasswordComponent" 
                        :password="form.password" 
                        class="password-check" 
                        @validation="val => showPasswordWarning = val"
                    />
                </div>
                <RegisterInputBox v-model="form.company" topic="Company" :error="errors.company" />
                <!-- <button :disabled="!isFormValid" class="button-login col-span-2 disabled:opacity-50 disabled:cursor-not-allowed">submit</button> -->
                <button class="button-login col-span-2">submit</button>
            </form>
            <div class="md:px-6">
                <Or />
                <button 
                    class="signin-google">
                        <img :src="googleImage" alt="Google Icon" class="w-5 h-5 mr-2">
                        Sign in with Google
                </button>
            </div>
        </div>
        <button
            @click="router.push('/login')" 
            class="flex md:ml-28 text-primary self-center items-center md:self-start gap-2 cursor-pointer">
            <img src="../assets/icons/Register-Vector.png" class="w-4 h-3">
            Back
        </button>
    </div>
</template>

<script setup>
import { reactive , ref, inject, watch} from 'vue'
import RegisterInputBox from '../components/RegisterInput.vue'
import googleImage from '../assets/icons/google-logo.png'
import { useRouter } from 'vue-router'
import BaseAlert from '../components/BaseAlert.vue'
import CheckPassword from '../components/CheckPassword.vue' 
import Or from '../components/Or.vue' 

const api = inject('api');
const error = ref('');
const router = useRouter();
const errorAuthen = ref(false);
const success = ref(false);
const checkPasswordComponent = ref(null);
const showPasswordWarning = ref(false);
const errorEmailForm = ref(false);

const form = reactive({
    firstName: '',
    lastName: '',
    username: '',
    email: '',
    password: '',
    company: ''
})

const errors = reactive({
    firstName: false,
    lastName: false,
    username: false,
    email: false,
    password: false,
    company: false
})

const passwordRules = {
  length: /.{8,}/,
  upper: /[A-Z]/,
  lower: /[a-z]/,
  number: /[0-9]/,
  special: /[^A-Za-z0-9]/
}

// Watch for email changes and clear error when user edits
watch(
  () => ({ ...form }),
  (newVal, oldVal) => {
    for (const key in newVal) {
      if (newVal[key] !== oldVal[key] && errors[key]) {
        errors[key] = false
      }
    }
  }
)

// Check email format + Clear email form error when user edits 
watch(() => form.email, (newEmail) => {
  const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  
  if (!newEmail) {
    errorEmailForm.value = false; // ถ้าว่างให้ล้าง error
  } else {
    // ถ้ามีค่า ให้เก็บผลลัพธ์ว่า "ผิด" หรือ "ถูก"
    errorEmailForm.value = !pattern.test(newEmail.trim());
  }
});

// Watch for password changes and update warning style
watch(() => form.password, () => { 
    if (checkPasswordComponent.value) {
        showPasswordWarning.value = checkPasswordComponent.value.shouldShowErrors.value
    }
})

const handleSubmit = async () => {
    // Reset errors
    Object.keys(errors).forEach(key => {
        errors[key] = false
    })
    
    error.value = ''

    // Validate required fields
    Object.keys(errors).forEach(key => {
        (form[key].trim()) 
        ? null
        : errors[key] = true
    })

    // Check if there are any errors
    const hasErrors = Object.values(errors).some(error => error)
    
    // Check password validation
    const passwordHasErrors = !form.password || !(
      passwordRules.length.test(form.password) &&
      passwordRules.upper.test(form.password) &&
      passwordRules.lower.test(form.password) &&
      passwordRules.number.test(form.password) &&
      passwordRules.special.test(form.password)
    )

    // const handleAsync = async (promise) => {
    // try {
    //     const data = await promise;
    //     return [null, data]; // [error, data]
    // } catch (error) {
    //     return [error, null];
    // }
    // };

    if (!hasErrors && !passwordHasErrors) {
    // if (!hasErrors) {
        try {
            const response = await api.post('/register', {
                    email: form.email,
                    password: form.password,
                    name: form.firstName,
                    surname: form.lastName,
                    username: form.username,
                });

                success.value = true;
                console.log("success value", success.value)
                setTimeout(() => {
                success.value = false;
            }, 5000);

        } catch (e) {
            (! e.status === 409) 
                ? error.value = 'Backend Error.'
                : errorAuthen.value = true
        };
        console.log("Authen value", errorAuthen.value)
        setTimeout(() => {
                errorAuthen.value = false;
            }, 5000);
    }
}
</script>