You are a technical documentation writer.

Create a complete, well-structured GitHub README.md (Markdown) for my university project:

Project Name: Weather Dashboard – Phase 3

Project Summary:
A responsive web application that shows current weather and a 5-day forecast for any city using the OpenWeatherMap API. The focus is clean UI, responsive layout, and simple testable features.

IMPORTANT OUTPUT RULES:
- Output ONLY one single README.md content in Markdown.
- Use proper headings, bullet points, code blocks, tables, and emojis where helpful (not excessive).
- The README must be directly copy-pasteable into GitHub.
- Include “How to Run (PHP Built-in Server)” clearly.
- Include a screenshots section with working Markdown image placeholders.
- Include an example test cases table.
- Mention localStorage favourites behavior clearly.
- Use clear, simple English suitable for university submission.

CONTENT TO INCLUDE (use these details exactly):

FEATURES
1) City Search
- Search any city by name
- Enter key or Search button triggers fetch
- Shows current weather + 5-day forecast on success

2) Current Weather Card
- City name
- Current date & time (from user’s browser)
- Temperature (°C)
- Humidity (%)
- Wind speed (km/h)
- Weather icon (OpenWeatherMap)
- Default weather icon shown initially until first successful API call

3) 5-Day Forecast
- Loaded from forecast.php endpoint
- 5 cards total, one per day
- Day name, icon, temperature (°C), short description (Clouds/Rain/Clear)

4) Favourite Cities
- Default: London, New York, Tokyo
- After searching, user can click “+ Add current city” to save favourite
- Favourites displayed as quick buttons
- Each favourite has × button to remove
- Persist favourites using localStorage

5) Error Handling
- Invalid city → show message “City not found. Please try again.”
- Does not crash/break layout
- Network error handling in JS catch blocks for current weather and forecast

6) Responsive Design
- Bootstrap + custom CSS
- Desktop: forecast cards in row; Mobile: stacked vertically
- Tested with Chrome DevTools (iPhone/iPad/Desktop)

TECH STACK
- Frontend: HTML5, CSS3, JavaScript (Vanilla), Bootstrap
- Backend/API proxy: PHP (weather.php, forecast.php)
- API: OpenWeatherMap (Current Weather + 5-Day / 3-Hour Forecast)
- Storage: localStorage
- Tools: VS Code, Chrome DevTools

PROJECT STRUCTURE
.
├── index.html
├── weather.php
├── forecast.php
├── screenshots/ (optional)
└── README.md

INSTALLATION & SETUP
0) Check PHP Installation (macOS)
- php -v
- If not installed: brew install php

1) Clone or Download
- git clone ...
- OR download ZIP

2) API Key Setup
- Add API key in weather.php and forecast.php:
  $apiKey = 'YOUR_API_KEY_HERE';
- Mention security note about public repo exposure

HOW TO RUN (PHP BUILT-IN SERVER)
- From project folder: php -S localhost:8000
- Keep terminal open; CTRL+C to stop
- Open: http://localhost:8000/index.html
- Do not open file:///... because PHP endpoints require http://localhost

OPTIONAL ENDPOINT TESTING
- http://localhost:8000/weather.php?city=Berlin
- http://localhost:8000/forecast.php?city=Berlin
- Expect JSON output

HOW TO USE
- Search city
- Add favourite
- Open favourite
- Remove favourite

TEST CASES TABLE (8 rows)
Include scenarios: valid city, invalid city, empty input, add favourite, prevent duplicate, remove favourite, persistence after refresh, responsive mobile view.

SCREENSHOTS SECTION
- Add a section “Screenshots”
- Include 4 placeholder images using Markdown, and assume images are in /screenshots folder:
  1) desktop-view.png
  2) mobile-view.png
  3) forecast-section.png
  4) error-invalid-city.png
- Include 1–2 short lines explaining how to capture screenshots in Chrome DevTools

TROUBLESHOOTING
- API errors: check API key, check server running, open via localhost
- Favourites not saving: check storage blocked, avoid private mode

CREDITS
- OpenWeatherMap
- Bootstrap

LICENSE
- Educational/University project

Finally: Make the README clean, professional, and complete.
