<script setup>
  import PokemonSearch from '../components/PokemonSearch.vue';
  import PopupBox from '../components/PopupBox.vue';
  import PokedexEntry from '../components/PokedexEntry.vue';
</script>

<template>
  <div class = "Home">
    <h1>This is the home page</h1>
    <PokemonSearch @guess="guess()"></PokemonSearch>
    <br>
    <br>
    <PopupBox v-if="displaySharePopup" @close="toggleShare()">
      <div class="center"> 
        <h1>You win!</h1>
        <h3>Guesses:</h3>
        <p v-text="getScore"></p>
        <h3>Points:</h3>
        <p v-text="getPoints"></p>
        <h3>Streak:</h3>
        <p v-text="getStreak"></p>

        <button @click="copyScore()" id="copy" style="margin-bottom: auto">Copy score</button>
      </div>
    </PopupBox>
    
    <PokedexEntry></PokedexEntry>
  </div>
</template>

<script>
export default {
  data(){
    return {
      displaySharePopup: false
    }
  },
  methods: {
    toggleShare(){
      //For now this is what it will 
      this.displaySharePopup = !this.displaySharePopup;
      return;
    },
    guess(){
      console.log("TEST");
      //Call guesses here to check if they are correct
      this.toggleShare();
      return;
    },
    copyScore() {
      //Copy to clipboard
      navigator.clipboard.writeText(this.getScore+"\nPoints: "+this.getPoints+"\nStreak: "+this.getStreak);
      //Chance copy button
      document.getElementById("copy").innerHTML="Copied!"
    }
  },
  //May be easier to put in data, not sure how it will be retrieving this information
  computed: {
    getScore: () => {
        return "❌❌✔️"
    },
    getPoints: () => {
        return "5000"
    },
    getStreak: () => {
        return "7"
    }
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
</style>
