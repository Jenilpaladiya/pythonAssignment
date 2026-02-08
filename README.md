# Weather Dashboard – Phase 3

A responsive web application that shows **current weather** and a **5-day forecast** for any city using the OpenWeatherMap API.  
The app is designed as a university project and focuses on **clean UI, responsive layout, and simple testable features**.

---

## Features

### 1. City Search
- Search for any city by name using the search bar.
- Press **Enter** or click the **Search** button to fetch data.
- If the city is valid, current weather and the 5-day forecast are displayed.

### 2. Current Weather Card
For the selected city, the app shows:

- City name  
- Current date & time (from the user’s browser)  
- Temperature (°C)  
- Humidity (%)  
- Wind speed (km/h)  
- Weather icon (from OpenWeatherMap)  

A **default weather icon** is shown when the page first loads, and it is replaced by the real icon after the first successful API call.

### 3. 5-Day Forecast
- Forecast data is loaded from the `forecast.php` endpoint.
- One card per day (5 cards total).
- Each card includes:
  - Day name (e.g., Fri, Sat, Sun)
  - Weather icon
  - Temperature (°C)
  - Short description (e.g. *Clouds*, *Rain*, *Clear*).

### 4. Favourite Cities
- Three default favourite cities: **London**, **New York**, **Tokyo**.
- After searching a city, you can click **“+ Add current city”** to save it as a favourite.
- Favourites are rendered as buttons for quick access.
- Each favourite has a small **`×` (cancel)** button to remove it.
- Favourites are persisted using **`localStorage`** so they remain after a page refresh.

### 5. Error Handling
- If the user searches for an invalid city, the app:
  - Shows a clear error message (e.g. *“City not found. Please try again.”*).
  - Does not crash or break the layout.
- Basic network error handling is included in the JavaScript `.catch(...)` blocks for both current weather and forecast.

### 6. Responsive Design
- Layout is built with **Bootstrap** and custom CSS.
- On **desktop**, forecast cards are shown in a row; on **mobile**, they stack vertically.
- The main weather card, search bar, and favourites section all scale to different screen sizes.
- Tested with Chrome DevTools device modes (e.g. iPhone, iPad, desktop).

---

## Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript (vanilla), Bootstrap  
- **Backend / API proxy:** PHP (`weather.php`, `forecast.php`)  
- **Weather data:** [OpenWeatherMap](https://openweathermap.org/) (Current Weather + 5-Day / 3-Hour Forecast API)  
- **Storage:** Browser `localStorage` for favourite cities  
- **Tools:** VS Code, Chrome DevTools

---

## Project Structure

```text
.
├── index.html         # Main UI (search, weather card, forecast, favourites)
├── weather.php        # PHP endpoint for current weather
├── forecast.php       # PHP endpoint for 5-day forecast
└── README.md


Installation & Setup
0. Check PHP Installation

Open a terminal in macOS and run:

php -v


If you see a PHP version (e.g. PHP 8.x.x) → PHP is installed ✅

If you see command not found: php → install PHP (for example with Homebrew):

brew install php


Then confirm again with php -v.

1. Clone or Download the Project
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>


Or download as ZIP and extract to a folder.

2. Configure Your OpenWeatherMap API Key

Open weather.php and forecast.php and set your API key:

$apiKey = 'YOUR_API_KEY_HERE';


Replace 'YOUR_API_KEY_HERE' with your real OpenWeatherMap API key:

$apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';


⚠️ For public repositories this key is visible. For a student project this is usually acceptable, but be aware of the risk.

3. How to Run the PHP Project (Built-in Server)

From the project folder in the terminal:

php -S localhost:8000


You should see something like:

PHP Development Server started
Listening on http://localhost:8000
Document root is /path/to/your/project


🔴 Important: Keep this terminal window open while you are using the app.
To stop the server later, press CTRL + C.

4. Open the App in Your Browser

Now open a browser (Chrome recommended) and go to:

http://localhost:8000/index.html


✅ Do not open the file as file:///Users/.../index.html –
the JavaScript requests to weather.php and forecast.php only work via http://localhost:8000.

5. Test the PHP Endpoints Directly (Optional)

You can also check the PHP endpoints in the browser:

Current weather:

http://localhost:8000/weather.php?city=Berlin


5-day forecast:

http://localhost:8000/forecast.php?city=Berlin


If everything is correct, you should see JSON output (a big { ... } object), not an error page.

How to Use the App

Search a city

Type a city name (e.g., Berlin) in the input box.

Click Search.

Current weather and 5-day forecast appear.

Add to favourites

After a successful search, click “+ Add current city”.

A new favourite button appears in the favourites list and is stored in localStorage.

Open a favourite

Click any favourite city button (e.g., London).

The dashboard reloads weather & forecast for that city.

Remove a favourite

Click the small × icon on a favourite button.

The city is removed from the list and from localStorage.

Example Test Cases
#	Scenario	Steps	Expected Result
1	Search valid city	Type Berlin → click Search	Current weather and 5-day forecast for Berlin are displayed.
2	Search invalid city	Type asdasd → click Search	Error message like “City not found. Please try again.” is shown.
3	Empty input	Leave input empty → click Search	Message/alert asking user to enter a city name.
4	Add city to favourites	Search Tokyo → click + Add current city	Tokyo button appears in favourites; city stored in localStorage.
5	Prevent duplicate favourite	Add Tokyo again using + Add current city	No duplicate Tokyo button is created (duplicates are rejected).
6	Remove favourite	Click × on the Tokyo favourite button	Tokyo button disappears; removed from localStorage.
7	Persistence after refresh	Add a favourite → refresh browser	Favourite cities are restored from localStorage.
8	Responsive mobile view	Open DevTools → choose mobile device → reload	Layout adapts to small screen; cards stack vertically and are readable.
Screenshots (Add yours here)

Create a folder screenshots/ in the repo and save images there.
Then update the paths below.

1. Desktop View (Normal State)
![Desktop view – search + forecast](screenshots/desktop-view.png)


Example: similar to the screenshot you sent where the app is running on http://localhost:8000 and shows the Weather Dashboard header, search bar, empty weather card, and default favourites (London, New York, Tokyo).

2. Mobile View (Responsive)
![Mobile view – responsive layout](screenshots/mobile-view.png)


Example: open DevTools → device toolbar (e.g., iPhone 12) and take a screenshot showing the app stacked vertically.

3. Forecast Section (5-Day Forecast Visible)
![Forecast section – 5-day cards](screenshots/forecast-section.png)


Example: after searching “Berlin” or “Tokyo”, scroll so the 5-day forecast cards are clearly visible.

4. Error Case (Invalid City / Empty Input)
![Error state – invalid city](screenshots/error-invalid-city.png)


Example: type a nonsense city (e.g., asdqwe) and click Search so the error message (“City not found…” or similar) is visible. Take a screenshot of that state and save it as screenshots/error-invalid-city.png.
