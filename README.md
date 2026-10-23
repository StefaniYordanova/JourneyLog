
# JourneyLog

**Plan your journeys. Organize your adventures. Keep every travel detail in one place.**

JourneyLog is a Django web application designed for passionate travelers who love discovering new places and planning their next adventures. Whether you are preparing for an upcoming holiday, organizing a detailed itinerary, or keeping track of important travel reminders, JourneyLog helps you bring every part of your travel planning together in one place.

## Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [How It Works](#-how-it-works)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Author](#-author)

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

## 🛠️ Tech Stack

JourneyLog is built using the following technologies:

- **Python** — application logic and backend development.
- **Django** — web framework, request handling, views, forms, and database interaction.
- **HTML5** — page structure and templates.
- **CSS3** — styling and responsive visual design.
- **Git and GitHub** — version control and source code management.

## ⚙️ Installation

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

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open the following address in your browser: http://127.0.0.1:8000/

## 👩‍💻 Author

**Stefani Yordanova** 

- Software Engineering Student with Python | SoftUni

- GitHub: [@StefaniYordanova](https://github.com/StefaniYordanova)

