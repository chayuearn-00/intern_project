<script setup >
import NavBar from '../components/NavBar.vue';
import Footer from '../components/Footer.vue';
import InformationCard from '../components/InformationCard.vue';
import TextCard from '../components/TextCard.vue';

</script>

<template>
    <NavBar class="fixed w-full"/>
    <div class=" bg-white container overflow-hidden">
        <div class="max-w-[90%] lg:max-w-[70%] mx-auto pt-28">
            <div class="flex flex-col w-full place-content-center min-h-screen items-center m-auto ">
                <div class="grid grid-cols-2 w-full place-content-between">
                    <TextCard />
                    <InformationCard />
                </div>
                <div class="w-full mt-20">
                    <p class="text-center">Over 4M+ connected with us!</p>
                    <div class="footer_position">
                        <Footer />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template> 
    <!-- <img src="@/assets/Images/images_test.jpg" class="h-800" /> -->