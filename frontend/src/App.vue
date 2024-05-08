<script setup>
import ping from '/services/ping.js'
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
import SignUpIn from './components/SignUpIn.vue'
</script>

<template>
  <header>
    <NavBar @sign-up="toggleSignUp()"/>
  </header>
  <br>
  <br>
  <!--
  <button @click="test()">
    Test
  </button>
  <p>Test results: {{output}}</p>
  -->
  <SignUpIn v-if="signUpEnabled" @close="toggleSignUp()"></SignUpIn>
  <main>
   
    <RouterView/>
    <!--
      This is where the sign up box will be

    -->
  </main>
</template>

<script>
  export default {
    name: 'App',
    components: [NavBar],
    data() {
      return {
        output: '',
        signUpEnabled: false,
      }
    },
    methods: {
      async test(){
        //This is an example of communication for the process
        let res = await ping.ping({
          "data": 'test'
        })
        this.output += res.data;
      },
      toggleSignUp(){
        this.signUpEnabled = !this.signUpEnabled;
      }
    }
  }
</script>

<style>
  body {
    margin: 0px;
  }
  main {
    margin: 8px;
  }
</style>
