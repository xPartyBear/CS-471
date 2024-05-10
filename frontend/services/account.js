import requests from './requests'

export default {
    async signup (email,username,password) {
        return await requests().post('/signup',{email,username,password});
    },
    async login (email,password) {
        return await requests().post('/login',{email,password});
    }
}
