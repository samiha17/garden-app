// Get user input instead of hardcoded values
let season = prompt("Enter the current season (summer/winter):").toLowerCase();
let plantType = prompt("Enter the plant type (flower/vegetable):").toLowerCase();

// Variable to hold gardening advice
let advice = "";

// Objects to store gardening advice
const SEASON_ADVICE = {
    summer: "Water your plants regularly and provide some shade.\n",
    winter: "Protect your plants from frost with covers.\n"
};

const PLANT_ADVICE = {
    flower: "Use fertiliser to encourage blooms.",
    vegetable: "Keep an eye out for pests!"
};

/**
 * Returns gardening advice based on season and plant type
 */
function getGardeningAdvice(season, plantType) {
    let advice = "";
    advice += SEASON_ADVICE[season] || "No advice for this season.\n";
    advice += PLANT_ADVICE[plantType] || "No advice for this type of plant.";
    return advice;
}

// Generate and display advice
console.log(getGardeningAdvice(season, plantType));