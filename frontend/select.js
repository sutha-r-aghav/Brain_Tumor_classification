const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");

imageInput.addEventListener("change", function () {

    const file = this.files[0];

    if(file){

        preview.src = URL.createObjectURL(file);

        preview.style.display = "block";
    }

});

async function predict() {

    const file = imageInput.files[0];

    if (!file) {
        alert("Please upload an MRI image.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    document.getElementById("result").innerHTML = "Predicting...";

    try {

        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        document.getElementById("result").innerHTML = `
            <h2>${data.prediction}</h2>
            <p><strong>Confidence:</strong> ${data.confidence}%</p>
        `;

    } catch (error) {

        document.getElementById("result").innerHTML =
            "Error connecting to the server.";

        console.error(error);
    }
}
