document.getElementById('previous').onclick = setPrevious;
document.getElementById('next').onclick = setNext;
document.getElementById('load-file').addEventListener('change', handleFileSelect, false);

let gameNo = document.getElementById('game-no');
let currentMatch = document.getElementById('current-match');
let nextMatch = document.getElementById('next-match');

let obj = {};
let idx = 1;
let objLen = 0;


function handleFileSelect(evt) {
    let file = evt.target.files[0];
    if (file) {
        getAsText(file);
    }     
}

function getAsText(readFile) {
    let reader = new FileReader();
    reader.readAsText(readFile);
    reader.onload = loaded;
}

function loaded(evt) {
    // Obtain the read file data
    let fileString = evt.target.result;
    // make the object obj from the obtained string
    obj = JSON.parse(fileString);
    objLen = Object.keys(obj).length;
    console.log(objLen);
    setInfo()
    //console.log(obj);
}

function setInfo() {
    gameNo.innerHTML = "Hra č. " + String(idx) + " z " + String(objLen);
    currentMatch.innerHTML = "Nyní hraje: " + obj[idx];
    if (idx+1 > objLen) {
        nextMatch.innerHTML = "Následující hra: -";
    } else {
        nextMatch.innerHTML = "Následující hra: " + obj[idx+1];
    }    
}

function setPrevious() {
    if (idx >= 2) {
        idx--;
        setInfo();
    }
    
}

function setNext() {
    console.log('called');
    if (idx < objLen) {
        idx++;
        setInfo();
    }
}


