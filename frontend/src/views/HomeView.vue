<script setup>
  import PokemonSearch from '../components/PokemonSearch.vue';
  import PopupBox from '../components/PopupBox.vue';
  import PokedexEntry from '../components/PokedexEntry.vue';
  import pokemon from '../../services/pokemon.js';
</script>

<template>
  <div class = "Home">
    <br>
    <br>  
    <PokemonSearch @guess="guess" :guessEnabled="!isSearchDisabled()"></PokemonSearch>
    <br>
    <br>
    <br>
    <div class="guesses" v-text="getGuesses()"></div>
    current score: {{stats.points}}
    <PokedexEntry @reveal="modifyScore(100)"></PokedexEntry>
    <PopupBox v-if="displaySharePopup" @close="toggleShare()">
      <div class="center"> 
        <h1>{{isRight?"You win!":"You Lose!"}}</h1>
        <img :src="todaysPokeImg" :alt="todaysPokemon">
        <br>
        {{todaysPokemon}}
        <h3>Guesses:</h3>
        <p v-text="stats.guesses"></p>
        <h3>Points:</h3>
        <p v-text="stats.points"></p>
        <h3>Streak:</h3>
        <p v-text="stats.streak"></p>

        <button @click="copyScore()" id="copy" style="margin-bottom: auto">Copy score</button>
      </div>
    </PopupBox>
  </div>
</template>

<script>
export default {
  data() {
    return {
      displaySharePopup: false,
      maxGuesses: 7,
      currentGuesses: 0,
      isRight: false,
      stats: {
          guesses: '',
          points: 1000,
          streak: 0,
      },
      minimumScore: 0,
      todaysPokeImg: '',
      todaysPokemon: ''
    }
  },
  methods: {
    modifyScore(scoreChange){
      let newScore = this.stats.points - scoreChange;
      this.stats.points = Math.max(newScore, this.minimumScore);
    },
    toggleShare(){
      //For now this is what it will do
      this.displaySharePopup = !this.displaySharePopup
      return
    },
    date(){
      const fullDate = new Date();
      let day = fullDate.getDate();
      let month = fullDate.getMonth() + 1;
      let year = fullDate.getFullYear();
      return `${month}-${day}-${year}`;
    },
    async guess(value){
      //Desired Pokemon will need to be fetched
      const res = await pokemon.guess_pokemon(this.date(),value);
      this.currentGuesses++;
      console.log(res.data);
      if(res.data.res){
        //Call guesses here to check if they are correct
        this.isRight = true;
        this.toggleShare();
        const todaysPokemon = await pokemon.get_pokemon(this.date());
        console.log(todaysPokemon);
        this.todaysPokemon = todaysPokemon.data.name;
        this.todaysPokeImg = todaysPokemon.data.imgSrc;
      }
      else{
        this.modifyScore(50);
        if(this.currentGuesses >= this.maxGuesses){
          const todaysPokemon = await pokemon.get_pokemon(this.date());
          console.log(todaysPokemon);
          this.todaysPokemon = todaysPokemon.data.name;
          this.todaysPokeImg = todaysPokemon.data.imgSrc;
          this.toggleShare();
        }
      }
      return;
    },
    copyScore() {
      //Copy to clipboard
      navigator.clipboard.writeText(this.stats.guesses+"\nPoints: "+this.stats.points+"\nStreak: "+this.stats.streak);
      //Change copy button
      document.getElementById("copy").innerHTML="Copied!"
    },
    getGuesses() {
      if(this.currentGuesses == null || this.maxGuesses == null) {
        return '';
      }
      let wrongs =(this.currentGuesses>0?"❌".repeat(this.currentGuesses-1):"");
      let wrongOrRight = (this.isRight?"✔️":((this.currentGuesses>0)?"❌":""));
      let remainingGuesses = "✖️".repeat(this.maxGuesses-this.currentGuesses);
      this.stats.guesses = wrongs + wrongOrRight + remainingGuesses;
      return this.stats.guesses;
    },
    getPoints () {
        return this.stats.points;
    },
    getStreak () {
        return this.stats.streak;
    },
    isSearchDisabled() {
      return this.isRight || (this.currentGuesses>=this.maxGuesses);
    },
  },
  //May be easier to put in data, not sure how it will be retrieving this information
  //Moved out of 
  computed: {
    // moved out of computed because of the execution order of computed vs data, data variables aren't initialized before computed variables are made.
    /*
    getGuesses() {
      return ""
    },
    getPoints: () => {
      return '5000'
    },
    getStreak: () => {
        return "7"
    },
    */
  }
}
</script>

<style scoped>
.Home {
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}

  .center{
    text-align: center;
  }
  .guesses{
    font-size: 18px;
    text-align:center;
  }
</style>
