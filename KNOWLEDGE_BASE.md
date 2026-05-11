# Technical Knowledge Base - Godhuli Portal

This document preserves technical decisions and "gotchas" for future development by Antigravity or other AI agents.

## 🎨 CSS Architecture & Theme System

### Variable System
Located in `:root` and `body.light-theme`. 
- Always use variables like `var(--bg-dark)`, `var(--primary)`, etc., for styling to ensure theme compatibility.
- Special variables for the Contact section: `var(--contact-inner-bg)`, `var(--contact-text-h)`.

### The "Nuclear" Circular Icon Fix
Subject icons were previously becoming ovals due to flexbox stretching.
**Location:** `style.css` under `.sidebar-menu a .icon` and `.sc-icon`.
**Solution:**
- Use `!important` on `width`, `height`, `min-width`, etc.
- Use `aspect-ratio: 1 / 1 !important`.
- Use `flex-shrink: 0 !important`.
- Use `display: flex !important` with `align-items: center` and `justify-content: center`.

## 📜 JavaScript Logic & State

### Global State
- `currentUser`: Stores email of the logged-in user.
- `currentLang`: 'bn' or 'en'.
- `currentLevel`: 'SSC' or 'HSC'.
- All persisted in `localStorage` with keys like `edusite_user`, `edusite_lang`, `theme`.

### Dynamic Rendering
- **Subjects**: `renderSubjects()` uses `getEduData()` to pull from the correct language array.
- **Auth UI**: `renderAuthUI()` updates the top-right buttons and the "Kebab" menu.
- **Language**: `applyLanguage(lang)` iterates over all elements with `data-i18n`.

### Navigation (Pseudo-Routing)
All sections are in the DOM but hidden by default. Use functions like:
- `showDashboard()`
- `showCourses()`
- `showContact()`
- `showProfile()`
- `showSajaw()`
- `loadChapters(index)`

## 🖼 Asset Management
- **Images**: Most images use `onerror` fallbacks to `ui-avatars.com` or `via.placeholder.com` to ensure the UI doesn't break if local assets are missing.
- **Slider**: `updateSliderImages()` swaps backgrounds based on light/dark mode.

## 🛠 Troubleshooting for New AI
1. **Empty Right Sidebar?** The `main-wrapper` uses a 3-column grid. When viewing sections like "Contact", the right sidebar is hidden and the grid is adjusted to 2 columns in JS.
2. **Translation not working?** Check if the element has the `data-i18n` attribute and if the key exists in the `i18n` object in `index.html`.
3. **Layout too narrow?** Check `main-wrapper` max-width. It should be at least `1800px` for the "De-cramped" feel.
