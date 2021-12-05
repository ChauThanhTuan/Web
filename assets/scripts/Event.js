let menuIcon = document.querySelector("#header #nav-menu");
let menu = document.querySelector("#header .menu");
let body = document.querySelector("body");

menuIcon.onclick = function() {
    console.log("Hello");
    menu.style.display = "block";
    body.style.backgroundColor = "#ccc";
}
