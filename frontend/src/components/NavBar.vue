<script setup>
import {RouterLink} from 'vue-router'
import SideBar from './SideBar.vue'
import MenuLink from './MenuLink.vue'
</script>

<template>
    <div class="header">
        <SideBar imgSrc="../../public/favicon.ico" :title="'Welcome, '+getName+ '!'">
            <div class="pageLink">
                <MenuLink icon="../../public/favicon.ico"><RouterLink class="link" to="/">Today's Puzzle</RouterLink></MenuLink>
                <MenuLink icon="../../public/favicon.ico"><RouterLink class="link" to="/past-puzzles">Past Puzzles</RouterLink></MenuLink>
                <MenuLink icon="../../public/favicon.ico"><RouterLink class="link" to="/accounts">Accounts</RouterLink></MenuLink>
                <MenuLink icon="../../public/favicon.ico" @click="displaySignUp()">
                    <p class="link">Sign Up / Sign In</p>
                </MenuLink>
            </div>
        </SideBar>
        <div class="title">Daily Pokedex</div>
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
            getName: () => {
                return 'John Doe'
            },
        }
    }
</script>

<style scoped>
    .header {
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
        margin: 0;
        height: 100%;
    }
    .title {
        text-align: center;
        left: 50%;
        font-size: 32px;
    }


</style>