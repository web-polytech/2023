<template>
  <div class="wrapper">
    <HeroSection class="wrapper__hero" />
    <DatesSection class="wrapper__dates" />
    <RequirementsSection class="wrapper__requirements" />
    <ApplicationFormSection id="form" class="wrapper__form" />
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

    @media (width <= 1210px) {
      padding-inline: 2rem;
    }
  }

</style>
