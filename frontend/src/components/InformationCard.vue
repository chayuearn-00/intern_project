<template>
  <div class="flex items-center justify-center h-full">
    <div class="bg-white/70 backdrop-blur-md rounded-2xl shadow-xl lg:max-w-[632px] w-full p-6 space-y-4 lg:space-y-6">
        <div class="flex gap-2">
            <h2 class="text-primary font-semibold text-2xl">
                User
            </h2>
            <h2 class="text-myblone font-semibold text-2xl">
                 Information
            </h2>
        </div>

      <!-- Avatar + Username -->
      <div class="flex items-center gap-4 max-w-full">
        <div class="w-31.5 h-31.5 rounded-full bg-white flex items-center justify-center overflow-hidden shadow-md">
          <img src="@/assets/icons/LogoAvatar1.png" alt="Avatar" class="w-22 h-22 " />
        </div>
        <div class="flex-1 bg-white rounded-full max-full px-4 py-6 text-base lg:text-2xl text-center text-secondary font-semibold shadow-md">
          {{user?.name}}
        </div>
      </div>

      <!-- Data Box-->
      <div class="flex flex-col gap-4 lg:gap-8 ">
        <div>
            <div class="information-box">
                <label class="information-topic">Name:</label>
                <div class="flex flex-auto place-self-center justify-center gap-2">
                    <p class="information-text">{{ user?.name }}</p> 
                    <p class="information-text">{{ user?.surname }}</p>
                </div>
          </div>
        </div>

        <div>
            <div class="information-box">
                <label class="information-topic">Email:</label>
                <p class="information-text flex-auto">{{ user?.email }}</p>
          </div>
        </div>

        <div>
            <div class="information-box">
                <label class="information-topic">Company:</label>
                <p class="information-text flex-auto">MFEC Company Limited</p>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, inject , onMounted } from "vue"

const token = localStorage.getItem("access_token");
const api = inject('api');
const user = ref(null);

// onMounted(async () => {
//     const response = await api.get("/getdata")
//     user.value = response.data[0];
//     console.log(user.value)
// });
onMounted(async () => {
  try {
    const response = await api.get("/getdata")
    user.value = response.data[0]
  } catch (error) {
    console.log("Failed to fetch user data:", error)
  }
})

// const name = response.data.name;
// const surname = response.data.surname;
// const email = response.data.email;
// company: ''

  
</script>

