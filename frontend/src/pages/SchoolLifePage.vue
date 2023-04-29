<template>
  <section class="promo">
    <h1 class="promo__heading">Школьная жизнь</h1>
    <p class="promo__decsription">Создаем условия для активного и здорового образа жизни, способствуем культурному и творческому развитию и позволяем преобретать навыки</p>
  </section>
  <section class="section">
    <h2 class="section__heading">Школьные объединения</h2>
    <ul class="section__list">
      <li class="section__card">
        <div class="news-card">
          <img src="../assets/images/SchoolLifeClubsCard1.webp" alt="" class="news-image" >
          <div class="news-text-wrapper">
            <h3 class="news-tagline">Юношеско-подростковый клуб волонтеров “Юный активист”</h3>
            <p class="news-text">Мы занимаемся волонтерством, экоактивизмом, помогаем детям и животным, а так же участвуем в различных мероприятиях.</p>
          </div>
        </div>
      </li>
      <li class="section__card">
        <div class="news-card">
          <img src="../assets/images/SchoolLifeClubsCard1.webp" alt="" class="news-image" >
          <div class="news-text-wrapper">
            <h3 class="news-tagline">Юношеско-подростковый клуб волонтеров “Юный активист”</h3>
            <p class="news-text">Мы занимаемся волонтерством, экоактивизмом, помогаем детям и животным, а так же участвуем в различных мероприятиях.</p>
          </div>
        </div>
      </li>
      <li class="section__card">
        <div class="news-card">
          <img src="../assets/images/SchoolLifeClubsCard1.webp" alt="" class="news-image" >
          <div class="news-text-wrapper">
            <h3 class="news-tagline">Юношеско-подростковый клуб волонтеров “Юный активист”</h3>
            <p class="news-text">Мы занимаемся волонтерством, экоактивизмом, помогаем детям и животным, а так же участвуем в различных мероприятиях.</p>
          </div>
        </div>
      </li>
      <li class="section__card">
        <div class="news-card">
          <img src="../assets/images/SchoolLifeClubsCard1.webp" alt="" class="news-image" >
          <div class="news-text-wrapper">
            <h3 class="news-tagline">Юношеско-подростковый клуб волонтеров “Юный активист”</h3>
            <p class="news-text">Мы занимаемся волонтерством, экоактивизмом, помогаем детям и животным, а так же участвуем в различных мероприятиях.</p>
          </div>
        </div>
      </li>
    </ul>
  </section>
  <section class="section">
    <h2 class="section__heading">Спортивные секции</h2>
    <ul class="section__list">
      <li class="section__card">

      </li>
    </ul>
  </section>
  <section class="section">
    <h2 class="section__heading">Лекции и курсы в Нашей школе <span class="section__heading_blue">(new)</span></h2>
    <ul class="section__list">
      <li class="section__card">

      </li>
    </ul>
  </section>
</template>

<script>

</script>

<style lang="scss" scoped>
  $wrapper: var(--wrapper);
  $color-blue: #1333ab;
  $color-black: #000000;

  .promo {
    // display: flex;
    // flex-direction: column;
    // justify-content: end;
    // align-items: center;
    // gap: 1rem;
    // min-height: calc(100vh - 100px);
    // inline-size: 100vw;
    // margin-inline-start: 50%;
    // padding-bottom: 4rem;
    // background-image: radial-gradient(40.47% 40.47% at 50% 91.95%, rgb(28 82 162 / 98%) 0%, rgb(28 82 162 / 83.3%) 19.46%, rgb(28 82 162 / 73.5%) 52.42%, rgb(28 82 162 / 63.7%) 73.47%, rgb(28 82 162 / 0%) 100%), linear-gradient(0deg, rgb(28 82 162 / 10%), rgb(28 82 162 / 10%)), url('../assets/images/SchoolLifePagePromo.webp');
    // background-repeat: no-repeat;
    // background-position-x: center;
    // background-size: cover;
    // transform: translateX(-50%);
    // padding-inline: calc((100% - #{$wrapper}) / 2);
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

  // display: flex;
  // flex-direction: column;
  // align-items: center;
  // width: 100%;
  // height: 100%;
  // max-height: 100%;
  // padding: 0;

  .promo__heading {
    padding-bottom: 1rem;
    color: #ffffff;
    font-weight: 700;
    font-size: 3rem;
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

  .section {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .section__heading {
    margin: 60px auto;
    font-weight: 700;
    font-size: 3rem;
    line-height: 1;
    text-align: center;
  }

  .section__heading_blue {
    color: #1333AB;
    font-weight: 700;
    font-size: 3rem;
    line-height: 1;
  }

  .section__list {
    display: flex;
    flex-flow: row wrap;
    justify-content: center;
    row-gap: 8rem;
    margin-top: 7rem;
    column-gap: 1rem;
    list-style: none;
  }

  .section__card {
    max-width: 26rem;
  }

  .news-card {
    display: flex;
    align-items: center;
  }

  .news-image {
    display: block;
    width: calc(100% - 3rem); // ширина изображения с учетом отступов
    height: auto;
    margin-top: -7rem;
  }

  .news-tagline {
    margin-top: 0.5em;
    padding: 0 1.5rem;
    color: $color-black;
    font-weight: 700;
    font-size: 1.5em;
    font-family: "PT Sans";
    font-style: normal;
    line-height: 110%;
  }

  .news-text {
    margin-top: 1em;
    padding: 0 1.5rem 3rem;
    color: $color-black;
    font-weight: 400;
    font-size: 1em;
    font-family: "PT Sans";
    font-style: normal;
    line-height: 130%;
  }

  // .clubs-card {
  //   max-width: 250px;
  // }


</style>
