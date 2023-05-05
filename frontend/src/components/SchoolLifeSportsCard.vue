<template>
  <RouterLink to="#">
    <div class="sports-card">
      <img :src="'src/assets/images/'+content.image" alt="Sport-club image" class="sports-image">
      <h3 class="sports-tagline">{{content.heading}}</h3>
    </div>
  </RouterLink>
</template>

<script>
import { RouterLink } from 'vue-router';

export default {
  props: {
    content: {
      type: Object,
      required: true,
    },
    type: {
      type: String,
      required: true,
    },
  },
  methods: {
    replaceString(text) {
      let unionsAndPrepositions = ['так что', 'дабы', 'с тем чтобы', 'несмотря на то', 'хоть', 'пускай', 'хотя', 'если', 'если бы', 'коли', 'ежели', 'так как', 'потому что',
        'как будто', 'словно', 'точно', 'как', 'как бы', 'до такой степени', 'настолько', 'до того', 'такой', 'где', 'куда', 'откуда', 'когда', 'что', 'то есть',
        'а именно', 'и', 'да', 'не только', 'но и', 'также', 'тоже', 'и', 'ни', 'как', 'так', 'сколько', 'столько', 'или', 'либо', 'то', 'ли', 'не', 'то', 'а',
        'зато', 'однако', 'же', 'все же', 'чтобы', 'чтоб', 'притом', 'причём', 'в', 'без', 'до', 'из', 'к', 'на', 'по', 'о', 'от', 'перед', 'при', 'через', 'с', 'со', 'у',
        'и', 'нет', 'за', 'над', 'для', 'об', 'под', 'про'];

      for (let str of unionsAndPrepositions) {
        if (text.includes(' ' + str + ' ')) {
          text = text.replace(' ' + str + ' ', ' ' + str + String.fromCharCode(160));
        }
      }
      return text;
    },
  },
};
</script>

<style lang="scss">
  $wrapper: var(--wrapper);
  $color-blue: #1333ab;
  $color-black: #000000;

  .sports-card {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    max-width: 26rem;
    height: 100%;
    margin: 0 0.5rem 2rem;
    text-decoration: none;
    transition: box-shadow 150ms ease-in;

    @media screen and (width <= 490px) {
      max-width: 20rem;
    }
  }

  .sports-image {
    max-width: 26rem;
    height: auto;

    @media screen and (width <= 490px) {
      max-width: 20rem;
    }
  }

  .sports-tagline {
    margin-top: 0.5em;
    color: $color-black;
    font-weight: 700;
    font-size: 1.5em;
    font-family: "PT Sans";
    font-style: normal;
    line-height: 110%;
  }
</style>
