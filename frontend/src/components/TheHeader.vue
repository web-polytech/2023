<template>
  <header class="header">
    <TheMenu />
    <TheSubMenu />
  </header>
</template>

<script setup>
import TheMenu from '../components/TheMenu.vue';
import TheSubMenu from '../components/TheSubMenu.vue';

</script>

<style lang="scss">
    .header {
        position: fixed;
        width: 100%;
    }
</style>
