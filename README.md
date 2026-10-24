
# JourneyLog

**Plan your journeys. Organize your adventures. Keep every travel detail in one place.**

JourneyLog is a Django web application designed for passionate travelers who love discovering new places and planning their next adventures. Whether you are preparing for an upcoming holiday, organizing a detailed itinerary, or keeping track of important travel reminders, JourneyLog helps you bring every part of your travel planning together in one place.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Author](#author)

## Overview

**JourneyLog brings all these travel essentials together in one organized space.**

The idea behind the project is simple: create a convenient place where travelers can manage their destinations and plan their trips without scattering important details across different notes and lists.

Whether you are planning a weekend getaway, a city break, or a longer adventure, JourneyLog helps you stay organized throughout your travel-planning process.

## Features

### 📍 Destination Management
- Add and manage destinations you dream of visiting.
- Store essential destination information, including names, countries, descriptions, and images.
- Browse your saved destinations.
- Search for destinations by name or country.
- Explore individual destination detail pages.

### 🗓️ Trip Planning
- Create trips associated with specific destinations.
- Organize your travel plans in one place.
- Keep track of trip details and travel dates.
- Browse upcoming and completed trips.
- Search trips by relevant trip and destination information.
- View detailed itineraries for individual trips.

### 🎯 Activity Organization
- Organize activities associated with your travel plans.
- Keep track of planned experiences and things to do during your trip.

### 📝 Travel Notes
- Record useful information and personal reminders related to your journeys.
- Keep important travel details organized and easy to revisit.

### 🎒 Packing Lists
- Prepare packing lists before departure.
- Keep track of the things you need to bring.
- Reduce the chance of forgetting important travel essentials.

### 🔎 Search and Navigation
- Find destinations and trips more easily using search functionality.
- Browse organized lists and individual detail pages.
  
## How It Works

JourneyLog follows a simple, intuitive workflow:

**1. Add a destination**

Start by saving a place you want to explore. Record its essential details and create your own collection of travel destinations.

**2. Create a trip**

Choose a saved destination and create a trip associated with it. Add your travel details and dates to start organizing your journey.

**3. Plan your activities**

Organize the activities and experiences you want to enjoy during your trip.

**4. Write your travel notes**

Keep useful information, ideas, and reminders together with your travel plans.

**5. Prepare your packing list**

Make a list of the things you need to bring so you can prepare for departure with greater confidence.

## Tech Stack

JourneyLog is built using the following technologies:

- **Python** — application logic and backend development.
- **Django** — web framework, request handling, views, forms, and database interaction.
- **HTML5** — page structure and templates.
- **CSS3** — styling and responsive visual design.
- **SQLite** — database for local development
- **Git and GitHub** — version control and source code management.

## Project Structure

JourneyLog is organized into separate Django apps and supporting directories, keeping the application's functionality structured and maintainable.

- **`activities/`** — Manages activities associated with trips.
- **`common/`** — Contains the home page and its related functionality.
- **`destinations/`** — Handles destination management, including creating, browsing, searching, and viewing destination details.
- **`JourneyLog/`** — Contains the main Django project configuration and settings.
- **`packing_items/`** — Manages packing list items associated with trips.
- **`travel_notes/`** — Handles travel notes and reminders related to trips.
- **`trips/`** — Manages trip creation, trip details, and travel planning.
- **`media/`** — Stores uploaded media files, such as destination images.
- **`static/`** — Contains static assets, such as images and CSS for styling.
- **`templates/`** — Contains HTML templates used to render the application's pages.

### Root Files

- **`manage.py`** — Provides the command-line utility for managing the Django project.
- **`requirements.txt`** — Lists the Python packages required to run the application.
- **`.env.example`** — Provides an example of the environment variables needed for configuration.
- **`.gitignore`** — Specifies files and directories Git should ignore.
- **`db.sqlite3`** — The SQLite database used for local development.

## Installation

Follow these steps to set up JourneyLog locally.

### Prerequisites

Make sure you have the following installed:

- Python
- Git
- pip, Python's package installer

### 1. Clone the repository

```bash
git clone https://github.com/StefaniYordanova/JourneyLog.git
```

Navigate into the project directory:

```bash
cd JourneyLog
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows, use:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root by copying `.env.example`:

```bash
cp .env.example .env
```

Open `.env` and configure the required environment variables according to the values and instructions provided in `.env.example`.

**Important:** Keep your `.env` file private and never commit it to GitHub. Use `.env.example` as a template when setting up the project on another machine.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open the following address in your browser: http://127.0.0.1:8000/

## Usage

After starting the development server and opening JourneyLog in your browser, follow these steps to organize your next adventure!

### 1. Explore the Home Page

Once you open the application, you will see the home page, where you can start exploring JourneyLog and access its main features through the navigation bar.

<img width="1300" height="700" alt="home_page" src="https://github.com/user-attachments/assets/0225f922-9fad-4693-8342-aee3156cc643" />

### 2. Add a Destination

Start by adding a destination you would like to visit. Enter the required information about the place and save it to your destinations collection.

<img width="1182" height="635" alt="add_destination" src="https://github.com/user-attachments/assets/ddd4890c-420e-4585-a63c-f4317bbed48a" />

### 3. Create a Trip

After adding a destination, create a trip associated with that destination. Add the relevant trip details to organize your travel plans.

<img width="1174" height="638" alt="add_trip" src="https://github.com/user-attachments/assets/6a6c9eb8-fd45-457e-a0f5-0bb1b7123bd8" />

### 4. Plan Your Activities

Add activities to your trip to keep track of the things you want to do and the places you want to explore during your journey.

<img width="1180" height="506" alt="add_activity" src="https://github.com/user-attachments/assets/b4e9eeb3-f087-4dea-a714-d4c6ce9ef3b4" />

<img width="1300" height="775" alt="add_form_activity" src="https://github.com/user-attachments/assets/cadce7c2-6031-462f-b417-930cf4a9c9bc" />

### 5. Add Travel Notes

Write down important information, useful reminders, and ideas you want to remember before or during your trip.

<img width="1178" height="545" alt="add_note" src="https://github.com/user-attachments/assets/f82a07cc-018e-4d57-82c1-0d9c95ecea2f" />

### 6. Create a Packing List

Navigate to your trip's details page and add packing list items to keep track of everything you need to bring on your journey. There you can also add your travel notes and activities.

<img width="1372" height="798" alt="Screenshot 2026-10-23 at 20 54 27" src="https://github.com/user-attachments/assets/620b3d0a-0751-40c4-842b-bc9e662ade23" />

<img width="1405" height="745" alt="Screenshot 2026-10-23 at 20 55 42" src="https://github.com/user-attachments/assets/831dbd0e-77b8-491f-b962-e4b940fb8e90" />

<img width="1239" height="770" alt="add_item" src="https://github.com/user-attachments/assets/7573b3bc-f875-4233-8127-41bc4b5838e2" />

### 7. Manage Your Travel Plans

Return to your destinations and trips whenever you need to review their details, update your plans, or keep your travel information organized in one place.

<img width="1392" height="791" alt="Screenshot 2026-10-23 at 21 03 20" src="https://github.com/user-attachments/assets/e319d857-c925-45ac-9a78-8b3f06bcda60" />

## Author

**Stefani Yordanova** 

- Software Engineering Student with Python | SoftUni

- GitHub: [@StefaniYordanova](https://github.com/StefaniYordanova)

