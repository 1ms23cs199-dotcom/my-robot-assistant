const apiKey = process.env.WEATHER_API_KEY;
if(!apiKey) {
   console.error("CRITICAL ERROR: No API key found!");
   process.exit(1);
}
console.log("app is running securely.");
