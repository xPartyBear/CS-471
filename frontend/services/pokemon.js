import requests from './requests'

export default {
    filter_mons(filter) {
        return requests().post('/filter_mons', {filter});
    },
    get_poke_info(date,info) {
        return requests().post('/get_info',{date,info});
    },
    guess_pokemon(date,guessName) {
        return requests().post('/guess_pokemon',{date,guessName});
    },
    get_pokemon(date){
        return requests().post('/get-pokemon',{date})
    }
} 
