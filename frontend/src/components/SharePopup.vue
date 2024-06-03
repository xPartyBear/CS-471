<script setup>

</script>

<template>
    <PopupBox v-if="displaySharePopup" @close="toggleShare()">
      <div class="center"> 
        <h1>{{isRight?"You win!":"You Lose!"}}</h1>
        <img :src="todaysPokeImg" :alt="todaysPokemon">
        <br>
        Today's Pokemon: {{todaysPokemon}}
        <h3>Guesses:</h3>
        <p v-text="stats.guesses"></p>
        <h3>Points:</h3>
        <p v-text="stats.points"></p>
        <h3>Streak:</h3>
        <p v-text="stats.streak"></p>

        <button @click="copyScore()" id="copy" style="margin-bottom: auto">Copy score</button>
      </div>
    </PopupBox>
</template>

<script>
    export default {
        methods: {
            toggleShare(){
                //For now this is what it will do
                this.displaySharePopup = !this.displaySharePopup;
                //Disable Plays for the day
                return;
            },
        }
    }
</script>