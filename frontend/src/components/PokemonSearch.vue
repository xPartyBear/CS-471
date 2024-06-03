<script setup>
import PokemonSearchElement from './PokemonSearchElement.vue';
import pokemon from '../../services/pokemon.js'
</script>

<template>
    <div class="dropdown-wrapper">
        <div :disabled="!guessEnabled" v-if="!isSearching" @click="isSearching=!isSearching" class="selected-item">
            <span class="result"> Selected Pokemon: {{selectedPokemon.name}} </span><img v-if="isImageValid()" class="icon" :src="selectedPokemon.imgSrc[0].default">
        </div>
        <div v-if="isSearching" class="dropdown-popover">
            <div class="bg" @click="isSearching=!isSearching"></div>
            <input class="search-bar" v-model="searchedPokemon" type="text" placeholder="Search for a Pokemon..." >
            <div class="options">
                <ul class="option" v-for="option in options" @click="selectPokemon(option)" >
                    <PokemonSearchElement :pokemonImg="option.imgSrc[0].default">{{option.name}}</PokemonSearchElement>
                </ul>
                <p v-if="isRequesting">Searching</p>
            </div>
        </div>
        <button :disabled="!guessEnabled" v-if="!isSearching" @click="guessPokemon" class="check">Check</button>
    </div>
</template>

<script>
    export default {
        name: 'PokemonSearch',
        props: {
            guessEnabled: Boolean,
        },
        data(){
            return {
                selectedPokemon: {
                    name: '',
                    imgSrc: [
                        {default: ''}
                    ]
                },
                isSearching: false,
                isRequesting: false,
                searchedPokemon: '',
                options: [{name: 'Search', imgSrc:[{default:''}]}]
            }
        },

        setup(){
            // GetAllPokemon the available list
            // Possibly not query for the whole dataset at once, only when it is relevant at once, only at points where we may need it, (i.e search event, scroll event, etc.)
        },
        methods: {
            selectPokemon(option){
                let res =  this.options.filter((pokemonName) => pokemonName.name.toLowerCase() == option.name.toLowerCase());
                if(res.length <= 0){
                    this.isSearching=false;
                    return;
                }
                this.selectedPokemon = res[0];
                this.searchedPokemon = res[0].name;
                this.isSearching = false;
            },
            guessPokemon(){
                if(this.selectedPokemon == '' || !this.guessEnabled){
                    console.log('Invalid Pokemon Name');
                    return;
                }
                this.$emit('guess',this.selectedPokemon.name);
            },
            isImageValid (){
                return !this.searchedPokemon == '';
            }
            
        },
        computed : {
        },
        watch: {
            searchedPokemon: async function (name) {
                // let res = this.options.filter((pokemonName) => pokemonName.toLowerCase().includes(this.searchedPokemon.toLowerCase()));
                this.isRequesting = true;
                let res = await pokemon.filter_mons(this.searchedPokemon.toLowerCase());
                //console.log(res.data);
                if(res.data.result.length <= 0 || res.data.result[0] == ''){
                    this.options = [{name: 'Search', imgSrc:[{default:''}]}]
                }
                this.isRequesting = false;
                //console.log(res.data.result);
                this.options = res.data.result;
            },
        }
    }
</script>

<style scoped>
    .icon{
        width: 48px;
        height: 48px;
        right: 0%;
        top: -20%;
        position:absolute;

    }
    .dropdown-wrapper {
        max-width: 350px;
        position:relative;
        margin: auto;

        .selected-item {
            display: flex;
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
            cursor: pointer;
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
            background-color: gray;
            border: 2px solid gray;
            user-select: none;
            border-radius: 2px;
        }
        .check:hover {
            cursor: pointer;
            background-color: lightgray;
            color: lightgray;
            border: 2px inset lightgray;
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
        background-color: lightgray;
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