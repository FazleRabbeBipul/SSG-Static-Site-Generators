# Static Site Generator (SSG)

A lightweight Python-based static site generator that converts Markdown files into fully functional HTML pages. This generator ensures a clean directory structure and a streamlined workflow for developing static websites.

---

## Features

- Converts Markdown files into static HTML pages.
- Supports custom HTML templates for consistent styling.
- Preserves directory structure while generating files.
- Copies static assets like CSS and images to the output directory.
- Uses a built-in Python HTTP server to preview the site locally.
- Modular and extendable Python codebase for easy maintenance.

![Static site](/static/images/workprocess.png)

---

## Architecture Overview

The system's data flow and core functionality are depicted below:

![Architecture Diagram](/static/images/architecture.png)

### High-Level Process:
1. **Markdown Input:**
   - Markdown files reside in the `/content` directory.
   - A template HTML file (`template.html`) provides the design layout.
2. **Static Site Generator:**
   - The Python code in `/src` reads Markdown and template files.
   - Generates HTML for each Markdown file and writes it to the `/public` directory.
3. **Static Assets:**
   - Any static assets (CSS, images, etc.) are copied to the `/public` directory.
4. **Preview Server:**
   - A built-in Python HTTP server serves the contents of `/public` on `http://localhost:8888`.
5. **Browser Preview:**
   - The final rendered website can be previewed in a browser.

---

## Technologies Used

- **Programming Language:** Python 3
- **Modules:**
  - `os` (for file and directory handling)
  - `http.server` (to serve files locally)
- **Markdown to HTML Conversion:** Custom parsing logic.

---

## How to Run

1. Clone the repository.
   ```bash
   git clone https://github.com/FazleRabbeBipul/SSG-Static-Site-Generators/
   cd SSG-Static-Site-Generators
   ```

2. Add your Markdown files to the `/content` directory.
3. Add or modify the HTML template (`template.html`).
4. Run the static site generator.
   ```bash
   python3 src/main.py
   ```
5. Start the local HTTP server to preview the generated site.
   ```bash
   python3 -m http.server 8888
   ```
6. Open a browser and navigate to:
   ```
   http://localhost:8888
   ```

---

## Usage

- Add Markdown files with the desired content into the `/content` directory.
- Use the `generate_pages_recursive` function to handle complex directory structures automatically.
- Modify `template.html` to customize the design of your static pages.

### Ideal Use Cases
Static sites are perfect for projects that do not require dynamic server-side logic or a database. Common examples include:
- Blogs
- Portfolios
- Landing pages
- Documentation


---

## Contribution Guidelines

We welcome contributions! Please:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request with a detailed description.

---
