<script setup>
import { RouterView } from 'vue-router';
import TheHeader from '@/components/TheHeader.vue';
import TheFooter from '@/components/TheFooter.vue';

</script>

<template>
  <TheHeader />
  <main>
    <RouterView />
  </main>
  <TheFooter />
</template>

<style lang="scss">
    @import 'https://fonts.googleapis.com/css2?family=PT+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap';
    @import 'https://fonts.googleapis.com/css2?family=PT+Serif:ital,wght@0,400;0,700;1,700&display=swap';

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        font-weight: 400;
        font-family: 'PT Sans', sans-serif;
    }

    .visually-hidden {
        position: absolute;
        width: 1px;
        height: 1px;
        margin: -1px;
        clip: rect(0, 0, 0, 0);
    }

    html {
        width: 100%;
        max-width: 100%;
        font-size: 0.62 !important;
        line-height: 1.5 !important;
    }

    main {
        padding-top: 100px;
    }
</style>


