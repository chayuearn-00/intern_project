<template>
    <div>
      <Card>
        <LoginForm />
        <img src="../assets/images/cover.png" alt="cover" class="hidden md:block place-self-center object-cover object-center"/>
      </Card>
    </div>
</template>

<script setup>
import Card from '../components/Card.vue'; 
import LoginForm from '../components/LoginForm.vue';
</script>