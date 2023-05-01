<template>
  <div class="wrapper">
    <HeroSection />
    <DatesSection />
    <RequirementsSection />
    <ApplicationFormSection id="form" />
  </div>
</template>

<script setup>
import HeroSection from './HeroSection.vue';
import DatesSection from './DatesSection.vue';
import RequirementsSection from './RequirementsSection.vue';
import ApplicationFormSection from './ApplicationFormSection.vue';
</script>


<style lang="scss" scoped>
  .wrapper {
    width: 100%;
    max-width: var(--wrapper);
    margin: 0 auto;
  }

 
</style>
