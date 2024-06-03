<script setup>
import {RouterLink} from 'vue-router';
import SideBar from './SideBar.vue';
import MenuLink from './MenuLink.vue';
import { useCookies } from 'vue3-cookies';
import BannerTextImg from './../assets/banner1.png'
import BannerLogoImg from './../assets/banner2.png'
</script>

<template>
    <div class="header">
        <SideBar imgSrc="../../public/bars.png" :title="'Welcome, '+getName+ '!'">
            <div class="pageLink">
                <MenuLink icon="../../public/search-alt.png"><RouterLink class="link" to="/">Today's Puzzle</RouterLink></MenuLink>
                <MenuLink icon="../../public/calendar-alt.png"><RouterLink class="link" to="/past-puzzles">Past Puzzles</RouterLink></MenuLink>
                <MenuLink icon="../../public/award.png"><RouterLink class="link" to="/leaderboards">Leaderboards</RouterLink></MenuLink>
                <MenuLink icon="../../public/smile.png"  v-if="isSignedIn"><RouterLink class="link" to="/accounts">My Account</RouterLink></MenuLink>
                <menuLink icon="../../public/signin.png" v-if="isSignedIn" @click="logout()">Log Out</menuLink>
                <MenuLink icon="../../public/signin.png" v-if="!isSignedIn" @click="displaySignUp()">
                    <p class="link">Sign Up / Sign In</p>
                </MenuLink>
            </div>
        </SideBar>
        <!--Banner Title-->
        <img :src="BannerLogoImg" style="width: 70px">
        <img :src="BannerTextImg" style="width: 300px; position:absolute; left:45%">
    </div>
</template>

<script>
    export default {
        name: 'NavBar',
        data() {
            return {
                isSignedIn: false
            }
        },  
        methods: {
            logout(){
                //check if the login is valid
                const { cookies } = useCookies();
                cookies.set("email","");
                cookies.set("username","")
                //Refresh the page
                this.$emit('refresh')
            },
            displaySignUp(){
                this.$emit('sign-up');
                console.log('show sign up modal');
            },
            signedin(){
                this.isSignedIn=true
            }
        },
        beforeMount(){
            const { cookies } = useCookies();
            let username_value = cookies.get("username");
            if(username_value != null){
                this.isSignedIn=true;
            }
        },
        computed: {
            getName: () => {
                const { cookies } = useCookies();
                let username_value = cookies.get("username");
                console.log(username_value);
                if(username_value != null){
                    return username_value;
                }
                return ''
            },
        }
    }
</script>

<style scoped>
    .header {
        background-color: white;
        box-shadow: 0px 5px 5px lightgray;
        float: left;
        position: fixed;
        width: 100%;
        margin: 0px;
        height: 64px;
        display: block;
        z-index: 1;
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