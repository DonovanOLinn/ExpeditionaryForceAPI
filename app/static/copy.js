

function copytxt1() {
    let copyText = document.getElementById("basic-url")
    copyText.select();
    copyText.setSelectionRange(0,99999);
    navigator.clipboard.writeText("https://exfor-api.herokuapp.com/api/" + copyText.value)
}

function copytxt2() {
    let copyText = document.getElementById("Species-filter-url")
    copyText.select();
    copyText.setSelectionRange(0,99999);
    navigator.clipboard.writeText("https://exfor-api.herokuapp.com/api/Species/all/" + copyText.value)
}

function copytxt3() {
    let copyText = document.getElementById("Character-filter-url")
    copyText.select();
    copyText.setSelectionRange(0,99999);
    navigator.clipboard.writeText("https://exfor-api.herokuapp.com/api/character/" + copyText.value)
}

function copytxt4() {
    let copyText = document.getElementById("Ship-filter-url")
    copyText.select();
    copyText.setSelectionRange(0,99999);
    navigator.clipboard.writeText("https://exfor-api.herokuapp.com/api/character/" + copyText.value)
}