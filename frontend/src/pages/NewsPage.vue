<template>
  <section class="main_news">
    <div class="main-news__wrapper">
      <h2 class="main-news__title">
        Главные новости
      </h2>
      <ul class="main-news__list">
        <li v-for="(item, index) in news" :key="index" :id="'news'+(index+1)" class="main-news__item main_news__item--big">
          <NewsCard :content="item" :type="(index==0||index==3)?'big':'default'" class="main-news__card" />
        </li>
      </ul>
    </div>
  </section>
<section class="other_news">
    <div class="other_news__wrapper">
      <h2 class="other_news__title">
        Последние новости
      </h2>
      <ul class="other_news__list">
        <li v-for="item, index in newo" :key="index" :id="'news'+(index+1)" class="last_news__item last_news__item--big">
          <HomeNewsCard :content="item"  class="other_news__card" />
        </li>
      </ul>
      <div class="other_news__action">
        <TheButton :path="'/news'" :label="'Больше новостей'" />
      </div>
    </div>
  </section>
</template>


<script>
import NewsCard from "@/components/NewsCard.vue";
import HomeNewsCard from "@/components/HomeNewsCard.vue"
import TheButton from '../components/TheButton.vue';

export default {
  name: "NewsPage",
  components: {
    NewsCard,
    HomeNewsCard,
    TheButton,

  },
  data() {
    return {
      news: [
        {
          imageSrc: 'Rectangle 2.png',
          title: 'НАУКА&ТЕХНОЛОГИИ',
          tagline: '1 сентября прошла торжественная церемония, посвященная началу учебного года в Нашей школе',
          text: 'Более 1200 учащихся пошло в Нашу школу в 2022 году, среди которых 210 первоклассников посетили свой первый урок. Восьмые классы теперь начнут учебы по выбранным специальностям, а для 11 классов этот год станет решающим и определяющим их будущее. Мы спросили у учащихся о том, готовы ли они к новому учебному году.',
        },
        {
          imageSrc: 'Rectangle 7.png',
          title: 'ШКОЛЬНАЯ ЖИЗНЬ',
          tagline: 'Прошло ежегодное собрание волонтерского клуба школы',
          text: 'Эко-активисты, молодые волонтеры, члены юношеской организации “Юный активист” 14 сентября провели собрание, где определили цели и задачи на 2022-2023 учебный год. Разработка стратегии, планирование мероприятий и назначение отвественных лиц – все это было выполнено на 45 минут.  Ребята подробно поделись своими планами.',

        },
        {
          imageSrc: 'Rectangle 3 .png',
          title: 'ОЛИМПИАДЫ',
          tagline: '4 победителя Всероссийского этапа олимпиады школьников',
          text: 'Крутников Алексей, Жасминова Александра, Иванов Денис, Васильева Ольга – победители Всероссийского этапа олимпиады школьников по биологии и химии. Ребята дали интервью, где поделились своими эмоциями и рассказали о том, как у них это получилось.',

        },
        {
          imageSrc: 'Rectangle 4 .png',
          title: 'ШКОЛЬНАЯ ЖИЗНЬ',
          tagline: 'Команда Нашей школы заняла первое место в игре  начальных классов школ города “Что? Где? Когда?” ',
          text: 'Уже в 6 раз команда умников и умниц из Нашей школы одерживают первое место в интеллектуальной игре “Что? Где? Когда?” среди школ города. В этом году отрыв в очках был рекордным, 24 балла составил разрыв между 2 местом и 1 местом. Мы узнали у ребят и их руководителя, как им это удалось.',

        },
        {
          imageSrc: 'Rectangle 5 .png',
          title: 'ШКОЛЬНАЯ ЖИЗНЬ',
          tagline: 'Учителя провели открытые уроки химии, физики и ОБЖ',
          text: 'Преподаватели многих школ области посетили организованные Нашей школой очные и дистанционные открытые уроки, где наши учителя продемонстрировали, как они используют современные технологии в обучении. Подробнее в репортаже наших юнкоров.',

        },
        {
          imageSrc: 'Rectangle 6 .png',
          title: 'НАУКА&ТЕХНОЛОГИИ',
          tagline: 'Набор учащихся 8-11 классов в конкурс IT-стартапов открыт',
          text: 'Каждый год Наша школа проводит среди 8, 9, 10 и 11 классов творческо интеллектуальный конкурс на идею лучшего стартапа. Первые участники уже представили свои идеи, но набор все еще открыт. Все желающие ученики старших классов могут выиграть крутые призы и получить спонсорскую помощь на развитие своих идей. ',

        },
      ],
      newo:[
        {
          name: '1 сентября прошла торжественная церемония, посвященная началу учебного года в Нашей школе',
          section: 'Наука & технологии',
          image: 'NewsCard1Big.webp',
        },
        {
          name: 'Прошло ежегодное собрание волонтерского клуба школы',
          section: 'Школьная жизнь',
          image: 'NewsCard2.webp',
        },
        {
          name: '4 победителя Всероссийского этапа олимпиады школьников',
          section: 'Олимпиады',
          image: 'NewsCard3.webp',
        },
        {
          name: 'Учителя провели открытые уроки химии, физики и ОБЖ',
          section: 'Наука & Технологии',
          image: 'NewsCard4.webp',
        },
        {
          name: 'Набор учащихся 8-11 классов в конкурс IT-стартапов открыт',
          section: 'Наука & Технологии',
          image: 'NewsCard5.webp',
        },
        {
          name: 'Команда Нашей школы заняла первое место в игре  начальных классов школ города “Что? Где? Когда?”',
          section: 'Школьная жизнь',
          image: 'NewsCard6Big.webp',
        },

      ]
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

  .main-news__title {
    margin: 60px auto;
    font-weight: 700;
    font-size: 3rem;
    line-height: 1;
    text-align: center;
  }

  .main-news__wrapper {
    max-width: 2800px;
    margin: 0 auto;
    padding: 0 40px;
  }

  .main-news__list {
    display: grid;
    grid-template:
      "news1 news1 news2 news3" 1fr
      "news4 news4 news5 news6" 1fr / 1fr 1fr 1fr 1fr;
    gap: 24px;
    list-style: none;
  }

  .other_news__list {
    display: grid;
    grid-template:
      "news1 news2 news3 news4" 360px
      "news5 news6 news7 news8" 360px / 1fr 1fr 1fr 1fr;
    gap: 24px;
    list-style: none;
  }

  .main-news__item {
    &#news1 {
      grid-area: news1;
    }

    &#news2 {
      grid-area: news2;
    }

    &#news3 {
      grid-area: news3;
    }

    &#news4 {
      grid-area: news4;
    }

    &#news5 {
      grid-area: news5;
    }

    &#news6 {
      grid-area: news6;
    }

    &#news7 {
      grid-area: news6;
    }

    &#news8 {
      grid-area: news6;
    }

  }

  .other_news__wrapper {
    max-width: 1400px;
    margin: 24px auto;
    padding: 0 40px;
  }

  .other_news__item {
    &#news1 {
      grid-area: news1;
    }

    &#news2 {
      grid-area: news2;
    }

    &#news3 {
      grid-area: news3;
    }

    &#news4 {
      grid-area: news4;
    }

    &#news5 {
      grid-area: news5;
    }

    &#news6 {
      grid-area: news6;
    }
  }

  .other_news__title {
    margin: 60px auto;
    font-weight: 700;
    font-size: 3rem;
    line-height: 1;
    text-align: center;
  }


  .other_news__action {
    display: flex;
    justify-content: end;
    margin-top: 36px;
  }
</style>
