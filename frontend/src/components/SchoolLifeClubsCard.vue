<template>
  <RouterLink to="#">
    <div class="clubs-card">
      <img :src="'src/assets/images/'+content.image" alt="Club image" class="clubs-card__image">
      <div class="clubs-card__text-wrapper">
        <h3 class="clubs-card__tagline">{{content.heading}}</h3>
        <p class="clubs-card__text">{{content.text}}</p>
      </div>
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

  .clubs-card {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    height: 100%;
    text-decoration: none;
    box-shadow: 0 0 10px rgb(0 0 0 / 15%), 0 3px 3px rgb(0 0 0 / 15%);
    transition: box-shadow 150ms ease-in;

    &:hover {
      box-shadow: 0 0 10px rgb(0 0 0 / 20%), 0 7px 10px rgb(0 0 0 / 20%);

      & .clubs-card__image {
        transform:  scale(1.02);
        transition: transform 200ms ease;
      }
    }
  }

  .clubs-card__image {
    display: block;
    width: calc(100% - 3rem);
    height: auto;
    margin-top: -7rem;
  }

  .clubs-card__tagline {
    margin-top: 0.5em;
    padding: 0 1.5rem;
    color: $color-black;
    font-weight: 700;
    font-size: 1.5em;
    font-family: "PT Sans";
    font-style: normal;
    line-height: 110%;
  }

  .clubs-card__text {
    margin-top: 1em;
    padding: 0 1.5rem 3rem;
    color: $color-black;
    font-weight: 400;
    font-size: 1em;
    font-family: "PT Sans";
    font-style: normal;
    line-height: 130%;
  }
</style>
