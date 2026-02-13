<script setup >
import NavBar from '../components/NavBar.vue';
import Footer from '../components/Footer.vue';
import InformationCard from '../components/InformationCard.vue';
import TextCard from '../components/TextCard.vue';

</script>

<template>
    <NavBar class="fixed w-full"/>
    <div class="container overflow-hidden">
        <div class="max-w-full lg:max-w-[80%] mx-auto pt-0">
            <div class="flex flex-col w-full place-content-center min-h-screen items-center m-auto ">
                <div class="lg:grid lg:grid-cols-2 lg:gap-8 w-full place-content-between">
                    <TextCard />
                    <InformationCard class="lg:block hidden"/>
                </div>
                <div class="flex flex-col w-full mt-8 lg:mt-20">
                    <p class="text-center text-xs">Over 4M+ connected with us!</p>
                    <div class="footer_position">
                        <Footer />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template> 
    <!-- <img src="@/assets/Images/images_test.jpg" class="h-800" /> -->