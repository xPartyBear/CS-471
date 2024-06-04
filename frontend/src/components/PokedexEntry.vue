<script setup>
import { toValue } from 'vue'
import pokemon from '../../services/pokemon'
import PokedexImg from './../assets/pokedex.png'
import MysteryImg from './../assets/mystery_symbol.png'
</script>

<template>
    <div class="container">
        <img class="mystery" :src="MysteryImg" style="width:450px; display: block; margin: 0 auto">
        <table class="table">
            <tr>
                <th @click="reveal('type1')">Type 1: {{pokemonInfo.type1}}</th>
                <th @click="reveal('type2')">Type 2: {{pokemonInfo.type2}}</th>
            </tr>
            <tr>
                <th @click="reveal('abilities')">Abilities: {{pokemonInfo.abilities}}</th>
                <th @click="reveal('height_weight')">Height and Weight: {{pokemonInfo.height_weight}}</th>
            </tr>
            <tr>
                <th @click="reveal('evo_method')">Evolution Method: {{pokemonInfo.evo_method}}</th>
                <th @click="reveal('evo_stage')">Evolution Stage: {{pokemonInfo.evo_stage}}</th>
            </tr>
            <tr>
                <th @click="reveal('egg_type')">Egg Type: {{pokemonInfo.egg_type}}</th>
            </tr>
            <tr>
                <th @click="reveal('region')">Region Origin: {{pokemonInfo.region}}</th>
                <th @click="reveal('form')">Form: {{pokemonInfo.form}}</th>
            </tr>
        </table>
    </div>
</template>

<script>
    export default {
        data(){
            return {
                pokemonInfo: {
                    "type1": "???",
                    "type2": "???",
                    "abilities": "???/???",
                    "evo_method": "???",
                    "height_weight": "??m /??? kg",
                    "evo_stage": "???",
                    "region": "???",
                    "form": "???",
                    "egg_type": "???/???",
                },
                hiddenInfo: {
                    "type1": "???",
                    "type2": "???",
                    "abilities": "???/???",
                    "evo_method": "???",
                    "height_weight": "??m /??? kg",
                    "evo_stage": "???",
                    "region": "???",
                    "form": "???",
                    "egg_type": "???/???",
                    // add cry
                    // add pokedex description
                }

            }
        },
        methods: {
            date(){
                const fullDate = new Date();
                let day = fullDate.getDate();
                let month = fullDate.getMonth() + 1;
                let year = fullDate.getFullYear();
                if(this.$route.params.month != null && this.$route.params.day != null && this.$route.params.year != null) {
                    this.pastPuzzleBeingPlayed = true;
                    return `${this.$route.params.month}-${this.$route.params.day}-${this.$route.params.year}`;
                }
                this.pastPuzzleBeingPlayed = false;
                return `${month}-${day}-${year}`;
            },
            async reveal(value,scoreEffected=true){
                // Fetch the data for the correct pokemon for the day
                // emit the score change upon reveal.
                if(!this.pokemonInfo[value] == this.hiddenInfo[value]){
                    return;
                }
                //get the pokedexInfo for that value
                const currentDate = pokemon.get_date(this.$route.params);
                const res = await pokemon.get_poke_info(currentDate,value);
                if(scoreEffected){
                    this.$emit('reveal');
                }
                // this.pokemonInfo[value] = this.hiddenInfo[value];
                this.pokemonInfo[value] = res.data;
                //apply the reveal to the score
                return;
            },
            revealRandom(){
                let keys = Object.keys(this.pokemonInfo);
                this.reveal(keys[Math.floor(keys.length * Math.random())],false);
                return;
            },
            revealAll(){
                let keys = Object.keys(this.pokemonInfo);
                for (i in keys){
                    this.reveal(i,false);
                }
            }
            
        },
        mounted(){
            this.revealRandom();
        },

    }

</script>

<style scoped>
    .container {
        color: lightgray;
        background-image: url('./../assets/pokedex.png');
        background-size: cover;
        height: 800px;
        width: 800px;
        margin: auto;
        position: absolute;
        top: 15%;
        left: 30%;
        z-index: -1;
    }
    th {
        border-width: 2px;
        border-style: dashed;
        user-select: none;
        padding: 15px;
    }
    th:hover {
        cursor: pointer;
        text-decoration: underline;
    }
    .bg {
        position: fixed;
        z-index: -1;
    }
    .table {
        scale: .80;
        max-width: 750px;
        position: absolute;
        top: 50%;
        left: 5%;
        font-size: 18px;
        font-family: "Courier New", monospace;

    }
    .mystery {
        position: absolute;
        scale:.7;
        top: 15%;
        left: 30%;
    }

</style>
