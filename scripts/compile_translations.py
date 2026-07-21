import json
import os

print("Compiling translations.js...")

with open('data/new_translations.json', 'r', encoding='utf-8') as f:
    translations = json.load(f)

# The base logic to append
js_logic = """
document.addEventListener("DOMContentLoaded", () => {
  const currentLangDisplay = document.querySelector(".lang-current");
  const langOptions = document.querySelectorAll(".lang-option");
  const translatableElements = document.querySelectorAll("[data-i18n]");

  // Load saved language or default to Alanian
  const savedLang = localStorage.getItem("site-lang") || "al";
  setLanguage(savedLang);

  // Setup click listeners on dropdown options
  langOptions.forEach(option => {
    option.addEventListener("click", (e) => {
      e.preventDefault();
      const lang = option.getAttribute("data-lang");
      setLanguage(lang);
      
      // Keep dropdown open briefly to show selection then close
      const dropdown = document.querySelector(".lang-dropdown");
      dropdown.style.visibility = "hidden";
      dropdown.style.opacity = "0";
      setTimeout(() => {
        dropdown.style.visibility = "";
        dropdown.style.opacity = "";
      }, 200);
    });
  });

  function setLanguage(langCode) {
    if (!dictionary[langCode]) return;
    localStorage.setItem("site-lang", langCode);

    // Always get a fresh list of elements
    const translatableElements = document.querySelectorAll("[data-i18n]");

    // Update the UI text
    translatableElements.forEach(el => {
      const key = el.getAttribute("data-i18n");
      if (dictionary[langCode][key]) {
        if (el.tagName === "INPUT" && el.type === "submit") {
          el.value = dictionary[langCode][key];
        } else if (el.tagName === "INPUT" && el.type === "placeholder") {
          el.placeholder = dictionary[langCode][key];
        } else {
          el.innerHTML = dictionary[langCode][key];
        }
      }
    });

    // Force DOM repaint (fixes Safari/WebKit text rendering bugs)
    document.body.style.display = 'none';
    document.body.offsetHeight; // trigger reflow
    document.body.style.display = '';

    // Update active state in dropdown
    langOptions.forEach(opt => opt.classList.remove("active"));
    const activeOption = document.querySelector(`.lang-option[data-lang="${langCode}"]`);
    if (activeOption) {
      activeOption.classList.add("active");
    }

    // Update current lang text in toggle button (uppercase code)
    if (currentLangDisplay) {
      currentLangDisplay.textContent = langCode.toUpperCase();
    }

    // Save preference
    localStorage.setItem("site-lang", langCode);
  }
});
"""

# Format as JS
js_content = f"""// Simple dictionary-based translation system
// We map the 2-letter codes to the fictional languages for the UI
// al: Alanian
// ga: Gallic
// ac: Alcamerian
// ra: Rälandic
// my: Myrati
// au: Austrumish
// le: Leislandic

const dictionary = {json.dumps(translations, indent=2, ensure_ascii=False)};
{js_logic}"""

with open('assets/js/translations.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("translations.js compiled successfully!")
