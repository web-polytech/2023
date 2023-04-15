<template>
  <div class="news-card">
    <img :src="'./public/Rectangle 4.png'" alt="" class="news-image">
    <div class="news-text-wrapper">
      <h2 class="news-title">{{ title }}</h2>
      <p class="news-tagline">{{ tagline }}</p>
      <p class="news-text">{{ text }}</p>
    </div>
  </div>
</template>


<script>
export default {
  name: "NewsCard",
  props: {
    imageSrc: {
      type: String,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    tagline: {
      type: String,
      required: true,
    },
    text: {
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
    position: relative;
    width: 100%;
    max-width: 600px;
    height: auto;
    margin: 0 auto;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    filter: drop-shadow(3px 3px 15px rgb(0 0 0 / 15%)) drop-shadow(0 0 10px rgb(0 0 0 / 15%));


     .news-image {
      width: calc(100% + 40px); // ширина изображения с учетом отступов
      height: auto;
      margin: -20px;


    }

    .news-title {
      margin-top: 1em;
      color: $color-blue;
      font-family: 'PT Serif';
      font-style: normal;
      font-weight: 700;
      font-size: 20px;
      line-height: 100%;
    }

    .news-tagline {
      font-size: 1.5em;
      margin-top: 0.5em;
      color: $color-black;
      font-weight: 700;
      font-family: "PT Sans";
      font-style: normal;
      line-height: 110%;
    }

    .news-text {
      font-size: 1em;
      margin-top: 1em;
      color: $color-black;
      font-weight: 400;
      font-family: "PT Sans";
      font-style: normal;
      line-height: 130%;
    }
  }

  @media screen and (min-width: 768px) {
    .news-title {
      font-size: 2.5em;
    }

    .news-tagline {
      font-size: 1.75em;
    }

    .news-text {
      font-size: 1.25em;
    }
  }
</style>
