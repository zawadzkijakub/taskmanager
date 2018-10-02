document.addEventListener("DOMContentLoaded", function() {

    var showpassword = document.getElementById('showpassword');
    var password = document.getElementById('password');
    var email = document.getElementById('emailhide');
    var login = document.getElementById('login');

    showpassword.addEventListener('click', function(e) {
        e.preventDefault();
        console.log('click');
        if (password.type === 'password') {
            password.type ='text';
        } else {
            password.type ='password';
        }

    })

    login.addEventListener('keyup', function(e) {
        if (email.id = 'emailhide') {
            email.id = 'email';
        } else {
            email.id = 'email';
        }
    })

    function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
}

    function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

});

