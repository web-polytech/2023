<template>
  <div class="wrapper">
    <h1 class="wrapper__title">
      Свяжитесь с&nbsp;нами
    </h1>
    <ContactsSection class="wrapper__contacts" />
    <FeedbackFormSection class="wrapper__form" />
    <MapSection class="wrapper__map" />
    <SocialSection class="wrapper__social" />
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
    grid-template-columns: 1.5fr 1fr;
    grid-template-areas:
      "title title"
      "contacts form"
      "map social";
    grid-auto-flow: 1em;
    gap: 2rem;
    row-gap: 8rem;
    width: 100%;
    max-width: 1600px;
    margin: 0 auto;
    margin-bottom: 6rem;
    padding-inline: 2rem;
  }

  .wrapper__title {
    grid-area: title;
    margin-top: 1rem;
    margin-bottom: 4rem;
  }

  .wrapper__contacts {
    grid-area: contacts;
  }

  .wrapper__form {
    grid-area: form;
    width: 100%;
  }

  .wrapper__map {
    grid-area: map;
  }

  .wrapper__social {
    grid-area: social;
  }

  @media (width <= 1600px) {
    .wrapper {
      grid-template-columns: 1fr 1fr 1fr;
      grid-template-areas:
        "title title title"
        "form form form"
        "contacts contacts social"
        "map map map";
    }

    .wrapper__contacts {
      padding-inline: 0;
    }
  }

  @media (width <= 1210px) {
    .wrapper {
      grid-template-columns: 1fr;
      grid-template-areas:
        "title"
        "form"
        "map "
        "contacts"
        "social";
      row-gap: 2rem;
    }
  }

  @media (width <= 786px) {
    .wrapper {
      padding-inline: 0;
    }

    .wrapper__title {
      margin-bottom: 0;
      font-size: 3em;
    }

    .wrapper__form {
      padding: 1rem;
    }

    .wrapper__contacts {
      padding: 1rem;
    }

    .wrapper__map {
      text-align: center;
    }

    .wrapper__social {
      padding: 1rem;
    }
  }
</style>
