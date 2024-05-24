<script setup>
import { toValue } from 'vue';
import pokemon from '../../services/pokemon';
import PokedexImg from './../assets/pokedex.png';
import MysteryImg from  './../assets/mystery_symbol.png';
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
                <th @click="reveal('evoMethod')">Evolution Method: {{pokemonInfo.evoMethod}}</th>
            </tr>
            <tr>
                <th @click="reveal('stage')">Evolution Stage: {{pokemonInfo.stage}}</th>
                <th @click="reveal('hw')">Height and Weight: {{pokemonInfo.hw}}</th>
            </tr>
            <tr>
                <th @click="reveal('species')">Species: {{pokemonInfo.species}}</th>
                <th @click="reveal('eggType')">Egg Type: {{pokemonInfo.eggType}}</th>
            </tr>
            <tr>
                <th @click="reveal('origin')">Region Origin: {{pokemonInfo.origin}}</th>
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
                    "evoMethod": "???",
                    "hw": "??ft ??in/??? lbs",
                    "stage": "???",
                    "origin": "???",
                    "form": "???",
                    "eggType": "???/???",
                    "species": "The ??? Pokemon",
                },
                hiddenInfo: {
                    "type1": "Electric",
                    "type2": "None",
                    "abilities": "Static/Lightning Rod",
                    "evoMethod": "Thunder Stone",
                    "hw": "1ft 4in/13.2 lbs",
                    "stage": "2",
                    "origin": "Kanto",
                    "form": "Normal",
                    "eggType": "Field/Fairy",
                    "species": "Mouse Pokemon",
                    // add cry
                    // add pokedex description
                }

            }
        },
        methods: {
            reveal(value){
                // Fetch the data for the correct pokemon for the day
                // emit the score change upon reveal.
                if(this.pokemonInfo[value] == this.hiddenInfo[value]){
                    return;
                }
                this.pokemonInfo[value] = this.hiddenInfo[value];
                //apply the reveal to the score
                return;
            },
            revealRandom(){
                let keys = Object.keys(this.pokemonInfo);
                this.reveal(keys[Math.floor(keys.length * Math.random())]);
                return;
            }
        },
        mounted(){
            this.revealRandom();
        }
    }
</script>

<style scoped>
    .container {
        color: lightgray;
        background-image: url('./../assets/pokedex.png');
        background-size: cover;
        height: 1000px;
        width: 1000px;
        margin: auto;
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
        position: static;
        border-top: 40px solid transparent;
        border-left: 100px solid transparent;
        border-right: solid transparent;
        border-bottom: solid transparent;
        font-size: 18px;
        font-family: "Courier New", monospace;
        border-collapse: collapse;
    }
    .mystery {
        border-top: 200px solid transparent;
    }

</style>

