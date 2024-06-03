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
    },
    get_date(params){
        const fullDate = new Date();
        let day = fullDate.getDate();
        let month = fullDate.getMonth() + 1;
        let year = fullDate.getFullYear();
        if(params.month != null && params.day != null && params.year != null) {
            this.pastPuzzleBeingPlayed = true;
            return `${params.month}-${params.day}-${params.year}`;
        }
        this.pastPuzzleBeingPlayed = false;
        return `${month}-${day}-${year}`;
    }
} 
