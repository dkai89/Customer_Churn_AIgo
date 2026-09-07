// Customer Churn Prediction - Frontend API Connection

const form = document.getElementById("predictionForm");

const resultSection = document.getElementById("result");
const predictionText = document.getElementById("predictionText");
const churnProbability = document.getElementById("churnProbability");
const noChurnProbability = document.getElementById("noChurnProbability");

form.addEventListener("submit", async function (event) {

    event.preventDefault();

    const customerData = {

        gender: document.getElementById("gender").value,

        SeniorCitizen: Number(
            document.getElementById("seniorCitizen").value
        ),

        Partner: document.getElementById("partner").value,

        Dependents: document.getElementById("dependents").value,

        tenure: Number(
            document.getElementById("tenure").value
        ),

        PhoneService: document.getElementById("phoneService").value,

        MultipleLines: document.getElementById("multipleLines").value,

        InternetService: document.getElementById("internetService").value,

        OnlineSecurity: document.getElementById("onlineSecurity").value,

        OnlineBackup: document.getElementById("onlineBackup").value,

        DeviceProtection: document.getElementById("deviceProtection").value,

        TechSupport: document.getElementById("techSupport").value,

        StreamingTV: document.getElementById("streamingTV").value,

        StreamingMovies: document.getElementById("streamingMovies").value,

        Contract: document.getElementById("contract").value,

        PaperlessBilling: document.getElementById("paperlessBilling").value,

        PaymentMethod: document.getElementById("paymentMethod").value,

        MonthlyCharges: Number(
            document.getElementById("monthlyCharges").value
        ),

        TotalCharges: document.getElementById("totalCharges").value
            ? Number(document.getElementById("totalCharges").value)
            : null
    };


    console.log("Sending customer data:", customerData);


    try {

        const response = await fetch(
            "/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(customerData)
            }
        );


        if (!response.ok) {

            const errorData = await response.json();

            throw new Error(
                errorData.detail || "Prediction API request failed."
            );
        }


        const result = await response.json();


        console.log("API response:", result);


        predictionText.textContent = result.prediction;

        churnProbability.textContent =
            `${(result.churn_probability * 100).toFixed(2)}%`;

        noChurnProbability.textContent =
            `${(result.no_churn_probability * 100).toFixed(2)}%`;


        resultSection.classList.remove("hidden");

    }


    catch (error) {

        console.error("Prediction error:", error);

        alert(
            "Prediction failed: " + error.message
        );
    }

});