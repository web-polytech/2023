<template>
  <section class="info">
    <div class="info__wrapper">
      <div class="info__text-wrapper">
        <h1 class="info__title">
          О Нашей Школе
        </h1>
        <p class="info__text">
          Мы дарим возможность творить,
          создавать, улучшать, реализовывать
          свои идеи и осуществлять мечты.
        </p>
      </div>
      <img src="../assets/images/School.webp" alt="Photo of school" class="info__image">
    </div>
    <ul class="info__list">
      <li class="info__item" v-for="item,index in info" :key="index">
        <p class="info__item-title">
          {{item.title}}
        </p>
        <p class="info__item-text">
          {{item.text}}
        </p>
        <p class="info__item-span">
          {{item.span}}
        </p>
      </li>
    </ul>
  </section>
  <section class="advantages">
    <h2 class="advantages__title">
      Преимущества Нашей школы
    </h2>
    <div class="advantages__wrap">
      <img class="advantages__image" src="../assets/images/Students.webp" alt="Students image">
      <ul class="advantages__list">
        <li class="advantages__item" v-for="item,index in advantages" :key="index">
          <p class="advantages__item-title">
            {{item.title}}
          </p>
          <p class="advantages__item-text">
            {{item.text}}
          </p>
        </li>
      </ul>
    </div>
  </section>
  <section class="admission">
    <p class="admission__text">
      Мы все еще проводим набор учеников в 1–4, 6–8 и 10 классы. <br>
      Успей подать заявку до 30 сентября — и получи приглашение на День открытых
      дверей и возможность уникальной консультации с приемной комиссией школы.
    </p>
    <TheButton :path="'#'" :label="'Узнать больше о поступлении'" type="light" />
  </section>
  <section class="teachers">
    <h2 class="teachers__title">
      Наш учительский состав
    </h2>
    <div class="teachers__wrap">
      <ul class="teachers__list">
        <li class="teachers__item" v-for="item,index in teachers" :key="index">
          <p class="teachers__item-title">
            {{item.title}}
          </p>
          <p class="teachers__item-text">
            {{item.text}}
          </p>
        </li>
      </ul>
      <div class="teachers__image-wrapper">
        <img src="../assets/images/Teacher1.webp" alt="Teacher image" class="teachers__image">
        <img src="../assets/images/Teacher2.webp" alt="Teacher image" class="teachers__image">
        <img src="../assets/images/Teacher3.webp" alt="Teacher image" class="teachers__image">
        <img src="../assets/images/Teacher4.webp" alt="Teacher image" class="teachers__image">
      </div>
    </div>
  </section>
  <section class="education">
    <h2 class="education__title">
      Образование
    </h2>
    <div class="education__wrapper">
      <div class="education__text-wrapper">
        <h3 class="education__subtitle">
          Программы обучения
        </h3>
        <p class="education__text">
          Мы предоставляем нашим учащимся возможность самостоятельного выбора специализации относительно их интересов.
        </p>
        <p class="education__text">
          С 8 класса Наша школа проводит профориентационное тестирование, которое позволяет практически точно определить склонности учащегося, его интересы и увлечения. При весм этом мы не навязываем определенную сферу деятельности, поэтому сменить специализацию можно в любой момент.
        </p>
      </div>
      <ul class="education__list">
        <li class="education__item" v-for="item,index in education" :key="index">
          <AboutProgramCard :content="item" />
        </li>
      </ul>
    </div>
  </section>
</template>
<script>
import TheButton from '../components/TheButton.vue';
import AboutProgramCard from '../components/AboutProgramCard.vue';

export default {
  components: {
    TheButton,
    AboutProgramCard,
  },
  data() {
    return {
      info: [
        {
          title: '>1200',
          text: 'учащихся',
          span: 'за 2021 год',
        },
        {
          title: '240',
          text: 'преподавателей',
          span: '',
        },
        {
          title: '8',
          text: 'специальностей',
          span: 'после 8 класса',
        },
        {
          title: '260',
          text: 'олимпиадников',
          span: 'за 2021 год',
        },
        {
          title: 'бесплатное',
          text: 'обучение и питание',
          span: '(кроме некоторых секций)',
        },
      ],
      advantages: [
        {
          title: 'Высокий уровень образования',
          text: 'Самое большое внимание мы уделяем индивидуальному обучению наших учеников. В дружеской конкурентной среде мы воспитываем в них целеустремленность и стойкость. Мы не просто даем знания, но и пытаемся заинтересовать учеников, чтобы каждый мог найти себя.',
        },
        {
          title: 'Интерактивная форма обучения',
          text: 'Современные технологии дарят множество возможностей для введения интерактива и игрового стиля в обучение. Благодаря новейшим сервисам и программам учащиеся лучше запоминают материал, а сами уроки становятся более веселыми и интересными, никому не дают заскучать.',
        },
        {
          title: 'Конкурсы, олимпиады и чемпионаты',
          text: 'Учащиеся Нашей школы принимают участие в сотнях различных мероприятиях, где часто занимают призовые места. Каждый ученик мечтает попасть на доску почета, стать героем школы, прославиться и получить бонусы, а наши учителя всегда готовы провести подготовку.',
        },
      ],
      teachers: [
        {
          title: 'Настоящие профессионалы своего дела',
          text: 'Наши учителя одни из самых специализированных в своих областях, у всех за плечами имеется опыт работы в крупнейших компаниях на высоких должностях, лучших школах или топ университетах страны. ',
        },
        {
          title: 'Кураторство, репетиторство и наставничество',
          text: 'Учителя умеют обучать, заинтересовывать и интересно преподносить материал, при всем этом они всегда помогут отстающему ученику и направят его в нужное русло. Если учащемуся интерес предмет или определенная область, то преподаватель это заметит и станет его куратором, после чего поможет ему разиваться в выбранной сфере.',
        },
        {
          title: 'Постоянное развитие',
          text: 'Не только учащиеся, но и преподаватели узнают новое, развиваются и прогрессируют. Мы старательно способствуем тому, чтобы учителя прокачивали свои навыки в изучении новых технологий, программных средств и навыков в обучении. Благодаря этому преподаватели дают максимум знаний, а учащиеся их полностью усваивают.',
        },
      ],
      education: [
        {
          title: 'Химия / Биология',
          text: 'Подходит для будущих медиков, химиков, экологов, или биологов, ну и работников промышленности.',
          image: 'ChembioCard.webp',
        },
        {
          title: 'Физика',
          text: 'Для будущих ученых, работников производств, авиа–ракето или машиностроения.',
          image: 'PhysicsCard.webp',
        },
        {
          title: 'Литература',
          text: 'Для желающих стать журналистом, дизайнером, переводчиком, писателем, актером или артистом.',
          image: 'LiteratureCard.webp',
        },
        {
          title: 'Информатика',
          text: 'Готовим профессиональных IT специалистов, а так же работников бизнес сферы.',
          image: 'InformaticsCard.webp',
        },
        {
          title: 'Обществознание',
          text: 'Юристы, работники суда, бухгалтеры, экономисты, работники бизнес отрасли.',
          image: 'SocialscienceCard.webp',
        },
        {
          title: 'Физическая культура',
          text: 'Мы готовим профессиональных спортсменов, тренеров, танцоров, а так же даем военную подготовку.',
          image: 'PhysicaleducationCard.webp',
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>

  .advantages,.education {
    max-width: 1440px;
    margin:auto;
  }

  .info,.advantages,.admission,.teachers,.education {
    &__title {
      padding-right: 20px;
      padding-left: 20px;
      font-weight: 700;
      font-size: 3.2rem;
      line-height: 1;
      text-align: center;

      @media screen and (width <= 600px) {
        font-size: 2.4rem;
      }
    }

    &__text {
      font-size: 1.4rem;
      line-height: 1.2;
    }
  }

  .info {
    display: flex;
    flex-direction: column;
    align-items: center;

    &__title{
      margin-top: 40px;
      font-family: 'PT Serif', sans-serif;
    }

    &__text {
      max-width: 675px;
      margin: 36px 0 38px;
      text-align: center;
    }

    &__image {
      width: 100%;
      max-width: 2400px;
      height: calc(100vh - 300px);
      object-fit: cover;
    }

    &__wrapper {
      display: flex;
      flex-direction: column;
      align-items: center;
      height: 100vh;
      text-align: center;
    }

    &__text-wrapper {
      height: 200px;
    }

    &__list {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-evenly;
      gap:20px;
      width: calc(100% - 40px);
      max-width: 1440px;
      margin: 0 auto 40px;
      padding: 36px;
      font-family: 'PT Serif', sans-serif;
      list-style: none;
      border-top: 1px solid #B5BBCB;
      border-bottom: 1px solid #B5BBCB;
    }

    &__item {
      display: flex;
      flex-direction: column;
      align-items: center;

      &-title {
        font-weight: 700;
        font-size: 2.4rem;
        line-height: 1.2;
      }

      &-text {
        font-size: 1.4rem;
        line-height: 1;
      }

      &-span {
        font-size: 1.1rem;
        font-style: italic;
      }
    }
  }

  .advantages,.teachers,.education {
    &__item {
      &-title {
        font-weight: 700;
        font-size: 1.8rem;
      }

      &-text {
        font-size: 1.2rem;
      }
    }
  }

  .advantages {
    &__wrap {
      display: flex;
      align-items: center;
      margin-top: 40px;
      margin-bottom: 40px;

      @media screen and (width <= 1330px) {
        flex-direction: column;
        margin-bottom: 0;
      }
    }

    &__image {
      max-width: 780px;
      max-height: 560px;
      object-fit: cover;
      margin: 0 40px;

      @media screen and (width <= 780px) {
        max-width: 100%;
      }
    }

    &__list {
      z-index: -1;
      margin-left: -144px;
      padding: 42px 40px 22px 188px;
      list-style: none;
      background-color: #F6F6F6;

      @media screen and (width <= 1330px) {
        margin: 40px;
        padding: 20px;
      }
    }

    &__item {
      margin-bottom: 20px;

      &-title {
        margin-bottom: 20px;
        line-height: 1.2;
      }
    }

  }

  .admission {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    gap:40px;
    max-width: 100%;
    min-height: 280px;
    padding: 40px;
    text-align: center;
    background-color: #1C52A2;

    &__text {
      max-width: 800px;
      color: white;

    }
  }

  .teachers {
    background-color: #F6F6F6;

    &__wrap {
      display: flex;
      align-items: center;
      max-width: 1440px;
      margin: auto;

      @media screen and (width <= 1330px) {
        flex-direction: column;
      }
    }

    &__title {
      box-sizing: content-box;
      margin-bottom: 40px;
      padding-top: 40px;
    }

    &__image {
      object-fit: cover;

      &-wrapper {
        display: flex;
        flex-wrap: wrap;
        gap:20px;
        width: 100%;
        min-width: 745px;

        @media screen and (width <= 1330px) {
          max-width: 745px;
          margin: auto;
          padding-bottom: 40px;
        }

        @media screen and (width <= 780px) {
          flex-wrap: nowrap;
          min-width: 0;
          overflow-x: scroll;
        }
      }
    }

    &__list {
      margin-right: -110px;
      margin-bottom: 184px;
      padding: 40px 168px 20px 60px;
      list-style: none;
      background-color: white;

      @media screen and (width <= 1330px) {
        margin: 0 40px 40px;
        padding: 20px;
      }
    }

    &__item {
      margin-bottom: 20px;

      &-title {
        margin-bottom: 20px;
        line-height: 1.2;
      }
    }
  }

  .education {
    &__title {
      margin-top: 40px;
      margin-bottom: 40px;
    }

    &__wrapper {
      display: flex;
      justify-content: space-between;
      margin: 40px;

      @media screen and (width <= 1050px) {
        flex-direction: column;
        align-items: center;
        gap: 40px;
      }
    }

    &__text-wrapper {
      display: flex;
      flex-direction: column;
      gap:20px;
      max-width: 440px;
    }

    &__subtitle {
      color: #1333AB;
      font-weight: 700;
      font-size: 1.8rem;
    }

    &__list {
      display: grid;
      grid-template-columns: repeat(3,1fr);
      gap: 0;
      list-style: none;

      @media screen and (width <= 1330px) {
        grid-template-columns: repeat(2,1fr);
      }

      @media screen and (width <= 615px) {
        grid-template-columns: repeat(1,1fr);
      }
    }
  }

</style>
