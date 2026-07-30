let speaker = "emily";
let emotion = "neutral";

const speakerCards = document.querySelectorAll(".speaker");

speakerCards.forEach(card => {

    card.addEventListener("click", () => {

        speakerCards.forEach(c => c.classList.remove("selected"));

        card.classList.add("selected");

        speaker = card.dataset.speaker;

    });

});


const emotionButtons = document.querySelectorAll(".emotion");

emotionButtons.forEach(button => {

    button.addEventListener("click", () => {

        emotionButtons.forEach(b => b.classList.remove("selected"));

        button.classList.add("selected");

        emotion = button.dataset.emotion;

    });

});



document.getElementById("generate").addEventListener("click", generateVoice);



async function generateVoice() {

    const text = document.getElementById("text").value.trim();

    if(text === ""){

        alert("Écris une phrase.");

        return;

    }

    const loading = document.getElementById("loading");

    const player = document.getElementById("player");

    loading.style.display = "block";

    player.style.display = "none";


    try{

        const response = await fetch("/api/tts/",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                text:text,

                speaker:speaker,

                emotion:emotion

            })

        });


        const data = await response.json();


        loading.style.display="none";


        if(data.audio_url){

            player.src = data.audio_url + "?t=" + new Date().getTime();

            player.style.display="block";

            player.load();

            player.play();

        }

        else{

            alert(data.error);

        }

    }

    catch(error){

        loading.style.display="none";

        alert("Erreur : " + error);

    }

}