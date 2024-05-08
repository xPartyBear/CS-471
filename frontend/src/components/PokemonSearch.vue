<script setup>
import PokemonSearchElement from './PokemonSearchElement.vue';
</script>

<template>
    <div class="dropdown-wrapper">
        <div v-if="!isSearching" @click="isSearching=!isSearching" class="selected-item">
            <span class="result"> Selected Pokemon: {{selectedPokemon}} <img class="icon" src="../../public/favicon.ico"> </span>
        </div>
        <div v-if="isSearching" class="dropdown-popover">
            <div class="bg" @click="isSearching=!isSearching"></div>
            <input class="search-bar" v-model="searchedPokemon" type="text" placeholder="Search for a Pokemon...">
            <div class="options">
                <ul class="option" v-for="option in filteredOptions" @click="selectPokemon(option)" >
                    <PokemonSearchElement :pokemonImg="pokeIcon(option)">{{option}}</PokemonSearchElement>
                </ul>
            </div>
        </div>
        <button v-if="!isSearching" @click="guessPokemon" class="check">Check</button>
    </div>
</template>

<script>
    export default {
        name: 'PokemonSearch',
        data(){
            return {
                selectedPokemon: '',
                isSearching: false,
                searchedPokemon: '',
                options: ['a','b','c','d','e','a','alpha','a','a','a','a','a','a','a','a','a']
            }
        },

        setup(){
            // GetAllPokemon the available list
            // Possibly not query for the whole dataset at once, only when it is relevant at once, only at points where we may need it, (i.e search event, scroll event, etc.)
        },
        methods: {
            selectPokemon(option){
                let res =  this.options.filter((pokemonName) => pokemonName.toLowerCase() == option.toLowerCase());
                if(res.length <= 0){
                    this.isSearching=false;
                    return;
                }
                this.selectedPokemon = res[0];
                this.searchedPokemon = '';
                this.isSearching = false;
            },
            guessPokemon(){
                if(this.selectedPokemon == ''){
                    console.log('Invalid Pokemon Name');
                    return;
                }
                this.$emit('guess',this.selectedPokemon);
            },
            pokeIcon(name) {
                // This is where we will need to get the image of the pokemon fetched (Backend Protocol)
                return '';
            }
        },
        computed : {
            filteredOptions(name) {
                let res = this.options.filter((pokemonName) => pokemonName.toLowerCase().includes(this.searchedPokemon.toLowerCase()));
                if(res.length <= 0){
                    return ['No Pokemon Found']
                }
                return res;
            },
        }
    }
</script>

<style scoped>
    .icon{
        width: 32px;
        height: 32px;
        padding-left: 50%;
    }
    .dropdown-wrapper {
        max-width: 350px;
        position:relative;
        margin: auto;

        .selected-item {
            position: relative;
            height:25px;
            padding: 4px 0px;
            width: 100%-1px;
            user-select: none;

            background-color: white;
            border: .5px solid black;
            border-radius: 2px;
            margin: 0;
            .result {
                position: relative;
                display: flex;

            
            }
            
        }
        .selected-item:hover{
            background-color: lightgray;
        }
        .dropdown-popover {
            width: 100%;
            user-select: none;
        }
        .option {
            background-color: white;
            width: 100%;
            margin:0;
            padding: 0;
            position: relative;
            list-style-type: none;
            border: 1px 2px solid black;
            display: block;
            height: 32px;
            padding: 1px;
        }
        .option:hover {
            background-color: lightgray;
            transition: background-color 0.1s ease;  
            cursor: pointer;
        }
        .options {
            position:fixed;
            width:100%;
            max-width:350px;
            max-height: 200px;
            overflow-y:scroll;
            background-color: gray;
            border: 1px solid black;
            border-radius: 2px;
            -ms-overflow-style: none;
            scrollbar-width: none;
            z-index: 2;
        }
        .options::-webkit-scrollbar {
            display: none;
        }
        .check {
            position: absolute;
            width:100%;
            height:32px;
            color:white;
            background-color: blue;
            border: 2px solid blue;
            user-select: none;
            border-radius: 2px;
        }
        .check:hover {
            cursor: pointer;
            background-color: white;
            color: blue;
            border: 2px inset blue;
            transition: all .3s ease;
        }
    }
    input[type=text]{
        border: none;
        border-radius: 2px;
        background-image: url('searchicon.png');
    }
    input[type=text]:focus{
        border: none;
        background-color: lightblue;
    }
    .search-bar {
        position: relative;
        width: 100%;
        padding: 4px 0px;
        height:25px;   
    }
    
    .bg {
        display: block;
        margin: 0;
        position: fixed;
        width: 100%;
        height: 100%;
        background-color: gray;
        opacity: 10%;
        left: 0;
        top: 0;
    }

</style>