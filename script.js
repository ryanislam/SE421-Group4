const firstname = document.getElementById('firstname')
const lastname = document.getElementById('lastname')
const email = document.getElementById('email')
const password = document.getElementById('psw')
const password = document.getElementById('psw-repeat')
const form = document.getElementById('genderform')
const select = document.getElementById('titleselect')

form.addEventListener('submit', (e) => {
    let messages = []
    if (name.value === '' || name.value == null) {
        messages.push('Name is required')
    }

    if (password.value.length <=6) {
        messages.push('Password must be longer than 6 characters')
    }

    if (password.value.length >=20) {
        messages.push("Password must be less than 20 characters")
    }

    if (password.value === 'password') {
        messagesd.push('Password cannot be password.')
    }

    if (messages.length > 0) {
        e.preventDefault()
        errorElement.innetText = messages.join(', ')
    }
})