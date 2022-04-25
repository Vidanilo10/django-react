var axios = require('axios');

var config = {
    method: 'get',
    url: 'http://localhost:8000/API/v1/users/',
    headers: { }
};

axios(config)
.then(function (response) {
    console.log(JSON.stringify(response.data));
})
.catch(function (error) {
    console.log(error);
});
