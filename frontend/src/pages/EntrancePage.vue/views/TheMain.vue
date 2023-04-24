<template>
  <main class="wrapper">
    <HeroSection />
    <DatesSection />
    <RequirementsSection />
    <ApplicationSection />
  </main>
</template>

<script setup>
import HeroSection from './HeroSection.vue';
import DatesSection from './DatesSection.vue';
import RequirementsSection from './RequirementsSection.vue';
import ApplicationSection from './ApplicationSection.vue';
</script>


<style lang="scss" scoped>
  .wrapper {
    width: 100%;
    max-width: 1440px;
    margin: 0 auto;
  }
</style>
