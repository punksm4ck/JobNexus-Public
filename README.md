# JobNexus 🌐 — Intelligent Job Search Platform

JobNexus is a decentralized, local-first, enterprise-grade job search aggregator. It combines traditional API integrations (like Adzuna) with a headless Deno scraper bridge to autonomously extract data from walled-garden job boards like Indeed and ZipRecruiter, bypassing CORS and CAPTCHA restrictions.

## 🚀 Key Features
* **Zero-Touch Geolocation:** Automatically localizes searches using OpenStreetMap reverse-geocoding.
* **Headless Scraper Bridge:** Built-in stealth Puppeteer integration via Deno to extract data autonomously.
* **Kanban Application Tracker:** Integrated pipeline to track "Applied" status, visually graying out completed applications to prevent duplicates.
* **Decentralized & Local-First:** Your data, tracking history, and API keys never leave your machine's local storage.

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/punksm4ck/JobNexus-Public.git](https://github.com/punksm4ck/JobNexus-Public.git)
cd JobNexus-Public
```

### 2. Setup the Deno Bridge (Required for Indeed/ZipRecruiter)
JobNexus utilizes a Deno-powered microservice to bypass JS challenges on secure job boards.
```bash
# Ensure Deno is installed, then install the stealth node modules
npm install

# Run the backend bridge locally on port 3456
deno run -A --node-modules-dir jobnexus_deno_bridge.ts
```

### 3. Launch the GUI
Simply open `jobnexus_public.html` in any modern Chromium-based browser.
Navigate to the **Configuration & APIs** tab to plug in your free Adzuna API keys and begin executing global searches.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.