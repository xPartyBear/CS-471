import requests from './requests'

export default {
    get_leaderboard (category) {
        return requests().post('/get-leaderboard', {category});
    },
}
