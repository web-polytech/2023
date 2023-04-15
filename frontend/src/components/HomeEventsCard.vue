<template>
  <RouterLink to="#" class="events-card">
    <div class="events-card__cover">
      <img :src="'src/assets/images/'+content.image" class="events-card__image" alt="Image for event">
    </div>
    <p class="events-card__date">
      <span class="evant-card__day">{{content.day}}</span>{{content.month}}
    </p>
    <div class="events-card__info">
      <p class="events-card__section">
        {{content.section}}
      </p>
      <h4 class="events-card__name">
        {{replaceString(content.name)}}
      </h4>
    </div>
  </RouterLink>
</template>

<script>
import { RouterLink } from 'vue-router';

export default {
  props: ['content'],
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

  .events-card__cover {
    width: 100%;
    max-width: 812px;
    height: 100%;
    overflow: hidden;
  }

  .events-card__image {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .events-card__info {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 8px;
    height: auto;
    padding: 24px;
    background-color: #FFFFFF;
  }

  .events-card__date {
    position: absolute;
    right:16px;
    bottom: 100px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 84px;
    height: 84px;
    color: #FFFFFF;
    font-weight: 700;
    font-size: 1.2rem;
    font-family: 'PT Serif', sans-serif;
    line-height: 1;
    text-align: center;
    background-color: #0C3777;
    border-radius: 50%;
    box-shadow: 0 2px 4px rgb(0 0 0 / 25%);
  }

  .evant-card__day {
    font-weight: 700;
    font-size: 1.4rem;
    font-family: 'PT Serif', sans-serif;
    line-height: 1;
  }

  .events-card__section {
    color: #1333AB;
    font-weight: 700;
    font-size: 1rem;
    font-family: 'PT Serif', sans-serif;
    line-height: 1.1;
    text-transform: uppercase;
  }

  .events-card__name {
    min-height: 38px;
    color: #000000;
    font-weight: 700;
    font-size: 1.2rem;
    line-height: 1.1;
  }

  .events-card {
    position: relative;
    display: flex;
    flex-direction: column;
    width: 312px;
    height: 400px;
    text-decoration: none;
    box-shadow: 0 0 10px rgb(0 0 0 / 15%), 0 3px 3px rgb(0 0 0 / 15%);
    transition: box-shadow 150ms ease-in;

    &:hover {
      box-shadow: 0 0 10px rgb(0 0 0 / 20%), 0 7px 10px rgb(0 0 0 / 20%);

      & .events-card__image {
        transform:  scale(1.02);
        transition: transform 200ms ease;
      }
    }
  }

</style>
