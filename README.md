# Weather Dashboard – Phase 3 🌦️

A responsive web application that shows **current weather** and a **5-day forecast** for any city using the **OpenWeatherMap API**.  
This university project focuses on **clean UI**, **responsive layout**, and **simple, testable features**.

---

## ✨ Features

### 1) City Search
- Search any city by name
- **Enter key** or **Search button** triggers fetch
- Shows **current weather + 5-day forecast** on success

### 2) Current Weather Card
Displays:
- City name
- Current date & time (from the user’s browser)
- Temperature (°C)
- Humidity (%)
- Wind speed (km/h)
- Weather icon (OpenWeatherMap)

✅ A **default weather icon** is shown initially and is replaced after the first successful API call.

### 3) 5-Day Forecast
- Loaded from `forecast.php` endpoint
- **5 cards total**, one per day
- Each day shows: day name, icon, temperature (°C), short description (Clouds/Rain/Clear)

### 4) Favourite Cities
- Default: **London**, **New York**, **Tokyo**
- After searching, click **“+ Add current city”** to save favourite
- Favourites displayed as quick buttons
- Each favourite has **×** button to remove
- Persist favourites using **localStorage** (they remain after refresh)

### 5) Error Handling
- Invalid city → show message: **“City not found. Please try again.”**
- Does not crash/break layout
- Network error handling in JS `.catch(...)` blocks for current weather and forecast

### 6) Responsive Design
- **Bootstrap + custom CSS**
- Desktop: forecast cards in a row
- Mobile: forecast cards stacked vertically
- Tested with Chrome DevTools (iPhone/iPad/Desktop)

---

## 🧰 Tech Stack
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla), Bootstrap
- **Backend / API proxy:** PHP (`weather.php`, `forecast.php`)
- **API:** OpenWeatherMap (Current Weather + 5-Day / 3-Hour Forecast)
- **Storage:** `localStorage`
- **Tools:** VS Code, Chrome DevTools

---

## 📁 Project Structure

On GitHub it will show as a nice terminal-style block.

## 2) Add multiple commands
```markdown
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
php -S localhost:8000


```text
.
├── index.html
├── weather.php
├── forecast.php
├── screenshots/ (optional)
└── README.md


