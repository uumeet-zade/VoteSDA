document.addEventListener('DOMContentLoaded', () => {
    const marqueeContainer = document.getElementById('marquee-container');
    const textContent = `<span class="marquee-sda">SOCIAL DEMOCRATIC ALLIANCE</span> &bull; <span class="marquee-rej">REJUVENATION</span> &bull; `;
    const repeatCount = 10; // Number of times to repeat the text in a single row
    const rowCount = 12;    // Number of rows to fill the background

    // Create the full repeated text string for a row
    const fullText = textContent.repeat(repeatCount);

    for (let i = 0; i < rowCount; i++) {
        const row = document.createElement('div');
        row.className = 'marquee-row';
        
        // We need two identical text spans inside each row 
        // to make the CSS translate(-50%) loop seamless.
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
});
