const url = process.env.URL

const connection = (endpoint, data, method='GET', headers={}, body={}) => {

    const axios = require('axios');

    if (method==='GET'){
        const config = {
            method: method,
            url: url + endpoint
        }

        const response = axios(config)
            .then(function (response) {
                console.log(JSON.stringify(response.data));
            })
            .catch(function (error) {
                console.log(error);
        })

        return response

    }else{
        const config = {
            method: method,
            url: url + endpoint,
            headers: headers,
            body: body,
        };
        const response = axios(config)
            .then(function (response) {
                console.log(JSON.stringify(response.data));
            })
            .catch(function (error) {
                console.log(error);
        })
    }
}

