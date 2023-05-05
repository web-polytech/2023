<template>
  <div>
    <section class="promo">
      <h1 class="promo__heading">Школьная жизнь</h1>
      <p class="promo__decsription">Создаем условия для активного и здорового образа жизни, способствуем культурному и творческому развитию и позволяем преобретать навыки</p>
    </section>
    <section class="clubs">
      <div class="clubs__wrapper">
        <h2 class="clubs__heading">Школьные объединения</h2>
        <ul class="clubs__list">
          <li class="clubs__card" v-for="item in clubs">
            <SchoolLifeClubsCard :content="item" class="clubs-card" />
          </li>
        </ul>
      </div>
    </section>
    <section class="sports">
      <div class="sports__wrapper">
        <h2 class="sports__heading">Спортивные секции</h2>
        <ul class="sports__list">
          <li class="sports__card" v-for="item in sports">
            <SchoolLifeSportsCard :content="item" class="sports-card" />
          </li>
        </ul>
      </div>
    </section>
    <section class="lectures">
      <h2 class="lectures__heading">Лекции и курсы в Нашей школе <span class="lectures__heading lectures__heading_blue">(new)</span></h2>
      <ul class="lectures__list">
        <li class="lectures__card" v-for="item, index in lectures" :key="index" :id="'lectures'+(index+1)">
          <SchoolLifeLecturesCard :content="item" :color="(index==1||index==3||index==4||index==5)?'white':'default'" :position="(index==4)?'right':'default'" class="lectures-card" />
        </li>
      </ul>
    </section>
  </div>
</template>

<script>
import SchoolLifeClubsCard from '../components/SchoolLifeClubsCard.vue';
import SchoolLifeSportsCard from '../components/SchoolLifeSportsCard.vue';
import SchoolLifeLecturesCard from '../components/SchoolLifeLecturesCard.vue';

export default {
  components: {
    SchoolLifeClubsCard,
    SchoolLifeSportsCard,
    SchoolLifeLecturesCard,
  },
  data() {
    return {
      clubs: [
        {
          heading: 'Юношеско-подростковый клуб волонтеров “Юный активист”',
          text: 'Мы занимаемся волонтерством, экоактивизмом, помогаем детям и животным, а так же участвуем в различных мероприятиях.',
          image: 'SchoolLifeClubsCard1.webp',
        },
        {
          heading: 'Научное объединение Нашей школы “Наша наука” для средней и старшей школы',
          text: 'Разрабатываем проекты, пишем статьи на научные темы, выступаем на конференциях и форумах, работаем в командах.',
          image: 'SchoolLifeClubsCard2.webp',
        },
        {
          heading: 'Школьный журналистский клуб “Юнкор” для 5-11 классников',
          text: 'Наш клуб организует множество мероприятий и участвует в книжных вечерах, олимпиадах по журналистике, встречах поэтов, интеллектуальных играх и во многом другом.',
          image: 'SchoolLifeClubsCard3.webp',
        },
        {
          heading: 'Группа для начальной школы развития и доп. подготовки',
          text: 'Даем дополнительные знания ребенку, помогаем разобраться в трудных для него темах, расширяем его кругозор и способствуем поиску новых увлечений и заинтересованности в обучении в Нашей школе.',
          image: 'SchoolLifeClubsCard4.webp',
        },
        {
          heading: 'Научное объединение Нашей школы “Наша наука” для средней и старшей школы',
          text: 'Для любителей проводить время на свежем воздухе, активно отдыхать, учеников знающих ОБЖ и готовых отрядом путешествовать по красотам нашей природы.',
          image: 'SchoolLifeClubsCard5.webp',
        },
        {
          heading: 'Школьный журналистский клуб “Юнкор” для 5-11 классников',
          text: 'Мы ставим пьесы и постановки, которые популярно во всем мире. Роль мы найдем для каждого и всему научим, главное чтобы было желание прокачивать свое актерское и ораторское мастерство.',
          image: 'SchoolLifeClubsCard6.webp',
        },
      ],
      sports: [
        {
          heading: 'Команды по волейболу и баскетболу для начальной, средней и старшей школы.',
          image: 'SchoolLifeSportsCard1.webp',
        },
        {
          heading: 'Секция по шахматам и школьные команды по киберспортивным дисциплинам',
          image: 'SchoolLifeSportsCard2_2.webp',
        },
        {
          heading: 'Хокей, лыжный спорт, футбол на снегу, фигурное катания доступны в зимний сезон',
          image: 'SchoolLifeSportsCard3.webp',
        },
      ],
      lectures: [
        {
          heading: 'Как стать успешным?',
          text: 'Рост и развитие в своей сфере',
          image: 'SchoolLifeLecture1.svg',
        },
        {
          heading: 'Интернет в обучении',
          text: 'Как правильно искать информацию в сети?',
          image: 'SchoolLifeLecture2.svg',
        },
        {
          heading: 'Планирование',
          text: 'Как распланировать свой день правильно?',
          image: 'SchoolLifeLecture3.svg',
        },
        {
          heading: 'Доклады и презентации',
          text: 'Как и где их нужно делать?',
          image: 'SchoolLifeLecture4.svg',
        },
        {
          heading: 'Учись правильно!',
          text: 'Как повысить свою продуктивность?',
          image: 'SchoolLifeLecture5.svg',
        },
        {
          heading: 'Коммуникации вокруг нас',
          text: 'Учимся общаться и вести переписку',
          image: 'SchoolLifeLecture6.svg',
        },
      ],
    };
  },
};
</script>

<style lang="scss">
  $wrapper: var(--wrapper);
  $color-blue: #1333ab;
  $color-black: #000000;

  .promo {
    display: flex;
    flex-direction: column;
    justify-content: end;
    align-items: center;
    gap: 1rem;
    min-height: calc(100vh - 100px);
    background-image: url("../assets/images/SchoolLifePagePromo.webp");
    background-repeat: no-repeat;
    background-position-x: center;
    background-size: cover;
  }

  .promo__heading {
    padding-bottom: 1rem;
    color: #ffffff;
    font-weight: 700;
    font-size: 3rem;
    font-family: 'PT Serif', sans-serif;
    line-height: 1;
    text-align: center;
  }

  .promo__decsription {
    max-width: 60ch;
    margin-bottom: 2rem;
    color: white;
    font-weight: 400;
    font-size: 1.75em;
    font-family: 'PT Sans', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', "Roboto", "Oxygen", "Ubuntu", "Cantarell", 'Open Sans', 'Helvetica Neue', sans-serif;
    font-style: normal;
    line-height: 1.4;
    text-align: center;
  }

  .clubs {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .clubs__wrapper {
    margin: 0 15px;
  }

  .clubs__heading {
    margin: 60px auto;
    font-weight: 700;
    font-size: 3rem;
    line-height: 1;
    text-align: center;
  }

  .clubs__list {
    display: flex;
    flex-flow: row wrap;
    justify-content: center;
    row-gap: 8rem;
    max-width: 1440px;
    margin-top: 9rem;
    column-gap: 1rem;
    list-style: none;
  }

  .clubs__card {
    max-width: 26rem;
  }

  .sports {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .sports__wrapper {
    margin: 0 15px;
  }

  .sports__heading {
    margin: 60px auto 40px;
    font-weight: 700;
    font-size: 3rem;
    line-height: 1;
    text-align: center;
  }

  .sports__list {
    display: flex;
    flex-flow: row wrap;
    justify-content: center;
    max-width: 1440px;
    list-style: none;
  }

  .lectures {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 2em;
  }

  .lectures__heading {
    margin: 30px 15px;
    font-weight: 700;
    font-size: 3rem;
    line-height: 1;
    text-align: center;
  }

  .lectures__heading_blue {
    color: #1333AB;
  }

  .lectures__list {
    display: grid;
    grid-template:
      "lecture1 lecture2" 278px
      "lecture3 lecture4" 278px
      "lecture5 lecture6" 278px / 1fr 1fr;
    gap: 24px;
    list-style: none;

    @media screen and (width <= 1440px) {
      grid-template:
        "lecture1" 278px
        "lecture2" 278px
        "lecture3" 278px
        "lecture4" 278px
        "lecture5" 278px
        "lecture6" 278px / 1fr;
      margin: 0 auto;
    }

    @media screen and (width <= 720px) {
      grid-template:
        "lecture1" 190px
        "lecture2" 190px
        "lecture3" 190px
        "lecture4" 190px
        "lecture5" 190px
        "lecture6" 190px / 1fr;
      margin: 0 auto;
    }

    @media screen and (width <= 490px) {
      grid-template:
        "lecture1" 126px
        "lecture2" 126px
        "lecture3" 126px
        "lecture4" 126px
        "lecture5" 126px
        "lecture6" 126px / 1fr;
      gap: 12px;
      margin: 0 auto;
    }
  }

</style>
