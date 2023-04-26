<template>
  <div class="wrapper">
    <h1 class="wrapper__title">
      Свяжитесь с нами
    </h1>
    <ContactsSection />
    <FeedbackFormSection />
    <MapSection />
    <SocialSection />
  </div>
</template>

<script setup>
import ContactsSection from './ContactsSection.vue';
import FeedbackFormSection from './FeedbackFormSection.vue';
import MapSection from './MapSection.vue';
import SocialSection from './SocialSection.vue';
</script>


<style lang="scss" scoped>
  .wrapper {
    display: grid;
    grid-template-columns: 1.4fr 1fr;
    gap: 2rem;
    width: 100%;
    max-width: 1648px;
    margin: 0 auto;
    margin-bottom: 6rem;
  }

  .wrapper__title {
    grid-column: 1 / -1;
    margin-top: 1rem;
    margin-bottom: 4rem;
  }
</style>
