class APICall{

    constructor(requestMethod, url, data){
        this.requestMethod = requestMethod;
        this.url = url;
        this.data = data;
        this.result = [];
    }

    post(){
        fetch(this.url, {
            method: this.requestMethod,
            headers: {
                'content-type': 'application/json',
            },
            body: JSON.stringify(this.data)
        })
        .then(res => res.json())
        .then(data => {
            this.result.push(data)
        }); 
        return this.result;
    }
}


function submitForm(){
    // get user login credentials.
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var requestMethod = "POST";
    var url = "http://localhost:8000/auth/api/v1/account/sign-in/";
    var data = {
        "email": email,
        "password": password
    };

    var loadCall = new APICall(requestMethod, url, data);
    console.log(loadCall.post());
}


var signInBtn = document.getElementById("sign-in");
signInBtn.addEventListener("click", function(){
    submitForm();
});
