let currentUsername = "";
let cards = document.querySelector(".card")

function getUsername(element) {
    console.log(element.value)
    currentUsername = element.value
}


function coderCard(data) {
    var res = `<div class ="card">
                <img src="${data.avatar_url}" alt="${data.login}">
                <h3>${data.login} - ${data.name}</h3>
                <p>Location: ${data.location}</p>
                <p>Repositories: ${data.public_repos}</p>
                </div>`
    return res
}

async function search() {
    let response = await fetch("https://api.github.com/users/" + currentUsername)
    let data = await response.json();
    console.log(data)
    cards.innerHTML = coderCard(data) + cards.innerHTML
}