<script setup>
  import PopupBox from './PopupBox.vue';
  import {useCookies} from 'vue3-cookies';
</script>
<template>
  <div>
    <!--Sign in window-->
    <PopupBox v-if="isSignIn" @close="close()">
      
      <h1 style="text-align: center; font-family: 'Arial';">Log in</h1>

      <p style="text-align: center; font-family: 'Arial';">Email: </p>
      <input v-model="logIn.email" type="text" class="horizontal-center"/>
      <br/>
      <p style="text-align: center; font-family: 'Arial';">Password: </p>
      <input v-model='logIn.password' type="password" class="horizontal-center"/>
      <br/>
      <br/>

      <div class="horizontal-center">
        <button @click="login()" type="submit">Login</button>
      </div>
      <br/>

      <p style="text-align:center; font-family: 'Arial';">No account? <button type="submit" @click="toggleAccountCreation()">Sign Up</button></p>
    </PopupBox>


    <!--Sign up window-->
    <PopupBox v-if="!isSignIn" @close="close()">
      
      <h1 style="text-align: center; font-family: 'Arial';">Sign Up</h1>

      <p style="text-align: center; font-family: 'Arial';">Email: </p>
      <input v-model='signUp.email' type="text" class="horizontal-center"/>
      <br/>
      <p style="text-align: center; font-family: 'Arial';">Username: </p>
      <input v-model='signUp.username' type="text" class="horizontal-center"/>
      <br/>
      <p style="text-align: center; font-family: 'Arial';">Password: </p>
      <input v-model='signUp.password' type="password" class="horizontal-center"/>
      <br/>
      <br/>

      <div class="horizontal-center">
        <button @click="signup()" type="submit">Sign Up</button>
      </div>
      <br/>

      <p style="text-align:center; font-family: 'Arial';">Have an account? <button type="link" @click="toggleAccountCreation()">Sign In</button></p>
    </PopupBox>
  </div>
</template>

<script>
import account from "../../services/account.js";

export default {
    data(){
        return {
            isSignIn: true,
            signUp: {
                email: '',
                username: '',
                password: ''
            },
            logIn: {
                email: '',
                password: ''
            }
        }
    },
    methods: {
        async login(){
            //check if the login is valid
            const { cookies } = useCookies();
            const res = await account.login(this.logIn.email,this.logIn.password);
            console.log(res);
            if(res.data.res == "Passed") {
                cookies.set("email", this.logIn.email);
                cookies.set("username",res.data.username);
                this.close();
                //Refresh the page
                location.reload();
            }
            //this.close();
        },
        async signup(){
            //check if the sign up is valid
            const { cookies } = useCookies();
            const res = await account.signup(this.signUp.email,this.signUp.username,this.signUp.password);
            console.log(res);
            if(res.data.res == 'Passed'){
                cookies.set("email",this.signUp.email);
                cookies.set("username",this.signUp.username);
                this.close();
                //Refresh the page
                location.reload();
            }
            //this.close();
        },
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
