document.addEventListener('DOMContentLoaded', () => {
    // Global Marquee Logic
    const marqueeContainer = document.getElementById('global-marquee-container');
    const textContent = `SOCIAL DEMOCRATIC ALLIANCE &bull; 2068 &bull; `;
    const repeatCount = 10; 
    const rowCount = 12;    

    const fullText = textContent.repeat(repeatCount);

    if (marqueeContainer) {
        for (let i = 0; i < rowCount; i++) {
            const row = document.createElement('div');
            row.className = 'marquee-row';
            
            const span1 = document.createElement('span');
            span1.className = 'marquee-text';
            span1.innerHTML = fullText;

            const span2 = document.createElement('span');
            span2.className = 'marquee-text';
            span2.innerHTML = fullText;

            row.appendChild(span1);
            row.appendChild(span2);

            marqueeContainer.appendChild(row);
        }
    }

    // Theme Toggle Logic
    const themeToggleBtn = document.getElementById('theme-toggle');
    if (themeToggleBtn) {
        // Check for saved theme
        const savedTheme = localStorage.getItem('theme') || 'dark'; // Dark is default
        document.documentElement.setAttribute('data-theme', savedTheme);
        themeToggleBtn.textContent = savedTheme === 'dark' ? 'Light Mode' : 'Dark Mode';

        themeToggleBtn.addEventListener('click', () => {
            const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            document.documentElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            
            themeToggleBtn.textContent = newTheme === 'dark' ? 'Light Mode' : 'Dark Mode';
        });
    }
});
