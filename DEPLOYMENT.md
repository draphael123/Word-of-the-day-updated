# Deployment Guide - Word of the Day Website

## Quick Deployment Summary

This website is a **static site** (HTML, CSS, JavaScript, JSON) and can be deployed anywhere that serves static files.

## Recommended Deployment Options

### 🚀 Option 1: Netlify (Recommended - Easiest & Free)

**Steps:**
1. Go to [netlify.com](https://netlify.com) and sign up (free)
2. Drag and drop your project folder onto Netlify's deploy area
3. Your site is live immediately with a URL like `your-site-name.netlify.app`
4. Optionally connect a custom domain (free SSL included)

**Pros:**
- ✅ Free forever for personal projects
- ✅ Automatic HTTPS
- ✅ Fast global CDN
- ✅ One-click deployment
- ✅ Can connect to GitHub for automatic deployments

**Cons:**
- None for basic use

**Time to Deploy:** 2 minutes

---

### 🌐 Option 2: GitHub Pages (Free)

**Steps:**
1. Create a GitHub account if you don't have one
2. Create a new repository (make it public, or use GitHub Pro for private)
3. Upload all project files to the repository
4. Go to Settings → Pages
5. Select source branch (usually `main`)
6. Your site will be at `https://yourusername.github.io/repository-name/`

**Pros:**
- ✅ Free
- ✅ Easy version control
- ✅ Automatic deployments on push

**Cons:**
- Public repository required (unless you have GitHub Pro)
- Slightly slower than Netlify/Vercel

**Time to Deploy:** 5-10 minutes

---

### ⚡ Option 3: Vercel (Free & Fast)

**Steps:**
1. Go to [vercel.com](https://vercel.com) and sign up
2. Click "Add New Project"
3. Import from GitHub or upload folder
4. Deploy (usually automatic)

**Pros:**
- ✅ Free
- ✅ Very fast
- ✅ Automatic HTTPS
- ✅ Great for static sites

**Cons:**
- None for basic use

**Time to Deploy:** 3-5 minutes

---

### 🏠 Option 4: Traditional Web Hosting (cPanel, etc.)

**Steps:**
1. Log into your web hosting control panel (cPanel, Plesk, etc.)
2. Navigate to File Manager
3. Upload all files to `public_html` or `www` directory
4. Ensure `index.html` is in the root
5. Visit your domain - site should be live

**Pros:**
- Works with any hosting provider
- Use your existing domain

**Cons:**
- May cost money (unless you already have hosting)
- Manual uploads for updates

---

## Pre-Deployment Checklist

- [ ] All files are in the same directory:
  - `index.html`
  - `styles.css`
  - `script.js`
  - `words.json`
- [ ] Test locally using a web server (not just opening HTML file)
- [ ] Verify `words.json` loads correctly (check browser console)
- [ ] Test on mobile device or responsive mode
- [ ] Ensure word count meets your needs (currently 119, expandable to 300+)

## Known Issues & Solutions

### Issue: CORS Error When Testing Locally

**Symptom:** Opening `index.html` directly shows "Error loading words" in console

**Cause:** Browsers block local JSON file loading due to CORS policy

**Solution:** Use a local server:
```bash
# Python 3
python -m http.server 8000

# Then visit: http://localhost:8000
```

### Issue: Words Not Loading After Deployment

**Possible Causes:**
1. **File path issue:** Ensure `words.json` is in same directory as `index.html`
2. **Case sensitivity:** Some servers are case-sensitive. Ensure filenames match exactly
3. **JSON syntax error:** Validate `words.json` using a JSON validator
4. **Server not serving JSON:** Most modern hosts serve JSON by default. If not, you may need to configure MIME types

**Solution:**
- Check browser developer console for specific errors
- Verify file paths are correct
- Test JSON file loads by visiting `yoursite.com/words.json` directly

### Issue: Same Word Shows Every Day

**Cause:** Browser caching or timezone issues

**Solution:**
- The date-based selection uses UTC. This is intentional for consistency
- Each calendar day shows the same word worldwide
- Clear browser cache if testing locally

### Issue: Mobile Layout Issues

**Solution:**
- The site includes responsive CSS
- Test in browser developer tools (mobile view)
- Ensure viewport meta tag is present (already included in HTML)

### Issue: Large words.json File Size

**Current Status:** With 119 words, file is ~50-80KB (acceptable)

**When Expanded to 300+ Words:**
- File may be 150-300KB (still acceptable)
- Most hosts compress automatically (gzip)
- If concerned, consider:
  - Lazy loading (load words as needed)
  - Splitting into multiple JSON files
  - Using a database (more complex, not needed for this project)

## Post-Deployment Testing

1. ✅ Visit your deployed URL
2. ✅ Verify word displays correctly
3. ✅ Check all sections (Origin, Use Cases, Feeling) show content
4. ✅ Test "View Another Word" button
5. ✅ Test on mobile device
6. ✅ Verify word changes daily (wait 24 hours or test by changing date)
7. ✅ Check browser console for errors

## Custom Domain Setup (Optional)

### Netlify:
1. Go to Domain Settings
2. Add custom domain
3. Follow DNS instructions (usually just add CNAME record)

### GitHub Pages:
1. Add `CNAME` file to repository with your domain
2. Configure DNS with your domain registrar
3. Add A records or CNAME as instructed

### Vercel:
1. Go to Project Settings → Domains
2. Add your domain
3. Follow DNS setup instructions

## Maintenance

### Adding More Words:
1. Edit `expand_words.py`
2. Add words to `additional_words` array
3. Run `python expand_words.py`
4. Commit and push changes
5. Site automatically updates (if using GitHub + auto-deploy)

### Updating Content:
- Edit HTML, CSS, or JavaScript files
- Test locally first
- Deploy changes using your chosen platform's method

## Performance Considerations

**Current Setup:** Excellent performance
- Static files load instantly
- No database queries
- Minimal JavaScript
- Small file sizes

**When Expanded:**
- 300+ words = ~200-300KB JSON file
- Still loads quickly on most connections
- Consider gzip compression (usually automatic)

## Security Considerations

**Current Setup:** Very secure
- No user input processed
- No server-side code
- No database
- No external API calls
- Static files only

**Recommendations:**
- Use HTTPS (automatic on Netlify, Vercel, GitHub Pages)
- Keep dependencies updated (none currently)
- Regular backups of your files

## Backup Strategy

1. **Version Control:** Use Git (recommended)
   - Push to GitHub
   - Automatic version history
   - Easy rollback

2. **Manual Backup:**
   - Download all files regularly
   - Store in cloud storage (Google Drive, Dropbox, etc.)

## Support Resources

- **Netlify Docs:** https://docs.netlify.com
- **GitHub Pages Docs:** https://docs.github.com/pages
- **Vercel Docs:** https://vercel.com/docs
- **JSON Validator:** https://jsonlint.com

---

## Quick Start Commands

```bash
# Test locally
python -m http.server 8000
# Visit: http://localhost:8000

# Add more words
python expand_words.py

# Check word count
python -c "import json; print(f'{len(json.load(open(\"words.json\")))} words')"
```

---

**Recommended:** Start with **Netlify** - it's the easiest and fastest option for deploying static sites.

