import requests from './requests'

export default {
    get_leaderboard (category) {
        return requests().post(`/get_leaderboard/${category}`);
    },
    get_limited_leaderboard (category, limit) {
        return requests().post(`/get_leaderboard/${category}/${limit}`);
    },
    set_leaderboard (username, score) {
        return requests().post(`/set_leaderboard/${username}/${score}`);
    }
}
