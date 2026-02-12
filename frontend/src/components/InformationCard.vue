<script>
// import LogoAvatar from '../assets/icons/LogoAvatar1.png';
// console.log(LogoAvatar);

</script>

<template>
  <div class="flex items-center justify-center from-blue-100 to-blue-300 h-full gap-14">
    <div class="bg-white/70 backdrop-blur-md rounded-2xl shadow-xl max-w-[632px]  w-full p-6 space-y-6">
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
        <div class="flex-1 bg-white rounded-full max-full px-4 py-6 text-2xl text-center text-secondary font-semibold shadow-md">
          USERNAME
        </div>
      </div>

      <!-- Data Box-->
      <div class="flex flex-col gap-8 ">
        <div>
            <div class="information-box">
                <label class="information-topic">Name:</label>
                <p class="information-text">Firstname Lastname</p>
          </div>
        </div>

        <div>
            <div class="information-box">
                <label class="information-topic">Email:</label>
                <p class="information-text">example@mfec.co.th</p>
          </div>
        </div>

        <div>
            <div class="information-box">
                <label class="information-topic">Company:</label>
                <p class="information-text">MFEC Company Limited</p>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>