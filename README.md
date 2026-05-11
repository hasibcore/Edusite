# Godhuli Educational Portal (EduSite)

Welcome to the **Godhuli Educational Portal**, a premium, high-performance educational platform designed for SSC and HSC students. This project is built as a highly interactive Single Page Application (SPA) using HTML, Vanilla CSS, and JavaScript.

## 🚀 Quick Start
To run this project locally:
1. Clone the repository.
2. Open `index.html` in any modern web browser.
3. For the best experience, use a local server (like Live Server in VS Code) to handle `localStorage` and routing properly.

## 📁 Project Structure
- `index.html`: The main entry point. Contains the core structure and most of the JavaScript logic.
- `style.css`: The central design system. Contains the theme variables, glassmorphism effects, and responsive grid layouts.
- `Universal_App.html`: A standalone version of the portal for testing or distribution.
- `assets/`: (Planned) Directory for images, icons, and PDFs.

## 🛠 Core Systems

### 1. Internationalization (i18n)
The site supports English (`en`) and Bengali (`bn`). 
- Data is stored in the `i18n` object.
- Use `data-i18n` attributes on HTML elements to auto-translate.
- Function: `applyLanguage(lang)` handles the switching.

### 2. Theme Switching
Supports **Dark Mode** (default) and **Light Mode**.
- Controlled via `body.light-theme` class.
- Preference is saved in `localStorage.getItem('theme')`.
- Function: `toggleTheme()` switches modes and updates slider images.

### 3. Subject Dashboard
The dashboard is dynamically rendered using the `renderSubjects()` function based on the `currentLevel` (SSC/HSC).
- Data Sources: `eduDataBN` and `eduDataEN`.
- Icons are styled as **perfect circles** with glowing effects.

### 4. Important Design Patterns
- **Neon Glassmorphism**: Used in the Contact and Notice Board sections.
- **Strict Circularity**: Subject and sidebar icons use `!important` dimensions and `aspect-ratio: 1/1` in `style.css` to prevent them from becoming ovals on different screens.

## 🧠 Knowledge for AI Assistants (Antigravity)
- **Icon Squashing**: If icons appear as ovals, do NOT change the `border-radius`. Instead, ensure `flex-shrink: 0` and fixed `width`/`height` with `!important` are set.
- **Layout Expansion**: The main layout uses a grid-based `main-wrapper` with a `max-width: 1800px`. Avoid narrowing this as it causes content "clamping."
- **Routing**: The "pages" (Dashboard, Courses, Profile, Contact, Sajaw) are simply hidden/shown `<div>` containers. Use the `showDashboard()`, `showContact()`, etc. functions to navigate.

## 📞 Contact & Support
- **Founder**: Hasibul Hasan (hasibulhasancore@gmail.com)
- **Official Page**: [Godhuli Official](https://www.facebook.com/share/1E2QAmpt9v/)

---
*Maintained with ❤️ by the Godhuli Team.*