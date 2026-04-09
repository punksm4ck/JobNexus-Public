"© 2026 Punksm4ck. All rights reserved."
"© 2026 Punksm4ck. All rights reserved."
"© 2026 Punksm4ck. All rights reserved."
#!/usr/bin/env python3
import pathlib

gitignore_lines = [
    "# Dependency directories",
    "node_modules/",
    "",
    "# Logs and databases",
    "bridge.log",
    "*.log",
    "",
    "# OS generated files",
    ".DS_Store",
    "Thumbs.db",
    "",
    "# Desktop shortcuts",
    "*.desktop"
]

readme_lines = [
    "# JobNexus 🌐 — Intelligent Job Search Platform",
    "",
    "JobNexus is a decentralized, local-first, enterprise-grade job search aggregator. It combines traditional API integrations (like Adzuna) with a headless Deno scraper bridge to autonomously extract data from walled-garden job boards like Indeed and ZipRecruiter, bypassing CORS and CAPTCHA restrictions.",
    "",
    "## 🚀 Key Features",
    "* **Zero-Touch Geolocation:** Automatically localizes searches using OpenStreetMap reverse-geocoding.",
    "* **Headless Scraper Bridge:** Built-in stealth Puppeteer integration via Deno to extract data autonomously.",
    "* **Kanban Application Tracker:** Integrated pipeline to track \"Applied\" status, visually graying out completed applications to prevent duplicates.",
    "* **Decentralized & Local-First:** Your data, tracking history, and API keys never leave your machine's local storage.",
    "",
    "## 🛠️ Installation & Setup",
    "",
    "### 1. Clone the Repository",
    "```bash",
    "git clone [https://github.com/punksm4ck/JobNexus-Public.git](https://github.com/punksm4ck/JobNexus-Public.git)",
    "cd JobNexus-Public",
    "```",
    "",
    "### 2. Setup the Deno Bridge (Required for Indeed/ZipRecruiter)",
    "JobNexus utilizes a Deno-powered microservice to bypass JS challenges on secure job boards.",
    "```bash",
    "# Ensure Deno is installed, then install the stealth node modules",
    "npm install",
    "",
    "# Run the backend bridge locally on port 3456",
    "deno run -A --node-modules-dir jobnexus_deno_bridge.ts",
    "```",
    "",
    "### 3. Launch the GUI",
    "Simply open `jobnexus_public.html` in any modern Chromium-based browser.",
    "Navigate to the **Configuration & APIs** tab to plug in your free Adzuna API keys and begin executing global searches.",
    "",
    "## 📄 License",
    "This project is licensed under the MIT License - see the LICENSE file for details."
]

license_lines = [
    "MIT License",
    "",
    "Copyright (c) 2026 punksm4ck",
    "",
    "Permission is hereby granted, free of charge, to any person obtaining a copy",
    "of this software and associated documentation files (the \"Software\"), to deal",
    "in the Software without restriction, including without limitation the rights",
    "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell",
    "copies of the Software, and to permit persons to whom the Software is",
    "furnished to do so, subject to the following conditions:",
    "",
    "The above copyright notice and this permission notice shall be included in all",
    "copies or substantial portions of the Software.",
    "",
    "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR",
    "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,",
    "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE",
    "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER",
    "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,",
    "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE",
    "SOFTWARE."
]

pathlib.Path('.gitignore').write_text('\n'.join(gitignore_lines), encoding='utf-8')
pathlib.Path('README.md').write_text('\n'.join(readme_lines), encoding='utf-8')
pathlib.Path('LICENSE').write_text('\n'.join(license_lines), encoding='utf-8')

print("Enterprise repository files generated perfectly.")
