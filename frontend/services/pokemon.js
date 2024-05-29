import requests from './requests'

export default {
    filter_mons(filter) {
        return requests().post('/filter_mons', {filter});
    }
} 
