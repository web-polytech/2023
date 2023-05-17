<template>
  <section class="cover-block">
    <img class="cover-block__cover" src="@/assets/images/Profile/profile-cover01.webp" alt="cover profile">
    <div class="cover-block__wrapper">
      <div class="cover-block__badge cover-block__badge--left">
        <p class="cover-block__badge-text cover-block__class">
          10 А класс
        </p>
      </div>
      <div class="cover-block__badge cover-block__badge--right">
        <p class="cover-block__badge-text cover-block__status">
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
            <circle cx="8" cy="8" r="8" fill="#1CCD18" />
            <circle cx="8" cy="8" r="5" fill="#1CCD18" stroke="white" stroke-width="2" />
          </svg>
          В сети
        </p>
      </div>
      <div class="cover-block__avatar">
        <img src="@/assets/images/Profile/profile-avatar01.webp" alt="" class="cover-block__image">
      </div>
      <h2 class="cover-block__username">
        Кирилл Петров
      </h2>
    </div>
  </section>
  <div class="profile__content">
    <section class="dashboard" id="dashboard">
      <div class="dashboard__wrapper">
        <h3 class="dashboard__title">
          Панель управления
        </h3>
        <ul class="dashboard__control">
          <li class="dashboard__items" v-for="item, index in tiles" :key="index">
            <ProfileTile :tile="item" />
          </li>
        </ul>
      </div>
    </section>
    <section class="connect" id="connect">
      <div class="connect__wrapper">
        <h3 class="connect__title">
          Привязанные соц. сети
        </h3>
        <ul class="connect__list">
          <li class="connect__item" v-for="item, index in connect" :key="index">
            <ProfileConnect :resourse="item" />
          </li>
        </ul>
      </div>
    </section>
    <section class="exit" id="exit">
      <div class="exit__wrapper">
        <TheButton label="Выйти из аккаунта" path="exit" />
      </div>
    </section>
    <div class="profile__info" id="info">
      <section class="about" id="about">
        <div class="about__wrapper">
          <h3 class="about__title">
            Мои данные
          </h3>
          <ul class="about__list">
            <li class="about__item">
              <p class="about__key">
                Год поступления
              </p>
              <p class="about__value">
                {{user.start_education}}
              </p>
            </li>
            <li class="about__item">
              <p class="about__key">
                Год выпуска
              </p>
              <p class="about__value">
                {{user.end_education}}
              </p>
            </li>
            <li class="about__item">
              <p class="about__key">
                Профиль обучения
              </p>
              <p class="about__value">
                {{user.specialization}}
              </p>
            </li>
            <li class="about__item">
              <p class="about__key">
                Классный руководитель
              </p>
              <p class="about__value">
                {{user.mentor}}
              </p>
            </li>
            <li class="about__item">
              <p class="about__key">
                Средний балл
              </p>
              <p class="about__value">
                {{user.score}}
              </p>
            </li>
          </ul>
        </div>
      </section>
      <section class="advances" id="advances">
        <div class="advances__wrapper">
          <h3 class="advances__title">
            Мои достижения
          </h3>
          <ul class="advances__list">
            <li class="advances__item" v-for="item, index in user.advances" :key="index">
              <p class="advances__key">
                {{Object.keys(item)[0]}}
              </p>
              <p class="advances__value">
                {{Object.values(item)[0]}}
              </p>
            </li>
          </ul>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import ProfileTile from './ProfileTile.vue';
import ProfileConnect from './ProfileConnect.vue';
import TheButton from '@/components/TheButton.vue';

export default {
  components: {
    ProfileTile,
    ProfileConnect,
    TheButton,
  },
  props: {
    user: {
      type: Object,
      require: true,
      default: NaN,
    },
  },
  data() {
    return {
      tiles: [
        {
          title: 'Сообщения',
          path: 'icons/mail.svg',
          link: 'messages',
          count: 4,
          active: true,
        },
        {
          title: 'Электронный дневник',
          path: 'icons/diary.svg',
          link: 'diary',
          count: 0,
          active: true,
        },
        {
          title: 'Объявления',
          path: 'icons/notification.svg',
          link: 'notification',
          count: 2,
          active: true,
        },
        {
          title: 'Учащиеся',
          path: 'icons/students.svg',
          link: 'students',
          count: 0,
          active: true,
        },
        {
          title: 'Учителя и руководство',
          path: 'icons/administration.svg',
          link: 'administration',
          count: 0,
          active: true,
        },
        {
          title: 'Настройки',
          path: 'icons/settings.svg',
          link: 'settings',
          count: 0,
          active: true,
        },
        {
          title: 'Платные услуги',
          path: 'icons/payable.svg',
          link: 'payable',
          count: 0,
          active: true,
        },
        {
          title: 'Портфолио',
          path: 'icons/portfolio.svg',
          link: 'portfolio',
          count: 0,
          active: true,
        },
        {
          title: 'Электронная библиотека',
          path: 'icons/library.svg',
          link: 'digital-library',
          count: 0,
          active: true,
        },
        {
          title: 'Клубы и секции',
          path: 'icons/clubs.svg',
          link: 'clubs',
          count: 0,
          active: true,
        },
        {
          title: 'Экзамены',
          path: 'icons/exams.svg',
          link: 'exams',
          count: 0,
          active: false,
        },
        {
          title: 'Зачисление',
          path: 'icons/admission.svg',
          link: 'entrance',
          count: 0,
          active: false,
        },
      ],
      connect: [
        {
          title: 'Страница Вконтакте',
          desc: 'id 183490201',
          open_link: 'vk-open-token',
          close_link: 'vk-close-token',
          icon: 'vk',
        },
      ],
    };
  },
};
</script>

<style lang="scss">

  .profile__content {
    display: grid;
    grid-template:
      "dashboard info" auto
      "connect info" auto
      "exit info" auto / 7fr 5fr;
    gap: 40px;
    max-width: 1440px;
    margin: 0 auto;
    padding: 0 40px;
  }

  .cover-block__wrapper {
    position: relative;
    max-width: 1440px;
    margin: 0 auto;
    margin-bottom: 200px;
    padding: 0 40px;

    @media screen and (width <= 786px) {
      display: flex;
      flex-direction: column;
      padding: 0;
    }
  }

  .cover-block__cover {
    z-index: 0;
    width: 100%;
    height: 320px;
    margin: 0 auto;
    object-fit: cover;
  }

  .cover-block__username {
    position: absolute;
    right: 0;
    left: 0;
    margin-top: 64px;
    margin-right: auto;
    margin-left: auto;
    font-weight: 700;
    font-size: 3.2rem;
    font-family: 'PT Serif', sans-serif;
    line-height: 1;
    text-align: center;
  }

  .cover-block__avatar {
    position: absolute;
    right: 0;
    bottom: -64px;
    left: 0;
    margin-right: auto;
    margin-left: auto;
    text-align: center;
  }

  .cover-block__image {
    width: 300px;
    height: 300px;
    border: 16px solid #FFFFFF;
    border-radius: 50%;
    box-shadow: 3px 3px 15px rgb(0 0 0 / 10%), 0 0 10px rgb(0 0 0 / 10%);
  }

  .cover-block__badge {
    position: absolute;
    top: -230px;
    padding: 12px 16px;
    background: #FFFFFF;
    border-radius: 24px;
    box-shadow: 3px 3px 15px rgb(0 0 0 / 5%), 0 0 10px rgb(0 0 0 / 5%);

    &--left {
      left: calc(50% - 260px);
    }

    &--right {
      right: calc(50% - 260px);
    }
  }

  .cover-block__badge-text {
    font-weight: 700;
    font-size: 1.2rem;
    line-height: 1;
  }

  .cover-block__status {
    display: flex;
    align-items: center;
    gap: 10px;
    color: #1CCD18;
    text-transform: uppercase;
  }

  .dashboard__wrapper, .connect__wrapper {
    margin-bottom: 20px;
  }

  .dashboard__title, .connect__title, .about__title, .advances__title {
    margin-bottom: 36px;
    font-weight: 700;
    font-size: 1.8rem;
    line-height: 1;
    text-align: center;
  }

  .dashboard__control, .connect__list {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    list-style: none;
  }

  .about, .advances {
    height: fit-content;
    margin-bottom: 40px;
    background-color: #F2F1EB;
    border-radius: 16px;
  }

  .about__wrapper, .advances__wrapper {
    padding: 40px;
  }

  .about__list, .advances__list {
    display: flex;
    flex-direction: column;
    gap: 20px;
    list-style: none;
  }

  .about__item, .advances__item {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .about__key, .advances__key {
    width: 60%;
    max-width: 370px;
    font-size: 1.4rem;
    line-height: 1;
  }

  .about__value, .advances__value {
    width: 40%;
    max-width: 238px;
    color: #1C52A2;
    font-weight: 700;
    font-size: 1.4rem;
    line-height: 1;
  }

  #about {
    grid-area: about;
  }

  #connect {
    grid-area: connect;
  }

  #info {
    grid-area: info;
  }

  #exit {
    grid-area: exit;
  }

  .exit__wrapper {
    display: flex;
    justify-content: end;
    margin-bottom: 40px;
  }

  .advances__key {
    width: 120px;
  }

  .advances__value {
    width: 100%;
    max-width: 440px;
  }
</style>
