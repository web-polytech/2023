<template>
  <section class="main_news">
    <div class="main_news__wrapper">
      <h2 class="main_news__title">
        Последние новости
      </h2>
      <ul class="main_news__list">
        <li v-for="(item, index) in news" :key="index" :id="'news'+(index+1)" class="main_news__item main_news__item--big">
          <NewsCard
                v-for="article in news"
      :key="article.id"
      :imageSrc="article.imageSrc"
      :title="article.title"
      :tagline="article.tagline"
      :text="article.text"
      :type="article.type"/>
        </li>
      </ul>
    </div>
  </section>
</template>


<script>
import NewsCard from "@/components/NewsCard.vue";

export default {
  name: "NewsPage",
  components: {
    NewsCard,
  },
  data() {
    return {
      news: [
        {
          id: 1,
          imageSrc: './Rectangle 4.png',
          title: 'News title 1',
          tagline: 'News tagline 1',
          text: 'News content 1',
          type: 'breaking',


        },
        {
          id: 2,
          imageSrc: './Rectangle 7.png',
          title: 'News title 2',
          tagline: 'News tagline 2',
          text: 'News content 2',
          type: 'default',

        },

      ],
    };
  },
};
</script>

<style lang="scss" scoped>
  body {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  h1 {
    font-weight: 700;
    font-size: 64px;
    font-family: 'PT Sans';
    font-style: normal;
    line-height: 100%;
  }

  .main_news__title {
    margin: 60px auto;
    font-weight: 700;
    font-size: 3rem;
    line-height: 1;
    text-align: center;
  }

  .main_news__wrapper {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 40px;
  }

  .main_news__list {
    display: grid;
    grid-template:
      "news1 news1 news2 news3" 360px
      "news4 news5 news6 news6" 360px / 1fr 1fr 1fr 1fr;
    gap: 24px;
    list-style: none;
  }


</style>
