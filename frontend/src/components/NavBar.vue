<script setup>
import {RouterLink} from 'vue-router'
import SideBar from './SideBar.vue'
import MenuLink from './MenuLink.vue'
</script>

<template>
    <div>
        <SideBar imgSrc="../../public/favicon.ico" :title="'Welcome, '+name+ '!'">
            <div class="pageLink">
                <MenuLink><RouterLink class="link" to="/">Home</RouterLink></MenuLink>
                <MenuLink><RouterLink class="link" to="/past-puzzles">Past Puzzles</RouterLink></MenuLink>
                <MenuLink><RouterLink class="link" to="/accounts">Accounts</RouterLink></MenuLink>
                <MenuLink @click="displaySignUp()">
                    <p class="link">Sign Up / Sign In</p>
                </MenuLink>
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
                console.log('show sign up modal');
            },
        },
        computed: {
            isSignedIn: () => {

            },
            name: () => {
                return 'John Doe'
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
        text-decoration: none;
        user-select:none;
        color: black;
    }
</style>