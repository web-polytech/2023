<template>
  <div class="news-card" :class="{'news-card--big': type=='big'}">
    <img :src="'src/assets/images/'+content.imageSrc" alt="" class="news-image" >
    <div class="news-text-wrapper">
      <h2 class="news-title">{{ content.title }}</h2>
      <p class="news-tagline">{{ content.tagline }}</p>
      <p class="news-text">{{ content.text }}</p>
    </div>
  </div>
</template>


<script>
export default {
  name: "NewsCard",
  props: {
    content: {
      type: Object,
      required: true,
    },
    type: {
      type: String,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
  $color-blue: #1333ab;
  $color-black: #000000;

  .news-card {
    width: 100%;
    max-width: 600px;
    height: auto;
    margin: 0 auto;
    padding: 20px;
    background-color: #ffffff;
    box-shadow: 0 4px 10px rgb(0 0 0 / 10%);
    filter: drop-shadow(3px 3px 15px rgb(0 0 0 / 15%)) drop-shadow(0 0 10px rgb(0 0 0 / 15%));

    &--big {
      width: 800px;
    }


    .news-image {
      width: calc(100% + 40px); // ширина изображения с учетом отступов
      height: auto;
      margin: -20px;
    }

    .news-title {
      margin-top: 1em;
      color: $color-blue;
      font-weight: 700;
      font-size: 20px;
      font-family: 'PT Serif';
      font-style: normal;
      line-height: 100%;
    }

    .news-tagline {
      margin-top: 0.5em;
      color: $color-black;
      font-weight: 700;
      font-size: 1.5em;
      font-family: "PT Sans";
      font-style: normal;
      line-height: 110%;
    }

    .news-text {
      margin-top: 1em;
      color: $color-black;
      font-weight: 400;
      font-size: 1em;
      font-family: "PT Sans";
      font-style: normal;
      line-height: 130%;
    }
  }


</style>
