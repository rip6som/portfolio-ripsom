;const greetings = document.querySelectorAll('.h1greeting .greeting-text');
;const name = document.querySelectorAll('.h2greeting .greeting-text');

function showGreeting(index) {
    greetings.forEach(function(element) {
        element.classList.remove('active');
    });
    name.forEach(function(element) {
        element.classList.remove('active');
    });

    greetings[index].classList.add('active');
    name[index].classList.add('active');

}
function randomSwitch() {
    const randomIndex = Math.floor(Math.random() * 3) + 1;

    showGreeting(randomIndex);

    setTimeout(function() {
        showGreeting(0);
    }, 1500);
}
function startAnimation() {
    const randomTime = Math.floor(Math.random() * 4000) + 3000;

    setTimeout(function() {
        randomSwitch();
        startAnimation();
    }, randomTime);
}

startAnimation();