function generateWord() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var result = xhr.responseText;
       
            document.getElementById("termOutput").innerHTML = result;
        }
    };
    xhr.open("GET", "/generateWord", true);
    xhr.send(null);
}

function submitTerms() {
    var termOne = document.getElementById("termInputOne").value
    var termTwo = document.getElementById("termInputTwo").value

    var data = new FormData();
    data.append("termOne", termOne);
    data.append("termTwo", termTwo);

    var xhr = new XMLHttpRequest();
    
    xhr.open("POST", "/submitTerms", true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var result = xhr.responseText;
            console.log(result);
            var gameData = JSON.parse(result);
            document.getElementById("playerOneTotalScore").innerHTML = gameData.playerOne.totalScore;
            document.getElementById("playerTwoTotalScore").innerHTML = gameData.playerTwo.totalScore;
            document.getElementById("playerOneCurrentScore").innerHTML = gameData.playerOne.currentScore;
            document.getElementById("playerTwoCurrentScore").innerHTML = gameData.playerTwo.currentScore;
            document.getElementById("termOutput").innerHTML = gameData.term;
            document.getElementById("turn").innerHTML = gameData.turn;
        }
    };
    
    xhr.send(data);
}

function startGame() {
    var nameOne = document.getElementById("nameOne").value
    var nameTwo = document.getElementById("nameTwo").value

    var data = new FormData();
    data.append("nameOne", nameOne);
    data.append("nameTwo", nameTwo);

    var xhr = new XMLHttpRequest();
    
    xhr.open("POST", "/startGame", true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var result = xhr.responseText;
            console.log(result);
            window.location.href = "/gameView";
        }
    };
    
    xhr.send(data);
}