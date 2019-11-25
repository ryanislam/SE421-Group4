
var firstname = document.forms['vform']['firstname'];
var lastname = document.forms['vform']['lastname'];
var email = document.forms['vform']['email'];
var password = document.forms['vform']['password'];
var password_comfirm = document.forms['vform']['password_confirm'];

var firstname_error = document.getElementById('firstname_error');
var lastname_error = document.getElementById('lastname_error');
var email_error = document.getElementById('email_error');
var password_error = document.getElementById('password_error');

firstname.addEventListener('blur', firstnameVerify, true);
lastname.addEventListener('blur', lastnameVerify, true);
email.addEventListener('blur', emailVerify, true);
password.addEventListener('blur', passwordVerify, true);

function Validate()
{
    if (firstname.value == "") 
    { 
        firstname.style.border = "1px solid red";
        document.getElementById('firstname_div').style.color = "red";
        firstname_error.textContent = "First name is required";
        firstname.focus();
        return false;
    }
    if (firstname.value.length < 3) 
    {
        firstname.style.border = "1px solid red";
        document.getElementById('firstname_div').style.color = "red";
        firstname_error.textContent = "First name must be at least 3 characters";
        firstname.focus();
        return false;
    }
    if (lastname.value == "") 
    { 
        lastname.style.border = "1px solid red";
        document.getElementById('lastname_div').style.color = "red";
        lastname_error.textContent = "Last name is required";
        lastname.focus();
        return false;
    }
    if (lastname.value.length < 3) 
    {
        lastname.style.border = "1px solid red";
        document.getElementById('lastname_div').style.color = "red";
        lastname_error.textContent = "Last name must be at least 3 characters";
        lastname.focus();
        return false;
    }
    if (email.value == "") 
    {
        email.style.border = "1px solid red";
        document.getElementById('email_div').style.color = "red";
        email_error.textContent = "Email is required";
        email.focus();
         return false;
    }
    if (password.value == "") 
    {
        password.style.border = "1px solid red";
        document.getElementById('password_div').style.color = "red";
        password_confirm.style.border = "1px solid red";
        password_error.textContent = "Password is required";
        password.focus();
        return false;
    }
    if (password.value != password_confirm.value) 
    {
        password.style.border = "1px solid red";
        document.getElementById('password_confirm_div').style.color = "red";
        password_confirm.style.border = "1px solid red";
        password_error.innerHTML = "The two passwords do not match";
        return false;
    }
}
function firstnameVerify() 
{
    if (firstname.value != "") 
    {
        firstname.style.border = "1px solid #5e6e66";
        document.getElementById('firstname_div').style.color = "#5e6e66";
        firstname_error.innerHTML = "";
        return true;
    }
}
function lastnameVarify()
{
    if (lastname.value != "") 
    {
        lastname.style.border = "1px solid #5e6e66";
        document.getElementById('lastname_div').style.color = "#5e6e66";
        lastname_error.innerHTML = "";
        return true;
    }
}
function emailVerify() 
{
    if (email.value != "") 
    {
        email.style.border = "1px solid #5e6e66";
        document.getElementById('email_div').style.color = "#5e6e66";
        email_error.innerHTML = "";
        return true;
    }
}
function passwordVerify() 
{
    if (password.value != "") {
        password.style.border = "1px solid #5e6e66";
        document.getElementById('password_confirm_div').style.color = "#5e6e66";
        document.getElementById('password_div').style.color = "#5e6e66";
        password_error.innerHTML = "";
        return true;
    }
    if (password.value === password_confirm.value) {
        password.style.border = "1px solid #5e6e66";
        document.getElementById('password_confirm_div').style.color = "#5e6e66";
        password_error.innerHTML = "";
        return true;
    }
}