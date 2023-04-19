<template>
  <section class="info">
    <h1 class="info__title">
      О Нашей Школе
    </h1>
    <p class="info__text">
      Мы дарим возможность творить,
      создавать, улучшать, реализовывать
      свои идеи и осуществлять мечты.
    </p>
    <img src="../assets/images/School.webp" alt="Photo of school" class="info__image">
    <ul class="info__list">
      <li class="info__item" v-for="item in info">
        <p class="info__item-title">{{ item.title }}</p>
        <p class="info__item-text">{{ item.text }}</p>
        <p class="info__item-span">{{ item.span }}</p>
      </li>
    </ul>
  </section>
  <section class="advantages">
    <h2 class="advantages__title">
      Преимущества Нашей школы
    </h2>
    <img src="../assets/images/Students.webp" alt="Students image">
    <ul class="advantages__list">
      <li class="advantages__item" v-for="item in advantages">
        <p class="advantages__item-title">
          {{ item.title }}
        </p>
        <p class="advantages__item-text">
          {{ item.text }}
        </p>
      </li>
    </ul>
  </section>
  <section class="admission">
    <p class="admission__text">
      Мы все еще проводим набор учеников в 1–4, 6–8 и 10 классы.
    </p>
    <p class="admission__text">
      Успей подать заявку до 30 сентября — и получи приглашение на День открытых дверей и возможность уникальной консультации с приемной комиссией школы.
    </p>
    <TheButton :path="'#'" :label="'Узнать больше о поступлении'" type="light" />
  </section>
  <section class="teachers">
    <h2 class="teachers__title">
      Наш преподавательский состав
    </h2>
    <ul class="teachers__list">
      <li class="teachers__item" v-for="item in teachers">
        <p class="teachers__item-title">
          {{ item.title }}
        </p>
        <p class="teachers__item-text">
          {{ item.text }}
        </p>
      </li>
    </ul>
    <img src="../assets/images/Teacher1.webp" alt="Teacher image" class="teachers__image">
    <img src="../assets/images/Teacher2.webp" alt="Teacher image" class="teachers__image">
    <img src="../assets/images/Teacher3.webp" alt="Teacher image" class="teachers__image">
    <img src="../assets/images/Teacher4.webp" alt="Teacher image" class="teachers__image">
  </section>
  <section class="education">
    <h2 class="education__title">
      Образование
    </h2>
    <ul class="education__list">
      <li class="aducation__item" v-for="item in education">
        <p class="education__item-title">
          {{ item.title }}
        </p>
        <p class="education__item-text">
          {{ item.text }}
        </p>
        <img :src="'src/assets/images/'+item.image" alt="Direction image">
      </li>
    </ul>
  </section>
</template>
<script>
import TheButton from '../components/TheButton.vue';

export default {
  components: {
    TheButton,
  },
  data() {
    return {
      info:[
        {
          title:'>1200',
          text:'учащихся',
          span:'за 2021 год',
        },
        {
          title:'240',
          text:'преподавателей',
          span:'',
        },
        {
          title:'8',
          text:'специальностей',
          span:'после 8 класса',
        },
        {
          title:'260',
          text:'олимпиадников',
          span:'за 2021 год',
        },
        {
          title:'бесплатное',
          text:'обучение и питание',
          span:'(кроме некоторых секций)',
        }
      ],
      advantages:[
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
      teachers:[
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
      education:[
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
    }
  }
}
</script>
