import requests from './requests'

export default {
    ping(data) {
        return requests().post('/ping',data);
    }
}