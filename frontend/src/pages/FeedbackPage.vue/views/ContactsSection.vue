<template>
  <section class="hero">
    <h1 class="hero__heading">
      Поступление
    </h1>
    <p class="hero__text">
      Мы ждем учеников, которые готовы реализовывать свои идеи, прокачивать свои навыки и всегда стремятся к самосовершенствованию.
    </p>
    <UIButton :light="true" :href="`#form`">
      Подача заявления
    </UIButton>
  </section>
</template>

<style lang="scss" scoped>
  $wrapper: var(--wrapper);

  .hero {
    display: flex;
    flex-direction: column;
    justify-content: end;
    align-items: center;
    gap: 1rem;
    min-height: calc(100vh - 100px);
    inline-size: 100vw;
    margin-inline-start: 50%;
    padding-bottom: 2rem;
    background-image: url('../../../assets/images/EntranceHero.jpg');
    background-repeat: no-repeat;
    background-position-x: center;
    background-size: cover;
    transform: translateX(-50%);
    padding-inline: calc((100% - #{$wrapper}) / 2);
  }


  .hero__heading {
    padding-bottom: 1rem;
    color: white;
  }

  .hero__text {
    max-width: 60ch;
    margin-bottom: 1rem;
    color: white;
    font-weight: 400;
    font-size: 1.75em;
    font-family: 'PT Sans', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', "Roboto", "Oxygen", "Ubuntu", "Cantarell", 'Open Sans', 'Helvetica Neue', sans-serif;
    font-style: normal;
    line-height: 1.4;
    text-align: center;
  }


</style>
