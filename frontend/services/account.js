import requests from './requests'

export default () => {
    signUp (email,username,password) {
        return requests().get('/signup',{data: {email,username,password}});
    }
    signIn (email,password) {
        return requests().get('/login',{data: {email,password}});
    }
}
