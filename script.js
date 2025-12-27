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

// Daily Life Tips Data
const dailyTips = [
    "Start your day with gratitude. Write down three things you're thankful for each morning - it sets a positive tone for the entire day.",
    "Practice deep breathing for 2-3 minutes when feeling stressed. Inhale for 4 counts, hold for 4, exhale for 4. It calms your nervous system instantly.",
    "Stay hydrated! Your brain is 75% water. Dehydration can affect your mood, energy, and cognitive function. Aim for 8 glasses daily.",
    "Take regular breaks from screens. Every hour, look at something 20 feet away for 20 seconds - the 20-20-20 rule protects your eyes.",
    "Make your bed each morning. This small win gives you a sense of accomplishment and sets a productive tone for the day.",
    "Practice active listening. When someone speaks, focus entirely on understanding their message rather than planning your response.",
    "Create a 'done list' instead of just a to-do list. Celebrate completed tasks - it boosts motivation and shows your progress.",
    "Spend time in nature daily. Even 10 minutes outside can reduce stress, improve mood, and boost creativity.",
    "Limit decision fatigue by planning outfits, meals, and important choices the night before. Preserve mental energy for bigger decisions.",
    "Practice the 'two-minute rule': If a task takes less than two minutes, do it immediately. It prevents small tasks from accumulating.",
    "End your day by writing down one thing you learned. This reflection practice enhances learning and self-awareness.",
    "Use the Pomodoro Technique: Work for 25 minutes, then take a 5-minute break. This method increases focus and prevents burnout.",
    "Practice kindness to yourself. Speak to yourself as you would to a good friend. Self-compassion improves mental health.",
    "Keep a water bottle visible on your desk. Visual reminders make it easier to maintain healthy habits throughout the day.",
    "Set phone boundaries: Designate phone-free times and spaces (like meals and bedtime) to improve relationships and sleep quality.",
    "Practice single-tasking instead of multitasking. Focus on one activity at a time for better quality and less stress.",
    "Create a morning ritual you enjoy. Whether it's meditation, exercise, or coffee, consistent routines reduce decision fatigue.",
    "Express appreciation daily. Tell someone what you appreciate about them - it strengthens relationships and spreads positivity.",
    "Learn something new every week. Reading an article, watching a tutorial, or exploring a new topic keeps your mind sharp and engaged.",
    "Practice 'no' confidently. Setting boundaries protects your time and energy for what truly matters to you."
];

let currentTipIndex = 0;

// Load and display daily tip
function loadDailyTip() {
    // Use date to get consistent tip for each day
    const today = new Date();
    const dayOfYear = Math.floor((today - new Date(today.getFullYear(), 0, 0)) / 1000 / 60 / 60 / 24);
    currentTipIndex = dayOfYear % dailyTips.length;
    
    displayTip(currentTipIndex);
}

// Display tip
function displayTip(index) {
    const tipTextElement = document.getElementById('tipText');
    const tipIcon = document.querySelector('.tip-icon');
    
    // Fade out
    tipTextElement.style.opacity = '0';
    tipTextElement.style.transform = 'scale(0.95)';
    if (tipIcon) {
        tipIcon.style.transform = 'rotate(-10deg) scale(0.9)';
    }
    
    setTimeout(() => {
        tipTextElement.textContent = dailyTips[index];
        // Fade in with animation
        tipTextElement.style.opacity = '1';
        tipTextElement.style.transform = 'scale(1)';
        if (tipIcon) {
            tipIcon.style.transform = 'rotate(0deg) scale(1)';
        }
    }, 250);
}

// Load next tip (for button)
function loadNextTip() {
    currentTipIndex = (currentTipIndex + 1) % dailyTips.length;
    displayTip(currentTipIndex);
}

// Initialize when page loads
loadWords();
loadDailyTip();


