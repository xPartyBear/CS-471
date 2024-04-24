<script setup>
import {RouterLink} from 'vue-router'
import SideBar from './SideBar.vue'
</script>

<template>
    <div>
        <SideBar imgSrc="../../public/favicon.ico" title="Hello! Name HERE">
            <div class="pageLink">
                <RouterLink class="link" to="/">Home</RouterLink>
                <RouterLink class="link" to="/past-puzzles">Past Puzzles</RouterLink>
                <RouterLink class="link" to="/accounts">Accounts</RouterLink>
                <button @click="">
                    Sign Up / In
                </button>
            </div>
        </SideBar>
        Daily Pokedex
    </div>
</template>

<script>
    export default {
        name: 'NavBar',
        data() {
            return {

            }
        },  
        methods: {
            displaySignUp(){
                this.$emit('sign-up');
            },
        }
    }
</script>

<style>
    header {
        background-color: gray;
        float: left;
        position: fixed;
        width: 100%;
        margin: 0px;
        height: 64px;
        display: block;
    }
    .pageLink {
        display: block;
    }
    .link {
        display: block; 
    }
</style>