# The Nykaa Journey &mdash; Falguni Sanjay Nayar
### *From Investment Banking to Building India's Beauty Empire*

[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![HTML5](https://img.shields.io/badge/HTML-5-orange.svg)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS-3-blue.svg)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-Zero%20(Pure%20CSS)-brightgreen.svg)]()
[![Database](https://img.shields.io/badge/Database-SQLite-lightgrey.svg)](https://www.sqlite.org/)

An educational biography website and enterprise case study dedicated to **Falguni Sanjay Nayar**, Founder and CEO of **Nykaa** (FSN E-Commerce Ventures Ltd). Developed as a second-year **B.Tech Computer Science and Engineering** web development project, this application showcases clean software architecture, semantic HTML5 structure, luxury beauty editorial CSS3 styling, and robust Django backend functionality without any external frontend frameworks or JavaScript.

---

## 1. Project Overview & Objectives

### Project Objectives
1. **Academic Demonstration:** Demonstrate mastery of fundamental web technologies (HTML5, CSS3, Python, and Django) suitable for a second-year college curriculum viva and portfolio showcase on GitHub.
2. **Business Case Study:** Provide an authoritative, chronologically verified educational biography of Falguni Nayar's transition from investment banking at age 49 to pioneering India's leading omnichannel beauty ecosystem.
3. **Pure CSS Responsiveness:** Implement responsive layouts, cards, and mobile menus using modern CSS (Flexbox, CSS Grid, media queries, CSS checkbox toggles) with **zero JavaScript**.
4. **Authentic Visual Presentation:** Features an authentic photograph of Falguni Sanjay Nayar within a luxury editorial frame alongside high-resolution corporate archives.

---

## 2. Technology Stack

- **Backend Framework:** Python 3.11+ &amp; Django 5.x
- **Database:** SQLite3 (Django's built-in, lightweight relational database)
- **Frontend Architecture:**
  - **HTML5:** Semantic elements (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`, `<table>`)
  - **CSS3:** Custom properties (CSS variables), CSS Grid, Flexbox, transitions, hover transformations, responsive media queries
  - **Zero JavaScript:** Navigation menu, animations, and layouts operate entirely with native HTML/CSS and Django template tags
  - **Typography:** Google Fonts (*Playfair Display*, *Plus Jakarta Sans*, *Cormorant Garamond*)
  - **Color Palette:** Soft Blush Pink (`#fef8f8`), Deep Burgundy (`#58111a`, `#2c070c`), Ivory (`#faf8f5`), Charcoal Black (`#1a1a1a`), and Subtle Gold accents (`#d4af37`)

---

## 3. Website Structure & Pages

The application consists of six distinct, richly designed pages and a custom 404 handler:

| Page | URL | Purpose &amp; Contents |
| :--- | :--- | :--- |
| **1. Home** | `/` | Hero section with an authentic photograph of Falguni Nayar, headline *"She Didn't Just Build a Brand. She Built an Empire."*, *"Who is Falguni Nayar"*, verified quick facts table, market vision, Nykaa at a glance, inspirational quote, and navigation CTAs. |
| **2. Success Story** | `/success-story/` | Chronological CSS timeline tracing her upbringing, Sydenham &amp; IIM Ahmedabad education, Kotak Mahindra career, founding of Nykaa, 2021 IPO milestone, and 6 core lessons. |
| **3. Achievements** | `/achievements/` | Verified honors gallery (EY World Entrepreneur of the Year, BSE/NSE IPO, Forbes Asia Power Businesswomen, TIME100 Next) and *"Why Her Journey Matters"*. |
| **4. Personal Life** | `/personal-life/` | Education details, family background (husband Sanjay Nayar, twin children Anchit and Adwaita Nayar), lifestyle, and executive leadership philosophy. |
| **5. About Nykaa** | `/about-nykaa/` | Corporate case study: inventory-led model, omnichannel retail (Nykaa Luxe &amp; On Trend), product categories (Skincare, Makeup, Haircare, Fragrance, Fashion), and milestone matrix. |
| **6. Gallery** | `/gallery/` | Photographic exhibition featuring public event photographs, celebrity brand launches, experiential counters, swatches, and licensing citations. |
| **7. Custom 404** | `*` | Elegant error page for missing URLs with return navigation links. |

---

## 4. Project Directory Structure

```text
The Nykaa Journey/
│
├── manage.py                   # Django CLI management script
├── requirements.txt            # Python dependencies
├── README.md                   # Comprehensive project documentation
├── .gitignore                  # Git exclusion rules
├── db.sqlite3                  # SQLite relational database
│
├── config/                     # Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py             # App registration, templates & static dirs
│   ├── urls.py                 # Root URL router & 404 handler
│   └── wsgi.py
│
├── biography/                  # Main educational application
│   ├── __init__.py
│   ├── admin.py                # Admin configuration
│   ├── apps.py                 # Biography app configuration
│   ├── models.py               # Models definition
│   ├── urls.py                 # Biography URL routing
│   ├── views.py                # View controllers for all 6 pages & 404
│   ├── tests.py                # Automated test suite
│   └── migrations/             # Database migration files
│       ├── 0001_initial.py
│       └── 0002_delete_feedback.py
│
├── templates/                  # Django HTML5 templates
│   ├── base.html               # Master layout with responsive nav & footer
│   ├── home.html               # Page 1: Hero & Overview
│   ├── success_story.html      # Page 2: CSS Timeline & Lessons
│   ├── achievements.html       # Page 3: Awards & Recognition
│   ├── personal_life.html      # Page 4: Family & Leadership
│   ├── about_nykaa.html        # Page 5: Business Model & Categories
│   ├── gallery.html            # Page 6: Curated Photo Grid
│   └── 404.html                # Custom 404 error page
│
└── static/                     # Static assets
    ├── css/
    │   └── style.css           # Complete luxury editorial stylesheet
    └── images/                 # Image assets (Wikimedia, Forbes & Unsplash)
        ├── nykaa-logo.svg      # Official vector logo
        ├── falguni-nayar.jpg   # Real photograph of Falguni Sanjay Nayar
        ├── bse-listing.jpg     # Bombay Stock Exchange building
        ├── iim-ahmedabad.jpg   # IIM Ahmedabad Louis Kahn Plaza
        ├── nykaa-brand.jpg     # Nykaa brand flatlay
        ├── nykaa-store.jpg     # Nykaa Luxe store interior
        ├── nykaa-beauty-products.jpg
        ├── skincare.jpg
        ├── makeup.jpg
        ├── haircare.jpg
        ├── fragrance.jpg
        ├── fashion.jpg
        └── gallery/            # Extended photographic assets
            ├── janhvi-nykaa-launch.jpg
            ├── nykaa-awards-aishwarya.jpg
            ├── beauty-counter.jpg
            ├── lipstick-collection.jpg
            └── wellness-spa.jpg
```

---

## 5. Installation and Execution Guide

Follow these simple steps to run the website locally on **Windows**, **macOS**, or **Linux**:

### Step 1: Open Terminal / PowerShell in the Project Directory
Navigate to the root directory where `manage.py` is located:
```powershell
cd "c:\Users\ASUS\OneDrive\Desktop\The Nykaa Journey"
```

### Step 2: Create a Python Virtual Environment
```powershell
python -m venv venv
```

### Step 3: Activate the Virtual Environment
- **On Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- **On macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### Step 4: Install Dependencies
```powershell
pip install -r requirements.txt
```

### Step 5: Apply Database Migrations
```powershell
python manage.py migrate
```

### Step 6: Launch the Development Server
```powershell
python manage.py runserver
```

### Step 7: Open the Website in Your Browser
Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to explore the live website!

---

## 6. Real Photograph Configuration

The homepage displays a genuine photograph of **Falguni Sanjay Nayar** (`static/images/falguni-nayar.jpg`), styled with:
- `object-fit: cover;`
- `object-position: center top;`
- High-resolution rounded portrait card with a deep burgundy backing and subtle gold border accents.

*Custom Photo Placement:* To provide a different official photograph, simply save your JPEG file as `static/images/falguni-nayar.jpg` and refresh the browser.

---

## 7. Media & Photographic Attributions

In strict compliance with academic standards, all images are credited to their original creators:

- **Falguni Nayar Portrait:** Forbes Leadership Profile Archives.
- **Nykaa Logo Vector:** [Wikimedia Commons File:Nykaa New Logo.svg](https://commons.wikimedia.org/wiki/File:Nykaa_New_Logo.svg) (Public Domain / Brand Identity).
- **Bombay Stock Exchange:** [Wikimedia Commons File:Bombay Stock Exchange.jpg](https://commons.wikimedia.org/wiki/File:Bombay_Stock_Exchange.jpg) (CC BY-SA 2.5).
- **IIM Ahmedabad Louis Kahn Plaza:** [Wikimedia Commons File:Indian Institute of Management Ahmedabad, Louis Kahn Plaza.jpg](https://commons.wikimedia.org/wiki/File:Indian_Institute_of_Management_Ahmedabad,_Louis_Kahn_Plaza.jpg) (CC BY-SA 3.0).
- **Janhvi Kapoor at Nykaa Launch:** [Wikimedia Commons File:Janhvi Kapoor snapped at Nykaa launch event (03).jpg](https://commons.wikimedia.org/wiki/File:Janhvi_Kapoor_snapped_at_Nykaa_launch_event_(03).jpg) (CC BY 3.0 via Bollywood Hungama).
- **Aishwarya Rai at Nykaa Femina Awards:** [Wikimedia Commons File:Aishwarya Rai graces the 4th edition of the Nykaa Femina Beauty Awards 2018 (01).jpg](https://commons.wikimedia.org/wiki/File:Aishwarya_Rai_graces_the_4th_edition_of_the_Nykaa_Femina_Beauty_Awards_2018_(01)_(cropped).jpg) (CC BY 3.0 via Bollywood Hungama).
- **Retail, Product & Lifestyle Photography:** Curated from [Unsplash](https://unsplash.com/) under the Unsplash Open License.

---

## 8. Instructions for Uploading to GitHub

To publish this project to GitHub for portfolio presentation:

1. **Initialize Git Repository:**
   ```powershell
   git init
   git add .
   git commit -m "feat: complete Falguni Nayar educational biography website"
   ```
2. **Link to Your GitHub Repository:**
   ```powershell
   git branch -M main
   git remote add origin https://github.com/<your-username>/the-nykaa-journey.git
   git push -u origin main
   ```

---

## 9. Student Author & Academic Disclaimer

- **Student Name:** [Enter Your Name Here]
- **Roll / Registration Number:** [Enter Roll Number]
- **Department:** Computer Science and Engineering (CSE)
- **Course:** B.Tech II Year &bull; Web Development &amp; Frameworks Lab
- **Academic Year:** 2025&ndash;2026

> **Academic Disclaimer:** This website is an independent educational study created solely for non-commercial academic evaluation. It is not affiliated with, endorsed by, or representing Nykaa (FSN E-Commerce Ventures Ltd) or Falguni Sanjay Nayar. All trademarks and brand names belong to their respective owners.
