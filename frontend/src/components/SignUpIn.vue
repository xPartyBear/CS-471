<script setup>
  import PopupBox from './PopupBox.vue';
</script>
<template>
  <div>
    <!--Sign in window-->
    <PopupBox v-if="isSignIn" @close="close()">
      
      <h2 style="text-align: center">Sign In</h2>

      <h3 style="text-align: center">Email: </h3>
      <input type="text" class="horizontal-center"/>
      <br/>
      <h3 style="text-align: center">Password: </h3>
      <input type="password" class="horizontal-center"/>
      <br/>
      <br/>

      <div class="horizontal-center">
        <button @click="close()" type="submit">Login</button>
      </div>
      <br/>

      <p style="text-align:right">No account? <button type="submit" @click="toggleAccountCreation()">Sign Up</button></p>
    </PopupBox>


    <!--Sign up window-->
    <PopupBox v-if="!isSignIn" @close="close()">
      
      <h2 style="text-align: center">Sign Up</h2>

      <h3 style="text-align: center">Email: </h3>
      <input type="text" class="horizontal-center"/>
      <br/>
      <h3 style="text-align: center">Username: </h3>
      <input type="text" class="horizontal-center"/>
      <br/>
      <h3 style="text-align: center">Password: </h3>
      <input type="password" class="horizontal-center"/>
      <br/>
      <br/>

      <div class="horizontal-center">
        <button @click="close()" type="submit">Sign Up</button>
      </div>
      <br/>

      <p style="text-align:right">Have an account? <button type="submit" @click="toggleAccountCreation()">Sign In</button></p>
    </PopupBox>
  </div>
</template>

<script>
export default {
  data(){
    return {
      isSignIn: true
    }
  },
  methods: {
    close() {
      this.$emit('close');
    },
    toggleAccountCreation(){
      this.isSignIn = !this.isSignIn;
    }
  }
}
</script>

<style scoped>
.horizontal-center{
  margin: 0;
  position: absolute;
  left: 50%;
  transform: translate(-50%);
}
.form {
  display: block;
}
</style>
