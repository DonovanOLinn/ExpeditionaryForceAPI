

function copytxt1() {
    let copyText = document.getElementById("basic-url")
    copyText.select();
    copyText.setSelectionRange(0,99999);
    navigator.clipboard.writeText("http://127.0.0.1:5000/api/" + copyText.value)
}

function copytxt2() {
    let copyText = document.getElementById("Species-filter-url")
    copyText.select();
    copyText.setSelectionRange(0,99999);
    navigator.clipboard.writeText("http://127.0.0.1:5000/api/Species/all/" + copyText.value)
}

function copytxt3() {
    let copyText = document.getElementById("Character-filter-url")
    copyText.select();
    copyText.setSelectionRange(0,99999);
    navigator.clipboard.writeText("http://127.0.0.1:5000/api/character/" + copyText.value)
}