# Word of the Day Website

A beautiful, straightforward website that displays a new English word daily, complete with origin, pronunciation, use cases, and emotional tone.

## Features

- **Daily Word Display**: Shows a different word each day based on the date
- **Comprehensive Information**: Each word includes:
  - Origin and etymology
  - Pronunciation guide
  - Use cases with contextual examples
  - Emotional tone and feeling description
- **Random Word Browser**: "View Another Word" button to explore the collection
- **Clean, Modern Design**: Responsive layout that works on all devices
- **300+ Word Database**: Extensive collection of interesting English words

## Project Structure

```
word-of-the-day/
├── index.html          # Main HTML file
├── styles.css          # Styling and layout
├── script.js           # JavaScript logic for word selection
├── words.json          # Database of words with details
├── expand_words.py     # Script to add more words
└── README.md           # This file
```

## How It Works

1. **Daily Selection**: Uses a date-based algorithm to select a consistent word for each day
2. **Word Display**: Shows the selected word with all its information in a clean card layout
3. **Random Mode**: Click "View Another Word" to explore words randomly

## Local Development

1. Clone or download this repository
2. Open `index.html` in a web browser
3. For local development with JSON loading, use a local server:
   - **Python**: `python -m http.server 8000`
   - **Node.js**: `npx serve`
   - **VS Code**: Use the Live Server extension

## Adding More Words

Use the `expand_words.py` script to add more words:

```bash
python expand_words.py
```

Edit the `additional_words` array in `expand_words.py` to add new words. Each word entry should follow this structure:

```json
{
  "word": "Example",
  "pronunciation": "/ɪɡˈzæmpəl/",
  "origin": "Word origin and etymology",
  "useCases": [
    {
      "context": "Context name",
      "example": "Example sentence using the word"
    }
  ],
  "feeling": "Emotional tone and feeling description"
}
```

## Deployment Options

### Option 1: GitHub Pages (Free, Easy)

1. Create a GitHub repository
2. Upload all files to the repository
3. Go to Settings → Pages
4. Select source branch (usually `main` or `master`)
5. Your site will be available at `https://yourusername.github.io/repository-name/`

**Pros**: Free, easy, automatic HTTPS
**Cons**: Public repository (unless using GitHub Pro)

### Option 2: Netlify (Free, Recommended)

1. Create account at [netlify.com](https://netlify.com)
2. Drag and drop the project folder, OR
3. Connect your GitHub repository for automatic deployments
4. Site is live immediately with a custom domain option

**Pros**: Free, fast, automatic deployments, custom domains
**Cons**: None for basic use

### Option 3: Vercel (Free, Fast)

1. Create account at [vercel.com](https://vercel.com)
2. Import your GitHub repository or upload files
3. Deploy with one click

**Pros**: Free, very fast, great for static sites
**Cons**: None for basic use

### Option 4: Traditional Web Hosting

Upload all files via FTP/SFTP to your web host:
- Ensure `index.html` is in the root directory
- All files (CSS, JS, JSON) should be accessible
- Most shared hosting providers work fine

## Potential Issues and Solutions

### Issue 1: JSON File Not Loading (CORS Error)

**Problem**: When opening `index.html` directly (file://), browsers block JSON loading due to CORS.

**Solution**: Use a local server (see Local Development section above).

### Issue 2: Words Not Displaying

**Problem**: Console shows errors about fetching words.json.

**Solutions**:
- Ensure `words.json` is in the same directory as `index.html`
- Check file path capitalization (case-sensitive on some servers)
- Verify JSON syntax is valid (use a JSON validator)

### Issue 3: Date-Based Selection Not Working

**Problem**: Same word appears every day instead of changing.

**Solution**: The algorithm uses a reference date (2024-01-01). This ensures consistency. Each day will show a different word based on the number of days since the reference date, modulo the number of words.

### Issue 4: Mobile Display Issues

**Problem**: Layout looks broken on mobile devices.

**Solution**: The CSS includes responsive design. Ensure viewport meta tag is present in HTML (already included).

### Issue 5: Large words.json File Size

**Problem**: Loading 300+ words makes the JSON file large.

**Solution**: 
- Current size (~100-200KB) is acceptable for most connections
- For production, consider:
  - Gzip compression (automatic on most hosts)
  - Lazy loading words as needed
  - Splitting into multiple JSON files

### Issue 6: Browser Compatibility

**Problem**: Website doesn't work in older browsers.

**Solution**: Uses modern JavaScript (async/await, fetch). For older browser support:
- Use Babel to transpile JavaScript
- Include fetch polyfill for Internet Explorer
- Test in target browsers

## Customization

### Changing Colors

Edit the CSS variables in `styles.css`:

```css
:root {
  --primary-color: #2c3e50;    /* Main text color */
  --secondary-color: #3498db;  /* Accent color */
  --accent-color: #e74c3c;     /* Highlight color */
  /* ... */
}
```

### Changing Reference Date

In `script.js`, modify the `getDateIndex()` function:

```javascript
const startDate = new Date('2024-01-01'); // Change this date
```

### Adding More Word Information

Extend the word object structure in `words.json` and update the `displayWord()` function in `script.js` to show the new fields.

## Future Enhancements

Possible improvements:
- User favorites/bookmarks
- Search functionality
- Word categories/tags
- Previous/next word navigation
- Share word on social media
- Audio pronunciation
- Word quizzes
- Email newsletter option

## License

This project is open source and available for personal and commercial use.

## Credits

Created as a vocabulary learning tool. Word definitions and etymologies compiled from various linguistic sources.

---

**Current Status**: The website currently contains 119 words. The `expand_words.py` script is set up and ready to expand the database to 300+ words. Simply edit the `additional_words` array in the script and run it to add more words.

**Quick Expansion**: To quickly reach 300+ words, you can:
1. Edit `expand_words.py` and add more word entries to the `additional_words` array
2. Run `python expand_words.py` to merge them into `words.json`
3. Repeat as needed until you have 300+ words

