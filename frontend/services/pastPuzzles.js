import requests from './requests'

export default {
    get_PastPuzzles () {
        return requests().post('/get_puzzles');
    },
}
