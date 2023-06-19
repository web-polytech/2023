import {defineStore} from 'pinia';
import axios from 'axios';

export const useNewsStore = defineStore('news', {
  state: () => {
    return {news: []};
  },
  actions: {
    async getNews() {
      try {
        const response = await axios.get('https://our-school.space/api/news/');
        this.news = response.data;
      } catch (error) {
        alert(error);
      }
    },
  },
  getters: {
    allNews(state) {
      return state.news;
    },
  },
});
