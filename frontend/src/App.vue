<script setup>
import ping from '/services/ping.js'
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import NavBar from './components/NavBar.vue'
</script>

<template>
  <header>
    <NavBar @sign-up=""/>
  </header>
  <br>
  <br>
  <!--
  <button @click="test()">
    Test
  </button>
  <p>Test results: {{output}}</p>
  -->
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
        signUpEnabled: false;
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
      openSignUp(){

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
