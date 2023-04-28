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
          <HomeNewsCard :content="item" type="default" class="other_news__card" />
        </li>
      </ul>
      <div class="other_news__action">
        <TheButton :path="'/news'" :label="'Больше новостей'" />
      </div>
    </div>
  </section>
  <section class="magazine_club">
    <div class="magazine_club__wrapper">
      <h2 class="magazine_club__title">
        Приглашаем в журналистский клуб
      </h2>
      <p class="magazine_club__desc">
        Наша школа поддерживает своих учащихся в&nbsp;их&nbsp;начинаниях, проектах и&nbsp;иследовательских работах.
      </p>
      <div class="magazine_club__content">
        <div class="magazine club__cover">
          <img src="../assets/images/magazine_clubImage.webp" alt="Image for admission section" class="magazine_club__image">
        </div>
        <div class="magazine_club__info">
          <p class="magazine_club__text">
            Если вы любите писать сочинения или эссе, вам нравится посещать интересные мероприятия,  делиться своими впечатлениями и эмоциями с другими, вы хорошо знаете граматику и редко совершаете ошибки в речи и письме,  то двери в наш журналисткий клуб “Юнкор” для вас открыты.
          </p>
          <p class="magazine_club__text">
            Каждому активному юному журналисту мы вручаем пресс-карту, с которой он может посещать многие мероприятия города абсолютно бесплатно.
          </p>
          <p class="magazine_club__text">
            Мы проводим и участвуем в литературных вечерах, поэтических встречах, интеллектуальных играх, олимпиадах по журналистике и во многом другом.
          </p>
          <TheButton label="Узнать больше" type="border" path="entrance" />
        </div>
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
          name: 'Татьяна Алексеевна стала учителем года по региону',
          section: 'Школьная ЖИЗНЬ',
          image: 'Othernwes1.webp',
        },
        {
          name: 'Интервью с участниками клуба “Юные робототехники”',
          section: 'Наука & Технологии',
          image: 'Othernwes2.webp',
        },
        {
          name: 'В Нашей школе появилась секция – “Шахматный клуб”.',
          section: 'Школьная ЖИЗНЬ',
          image: 'Othernwes3.webp',
        },
        {
          name: 'Наши молодые чемпионы в городской спартакиаде',
          section: 'СПОРТ',
          image: 'Othernwes4.webp',
        },
        {
          name: 'Прошла игра по командному программированию 9 классов',
          section: 'Наука & Технологии',
          image: 'Othernwes5.webp',
        },
        {
          name: 'Турнир по футболу начальной, средней и старшей школы',
          section: 'СПОРТ',
          image: 'Othernwes6.webp',
        },
        {
          name: 'Самые активные ученики сентября уже получили призы',
          section: 'Школьная жизнь',
          image: 'Othernwes7.webp',
        },
        {
          name: 'Набор в группу театрального кружка у начальных классов',
          section: 'ТЕАТР',
          image: 'Othernwes8.webp',
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

    @media screen and (width <= 1086px) {
      grid-template:
        "news1 news1" 1fr
        "news2 news3" 1fr
        "news6 news6" 1fr
        "news4 news5" 1fr / 1fr 1fr;
      max-width: 812px;
      margin: 0 auto;
    }

    @media screen and (width <= 460px) {
      grid-template:
        "news1" 1fr
        "news2" 1fr
        "news3" 1fr
        "news5" 1fr
        "news4" 1fr
        "news6" 1fr / 1fr;
      max-width: 420px;
      margin: 0 auto;
    }


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

  .magazine_club__wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 1400px;
    margin: 0 auto;
    margin-bottom: 60px;
    padding: 0 40px;
  }


  .magazine_club__desc {
    max-width: 840px;
    margin-bottom: 40px;
    font-size: 1.8rem;
    line-height: 1.2;
    text-align: center;
  }

  .magazine_club__content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    align-items: center;
    gap: 80px;

    @media screen and (width <= 796px) {
      grid-template-columns: 1fr;
      gap: 40px;
    }
  }

  .magazine_club__cover {
    position: relative;
    max-width: 100%;
    height: 100%;
  }

  .magazine_club__title {
    margin: 60px auto;
    margin-bottom: 30px;
    font-weight: 700;
    font-size: 3rem;
    line-height: 1;
    text-align: center;
  }

  .magazine_club__image {
    width: 100%;
    min-width: 364px;
    object-fit: cover;
  }

  .magazine_club__info {
    display: flex;
    flex-direction: column;
    align-items: end;
    gap: 24px;
  }

  .magazine_club__text {
    font-size: 1.2rem;
    line-height: 1.2;
  }
</style>
