var counter = 0;

function upvote() {
  counter++;

  document.getElementById('votes').innerHTML = counter;
}

function downvote() {
  counter--;

  document.getElementById('votes').innerHTML = counter;
}