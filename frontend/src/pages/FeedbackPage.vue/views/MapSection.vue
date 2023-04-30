<template>
  <div class="requirements">
    <h2 class="requirements__heading">
      Наша школа на карте
    </h2>
    <iframe class="requirements__map" src="https://yandex.ru/map-widget/v1/?um=constructor%3A1c495c29179e90812d3630e05c7249ddc6b7da5920cc198d9ecc5cc64d268a35&amp;source=constructor" width="500" height="400" frameborder="0" />
  </div>
</template>

<script>
</script>


<style lang="scss" scoped>
  .requirements  {
    margin: 0;
  }

  .requirements__heading  {
    font-size: 3em;
    text-align: start
  }

  .yandex-map {
    width: 100%;
    min-height: 500px;
  }

  .requirements__map  {
    display: block;
    width: 100%;
    min-height: 600px;
    background-image: url('@/assets/images/FeedbackPage/MapScreenshot.png');
  }

</style>

