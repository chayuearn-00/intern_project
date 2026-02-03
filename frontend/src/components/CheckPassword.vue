 <template>
    <transition>
        <div v-if="shouldShowErrors">
            <div class="text-sm mt-2 space-y-1">
                <span v-if="passwordErrors.length" class="absolute password-check">
                    Minimum 8 characters
                </span>
                <span v-if="passwordErrors.upper" class="absolute password-check">
                    One uppercase letter (A–Z)
                </span>
                <span v-if="passwordErrors.lower" class="absolute password-check">
                    One lowercase letter (a–z)
                </span>
                <span v-if="passwordErrors.number" class="absolute password-check">
                    One number (0–9)
                </span>
                <span v-if="passwordErrors.special" class="absolute password-check">
                    One special character (!@#$…)
                </span>
            </div>
        </div>
    </transition>
</template>

<script setup>
import { reactive, computed, watch} from 'vue'

const props = defineProps({
  password: {
    type: String,
    default: ''
  }
})

const passwordErrors = reactive({
  length: false,
  upper: false,
  lower: false,
  number: false,
  special: false,
})

const rules = {
  length: /.{8,}/,                 // อย่างน้อย 8 ตัว
  upper: /[A-Z]/,                  // พิมพ์ใหญ่
  lower: /[a-z]/,                  // พิมพ์เล็ก
  number: /[0-9]/,                 // ตัวเลข
  special: /[^A-Za-z0-9]/          // อักขระพิเศษ
}
 
function validatePassword() {
  const pwd = props.password || ''

  passwordErrors.upper = false
  passwordErrors.lower = false
  passwordErrors.number = false
  passwordErrors.special = false
  passwordErrors.length = false

  if (!rules.lower.test(pwd)) {
    passwordErrors.lower = true
  } else if (!rules.upper.test(pwd)) {
    passwordErrors.upper = true
  } else if (!rules.number.test(pwd)) {
    passwordErrors.number = true
  } else if (!rules.special.test(pwd)) {
    passwordErrors.special = true
  } else if (!rules.length.test(pwd)) {
    passwordErrors.length = true
  }
}

// Watch for password changes and validate
watch(() => props.password, () => {
  validatePassword()
}, { immediate: true })

const shouldShowErrors = computed(() => {
  return props.password.length > 0 && Object.values(passwordErrors).some(error => error)
})

const isPasswordValid = computed(() => {
  return props.password && !Object.values(passwordErrors).some(error => error)
})

// // Export validation state via defineExpose
defineExpose({
  shouldShowErrors,
  isPasswordValid,
})

// push state to event(emit) from child -> parent
const emit = defineEmits(['validation']);

watch(shouldShowErrors, (newVal) => {
  emit('validation', newVal)
})
</script>