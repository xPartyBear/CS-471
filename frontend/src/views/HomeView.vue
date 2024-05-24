<script setup>
  import PokemonSearch from '../components/PokemonSearch.vue';
  import PopupBox from '../components/PopupBox.vue';
  import PokedexEntry from '../components/PokedexEntry.vue';
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
    <PokedexEntry></PokedexEntry>
    <PopupBox v-if="displaySharePopup" @close="toggleShare()">
      <div class="center"> 
        <h1>{{isRight?"You win!":"You Lose!"}}</h1>
        <h3>Guesses:</h3>
        <p v-text="getGuesses()"></p>
        <h3>Points:</h3>
        <p v-text="getPoints()"></p>
        <h3>Streak:</h3>
        <p v-text="getStreak()"></p>

        <button @click="copyScore()" id="copy" style="margin-bottom: auto">Copy score</button>
      </div>
    </PopupBox>
  </div>
</template>

<script>
export default {
  data(){
    return {
      displaySharePopup: false,
      desiredPokemon: "pikachu",
      maxGuesses: 7,
      currentGuesses: 0,
      isRight: false,
    }
  },
  methods: {
    toggleShare(){
      //For now this is what it will do
      this.displaySharePopup = !this.displaySharePopup;
      return;
    },
    guess(value){
      console.log("TEST" + value + " " + this.desiredPokemon);
      //Desired Pokemon will need to be fetched
      if(value.toLowerCase() == this.desiredPokemon.toLowerCase()){
        //Call guesses here to check if they are correct
        this.isRight = true;
        this.toggleShare();
      }
      else{
        this.currentGuesses++;
        if(this.currentGuesses >= this.maxGuesses){
          this.toggleShare();
        }
      }
      return;
    },
    copyScore() {
      //Copy to clipboard
      navigator.clipboard.writeText(this.getScore+"\nPoints: "+this.getPoints+"\nStreak: "+this.getStreak);
      //Chance copy button
      document.getElementById("copy").innerHTML="Copied!"
    },
    getGuesses() {
      if(this.currentGuesses == null || this.maxGuesses == null) {
        return '';
      }
      let wrongs =(this.currentGuesses>0?"❌".repeat(this.currentGuesses-1):"");
      let wrongOrRight = (this.isRight?"✔️":((this.currentGuesses>0)?"❌":""));
      let remainingGuesses = "✖️".repeat(this.maxGuesses-this.currentGuesses);
      return wrongs + wrongOrRight + remainingGuesses;
    },
    getPoints: () => {
      return "5000"
    },
    getStreak: () => {
        return "7"
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
      return "5000"
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
    width: 50%
  }

  .center{
    text-align: center;
  }
  .guesses{
    font-size: 18px;
    text-align:center;
  }
</style>
