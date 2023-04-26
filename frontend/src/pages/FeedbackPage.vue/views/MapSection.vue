<template>
  <section class="requirements">
    <h2 class="requirements__heading">
      Наша школа на карте
    </h2>
    <yandex-map
      class="requirements__map"
      :coords="coords"
      :zoom="10"
      @click="onClick"
    >
      <ymap-marker
        :coords="coords"
        marker-id="123"
        hint-content="some hint"
      />
    </yandex-map>
  </section>
</template>

<script>
export default {
  data: () => ({
    coords: [
      54.82896654088406,
      39.831893822753904,
    ],
  }),
  methods: {
    onClick(e) {
      this.coords = e.get('coords');
    },
  },
};
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
    min-width: 200px;
    min-height: 100px;
  }

</style>

