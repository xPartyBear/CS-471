<template>
  <div class="modal">
    <div @click="close()" class="bg"></div>

    <!--Sign in window-->
    <div class="window" id="signin">
      
      <h2 style="text-align: center">Sign In</h2>

      <h3 style="text-align: center">Email: </h3>
      <input type="text" class="horizontal-center"/>
      <br/>
      <h3 style="text-align: center">Password: </h3>
      <input type="password" class="horizontal-center"/>
      <br/>
      <br/>

      <div class="horizontal-center">
        <button type="submit">Login</button>
      </div>
      <br/>

      <p style="text-align:right">No account? <button type="submit" @click="toSignUp()">Sign Up</button></p>
    </div>


    <!--Sign up window-->
    <div class="window" id="signup" style="visibility:hidden">
      
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
        <button type="submit">Sign Up</button>
      </div>
      <br/>

      <p style="text-align:right">Have an account? <button type="submit" @click="toSignIn()">Sign In</button></p>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    close() {
      this.$emit('close')
    },
    toSignIn(){
      document.getElementById("signup").style.visibility="hidden";
      document.getElementById("signin").style.visibility="visible";
    },
    toSignUp(){
      document.getElementById("signin").style.visibility="hidden"
      document.getElementById("signup").style.visibility="visible"
    }
  }
}
</script>

<style scoped>
.modal {
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
}
.horizontal-center{
  margin: 0;
  position: absolute;
  left: 50%;
  transform: translate(-50%);
}
.bg {
  background-color: gray;
  opacity: 50%;
  position: fixed;
  width: 100%;
  height: 100%;

  z-index: 2;
}
.window {
  z-index: 2;
  width: 35%;
  height: 45%;
  background-color: lightgray;
  position: absolute;
  display: table;
  left: 30%;
  top: 30%;
  border-radius: 16px;
  box-shadow: 0px 4px 4px 0px gray;
}
.form {
  display: block;
}
</style>
