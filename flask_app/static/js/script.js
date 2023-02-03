
// Adding and removing shake animation
function addShake(element){
    element.classList.add("animate__animated");
    element.classList.add("animate__tada");
    element.classList.add("animate__infinite");
    element.classList.add("infinite");
}

function removeShake(element){
    element.classList.remove("animate__animated");
    element.classList.remove("animate__tada");
    element.classList.remove("animate__infinite");
    element.classList.remove("infinite");

}

// Adding and Removing the words for the main RPS header
function addRock(element){
    element.innerHTML = "Rock"
}
function addPaper(element){
    element.innerHTML = "Paper"
}
function addScissors(element){
    element.innerHTML = "Scissors"
}
function removeRock(element){
    element.innerHTML = "R"
}
function removePaper(element){
    element.innerHTML = "P"
}
function removeScissors(element){
    element.innerHTML = "S"
}

function winnerShake(){
    user_chocie = document.querySelector('#user_choice_hand');
    comp_choice = document.querySelector('#computer_choice_hand');
    
    if(winId==1){
        user_chocie.classList.add("animate__animated","animate__shakeY","animate__repeat-1");
    }else if(winId==0){
        comp_choice.classList.add("animate__animated","animate__shakeY","animate__repeat-1")
    }
}