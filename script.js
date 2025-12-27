let wordsData = [];
let currentDateIndex = 0;

// Load words data
async function loadWords() {
    try {
        const response = await fetch('words.json');
        wordsData = await response.json();
        initializeWord();
    } catch (error) {
        console.error('Error loading words:', error);
        document.getElementById('word').textContent = 'Error loading words';
    }
}

// Get date-based index for consistent daily word
function getDateIndex() {
    const startDate = new Date('2024-01-01'); // Starting reference date
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    
    const diffTime = today - startDate;
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
    
    return diffDays % wordsData.length;
}

// Initialize word display
function initializeWord() {
    if (wordsData.length === 0) return;
    
    // Display current date
    const today = new Date();
    const dateString = today.toLocaleDateString('en-US', { 
        weekday: 'long', 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric' 
    });
    document.getElementById('dateDisplay').textContent = dateString;
    
    // Load word of the day
    currentDateIndex = getDateIndex();
    displayWord(wordsData[currentDateIndex]);
}

// Display word information
function displayWord(word) {
    document.getElementById('word').textContent = word.word;
    document.getElementById('pronunciation').textContent = word.pronunciation;
    document.getElementById('origin').textContent = word.origin;
    document.getElementById('feeling').textContent = word.feeling;
    
    // Display use cases
    const useCasesDiv = document.getElementById('useCases');
    if (Array.isArray(word.useCases)) {
        let html = '<ul>';
        word.useCases.forEach(useCase => {
            html += `<li><strong>${useCase.context}:</strong> ${useCase.example}</li>`;
        });
        html += '</ul>';
        useCasesDiv.innerHTML = html;
    } else {
        useCasesDiv.innerHTML = `<p>${word.useCases}</p>`;
    }
}

// Load random word (for "View Another Word" button)
function loadRandomWord() {
    if (wordsData.length === 0) return;
    
    let randomIndex;
    do {
        randomIndex = Math.floor(Math.random() * wordsData.length);
    } while (randomIndex === currentDateIndex && wordsData.length > 1);
    
    currentDateIndex = randomIndex;
    displayWord(wordsData[randomIndex]);
}

// Initialize when page loads
loadWords();

