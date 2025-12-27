import json
import re

# Dictionary of meanings for words
meanings_dict = {
    "Serendipity": "The occurrence and development of events by chance in a happy or beneficial way; a fortunate accident.",
    "Ephemeral": "Lasting for a very short time; transient, fleeting.",
    "Mellifluous": "Having a sweet, musical, pleasant sound; flowing smoothly.",
    "Resilient": "Able to withstand or recover quickly from difficult conditions; able to bounce back.",
    "Quintessential": "Representing the most perfect example of a quality or class; the essence of something.",
    "Petrichor": "The pleasant earthy smell produced when rain falls on dry soil.",
    "Eloquent": "Fluent or persuasive in speaking or writing; expressing something clearly and effectively.",
    "Ineffable": "Too great or extreme to be expressed or described in words; beyond description.",
    "Ubiquitous": "Present, appearing, or found everywhere; omnipresent.",
    "Luminous": "Full of or shedding light; bright or shining, especially in the dark.",
    "Enigmatic": "Difficult to interpret or understand; mysterious, puzzling.",
    "Resplendent": "Attractive and impressive through being richly colorful or sumptuous; splendid, magnificent.",
    "Pernicious": "Having a harmful effect, especially in a gradual or subtle way; destructive, deadly.",
    "Voracious": "Wanting or devouring great quantities of food; having a very eager approach to an activity.",
    "Melancholy": "A feeling of pensive sadness, typically with no obvious cause; a sad, gloomy state.",
    "Benevolent": "Well meaning and kindly; showing goodwill, charitable.",
    "Paradigm": "A typical example or pattern of something; a model or framework.",
    "Solitude": "The state or situation of being alone; isolation, seclusion.",
    "Meticulous": "Showing great attention to detail; very careful and precise.",
    "Magnanimous": "Very generous or forgiving, especially toward a rival or someone less powerful than oneself.",
    "Intrepid": "Fearless, adventurous; showing no fear of dangerous situations.",
    "Prodigious": "Remarkably or impressively great in extent, size, or degree; enormous.",
    "Ethereal": "Extremely delicate and light in a way that seems too perfect for this world; heavenly, celestial.",
    "Tenacious": "Tending to keep a firm hold of something; persistent, determined.",
    "Vivacious": "Attractively lively and animated; spirited, energetic.",
    "Zenith": "The time at which something is most powerful or successful; the highest point.",
    "Nadir": "The lowest point in the fortunes of a person or organization; rock bottom.",
    "Laconic": "Using very few words; concise to the point of being mysterious or abrupt.",
    "Ebullient": "Cheerful and full of energy; enthusiastic, exuberant.",
    "Omnipotent": "Having unlimited power; able to do anything; all-powerful.",
    "Aesthetic": "Concerned with beauty or the appreciation of beauty; having a pleasing appearance.",
    "Juxtaposition": "The fact of two things being seen or placed close together with contrasting effect.",
    "Idiosyncrasy": "A mode of behavior or way of thought peculiar to an individual; a distinctive characteristic.",
    "Equanimity": "Mental calmness, composure, and evenness of temper, especially in a difficult situation.",
    "Pragmatic": "Dealing with things sensibly and realistically in a way that is based on practical rather than theoretical considerations.",
    "Sycophant": "A person who acts obsequiously toward someone important in order to gain advantage; a yes-man.",
    "Panacea": "A solution or remedy for all difficulties or diseases; a cure-all.",
    "Esoteric": "Intended for or likely to be understood by only a small number of people with specialized knowledge; obscure.",
    "Capricious": "Given to sudden and unaccountable changes of mood or behavior; unpredictable, fickle.",
    "Proclivity": "A tendency to choose or do something regularly; an inclination or predisposition toward a particular thing.",
    "Inequity": "Lack of fairness or justice; unfair treatment or circumstance.",
    "Magnificent": "Impressively beautiful, elaborate, or extravagant; extremely good or impressive.",
    "Cacophony": "A harsh, discordant mixture of sounds; noise, dissonance.",
    "Euphonic": "Pleasing to the ear; having a pleasant sound; harmonious.",
    "Nebulous": "Unclear, vague, or ill-defined; hazy, indistinct.",
    "Lucid": "Expressed clearly; easy to understand; clear, comprehensible.",
    "Auspicious": "Conducive to success; favorable; promising success or good fortune.",
    "Ominous": "Giving the impression that something bad or unpleasant is going to happen; threatening, inauspicious.",
    "Gregarious": "Fond of company; sociable; liking to be with other people.",
    "Reticent": "Not revealing one's thoughts or feelings readily; reserved, uncommunicative.",
    "Exquisite": "Extremely beautiful and delicate; intensely felt; perfect, flawless.",
    "Taciturn": "Reserved or uncommunicative in speech; saying little; silent.",
    "Volatile": "Liable to change rapidly and unpredictably, especially for the worse; unstable, explosive.",
    "Stoic": "A person who can endure pain or hardship without showing their feelings or complaining; unemotional.",
    "Ambivalent": "Having mixed feelings or contradictory ideas about something or someone; uncertain.",
    "Clandestine": "Kept secret or done secretively, especially because illicit; hidden, covert.",
    "Diligent": "Having or showing care and conscientiousness in one's work or duties; hard-working, thorough.",
    "Fastidious": "Very attentive to and concerned about accuracy and detail; hard to please.",
    "Hedonistic": "Engaged in the pursuit of pleasure; sensually self-indulgent.",
    "Idyllic": "Extremely happy, peaceful, or picturesque; charmingly simple or serene.",
    "Jubilant": "Feeling or expressing great happiness and triumph; elated, triumphant.",
    "Kaleidoscopic": "Having complex patterns of colors; multicolored; complex and varied.",
    "Nefarious": "Wicked, villainous, or criminal; evil, iniquitous.",
    "Obfuscate": "Render obscure, unclear, or unintelligible; confuse, bewilder.",
    "Pristine": "In its original condition; unspoiled; clean and fresh as if new; immaculate.",
    "Quixotic": "Exceedingly idealistic; unrealistic and impractical; pursuing lofty but unattainable ideals.",
    "Rambunctious": "Uncontrollably exuberant; boisterous; noisy and difficult to control.",
    "Tranquil": "Free from disturbance; calm; peaceful, serene.",
    "Venerable": "Accorded a great deal of respect, especially because of age, wisdom, or character; revered.",
    "Wistful": "Having or showing a feeling of vague or regretful longing; nostalgic, melancholy.",
    "Xenophobic": "Having or showing a dislike of or prejudice against people from other countries; intolerant of foreigners.",
    "Yearning": "A feeling of intense longing for something; a deep desire or craving.",
    "Zealous": "Showing great energy or passion in pursuit of a cause or an objective; fervent, enthusiastic.",
    "Abstruse": "Difficult to understand; obscure; complex, esoteric.",
    "Acumen": "The ability to make good judgments and quick decisions, typically in a particular domain; insight, shrewdness.",
    "Adroit": "Clever or skillful in using the hands or mind; dexterous, nimble.",
    "Alacrity": "Brisk and cheerful readiness; eagerness, enthusiasm.",
    "Amalgamate": "Combine or unite to form one organization or structure; merge, blend.",
    "Ameliorate": "Make something bad or unsatisfactory better; improve, enhance.",
    "Amorphous": "Without a clearly defined shape or form; shapeless, formless.",
    "Anachronism": "A thing belonging or appropriate to a period other than that in which it exists; something out of its time.",
    "Analogous": "Comparable in certain respects, typically in a way that makes clearer the nature of the things compared; similar.",
    "Anathema": "Something or someone that one vehemently dislikes; a curse; a detested thing.",
    "Ancillary": "Providing necessary support to the primary activities or operation of an organization, institution, industry, or system; supplementary.",
    "Anomalous": "Deviating from what is standard, normal, or expected; abnormal, irregular.",
    "Antediluvian": "Of or belonging to the time before the biblical Flood; extremely old or old-fashioned.",
    "Antipathy": "A deep-seated feeling of dislike; aversion, hostility.",
    "Aplomb": "Self-confidence or assurance, especially when in a demanding situation; poise, composure.",
    "Apocryphal": "Of doubtful authenticity, although widely circulated as being true; dubious, questionable.",
    "Apposite": "Very appropriate or suitable; fitting, relevant.",
    "Arcane": "Understood by few; mysterious or secret; esoteric, obscure.",
    "Arduous": "Involving or requiring strenuous effort; difficult and tiring; laborious.",
    "Ascetic": "Characterized by severe self-discipline and abstention from all forms of indulgence; austere, strict.",
    "Assiduous": "Showing great care and perseverance; diligent, thorough.",
    "Austere": "Severe or strict in manner, attitude, or appearance; plain, simple.",
    "Avarice": "Extreme greed for wealth or material gain; cupidity, covetousness.",
    "Banal": "So lacking in originality as to be obvious and boring; trite, unoriginal.",
    "Bellicose": "Demonstrating aggression and willingness to fight; warlike, combative.",
    "Benign": "Gentle, kindly, favorable; not harmful in effect.",
    "Boisterous": "Noisy, energetic, and cheerful; rowdy, rambunctious.",
    "Bombastic": "High-sounding but with little meaning; inflated; pompous, grandiose.",
    "Bucolic": "Relating to the pleasant aspects of the countryside and country life; pastoral, rural.",
    "Cacophonous": "Involving or producing a harsh, discordant mixture of sounds; noisy, dissonant.",
    "Calamitous": "Involving calamity; catastrophic or disastrous; causing great harm.",
    "Callous": "Showing or having an insensitive and cruel disregard for others; unfeeling, hard-hearted.",
    "Candor": "The quality of being open and honest in expression; frankness, sincerity.",
    "Cathartic": "Providing psychological relief through the open expression of strong emotions; cleansing, purging.",
    "Caustic": "Able to burn or corrode organic tissue by chemical action; sarcastic in a scathing and bitter way.",
    "Cogent": "Clear, logical, and convincing; compelling, persuasive.",
    "Commensurate": "Corresponding in size or degree; in proportion; equivalent.",
}

# Read existing words
with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

# Add meanings to words
words_updated = 0
for word in words:
    word_name = word.get('word', '')
    if word_name in meanings_dict and 'meaning' not in word:
        word['meaning'] = meanings_dict[word_name]
        words_updated += 1
    elif word_name not in meanings_dict:
        print(f"Warning: No meaning found for '{word_name}'")

# Save updated words
with open('words.json', 'w', encoding='utf-8') as f:
    json.dump(words, f, indent=2, ensure_ascii=False)

print(f"Updated {words_updated} words with meanings.")
print(f"Total words in database: {len(words)}")

