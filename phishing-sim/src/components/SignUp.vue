<template>
    <img class="logo" src="../assets/logo.png">
    <h1>Sign up or something</h1>
    <div class="register">
        <input type="text" v-model="name" placeholder="Enter Name"/>
        <input type="text" v-model="email" placeholder="Enter Email"/>
        <input type="password" v-model="password" placeholder="Enter Password"/>
        <button v-on:click="signUp">Sign up</button>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'SignUp',
    data() {
        return {
            name: '',
            email: '',
            password: ''
        }
    },
    methods: {
        signUp() { 
            let result = axios.post("http://localhost:3000/users", {
                email: this.email,
                password: this.password,
                name: this.name
            });
            console.log(result)
        }
    }
}


</script>

<style>
.logo {
    width:100px
}

.register input {
    width:300px;
    height: 40px;
    padding-left: 20px;
    display: block;
    margin-bottom: 30px;
    margin-left: auto;
    margin-right: auto;
    border: 1px solid lightcoral
}

.register button {
    width: 331px;
    height: 40px;
    border: 1px solid lightcoral;
    background: lightcoral;
    color: white;
    cursor: pointer;
}
</style>