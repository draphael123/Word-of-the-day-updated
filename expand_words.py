import json

# Additional words to add (expanded list)
additional_words = [
  {
    "word": "Abstruse",
    "pronunciation": "/abˈstro͞os/",
    "origin": "From Latin 'abstrusus' meaning 'concealed', from 'abstrudere' (to push away, conceal).",
    "useCases": [
      {"context": "Academic", "example": "The abstruse mathematical theory was difficult for students to grasp."},
      {"context": "Philosophy", "example": "He wrote abstruse essays that few could understand."}
    ],
    "feeling": "Complex, difficult, and obscure. This word suggests something hard to understand, often intentionally so."
  },
  {
    "word": "Acumen",
    "pronunciation": "/əˈkyo͞omən/",
    "origin": "From Latin 'acumen' meaning 'sharp point', from 'acuere' (to sharpen).",
    "useCases": [
      {"context": "Business", "example": "Her business acumen helped the company thrive."},
      {"context": "Intelligence", "example": "His political acumen was admired by both allies and opponents."}
    ],
    "feeling": "Sharp, insightful, and discerning. This word suggests keen intelligence and good judgment."
  },
  {
    "word": "Adroit",
    "pronunciation": "/əˈdroit/",
    "origin": "From French 'adroit' meaning 'right, skillful', from 'à droit' (to the right, properly).",
    "useCases": [
      {"context": "Skill", "example": "The adroit surgeon completed the operation flawlessly."},
      {"context": "Diplomacy", "example": "Her adroit handling of the crisis prevented conflict."}
    ],
    "feeling": "Skillful, clever, and nimble. This word suggests deftness and mental agility."
  },
  {
    "word": "Aesthetic",
    "pronunciation": "/esˈTHetik/",
    "origin": "From Greek 'aisthetikos' meaning 'of sense perception', from 'aisthanesthai' (to perceive).",
    "useCases": [
      {"context": "Design", "example": "The minimalist aesthetic created a sense of peace."},
      {"context": "Art", "example": "She had a refined aesthetic sensibility."}
    ],
    "feeling": "Beautiful, tasteful, and artistic. This word relates to beauty, art, and visual appeal."
  },
  {
    "word": "Alacrity",
    "pronunciation": "/əˈlakritē/",
    "origin": "From Latin 'alacritas' meaning 'cheerfulness, eagerness', from 'alacer' (brisk, eager).",
    "useCases": [
      {"context": "Response", "example": "She accepted the invitation with alacrity."},
      {"context": "Action", "example": "The team responded with alacrity to the emergency."}
    ],
    "feeling": "Eager, cheerful, and brisk. This word suggests enthusiastic promptness."
  },
  {
    "word": "Amalgamate",
    "pronunciation": "/əˈmalɡəˌmāt/",
    "origin": "From Medieval Latin 'amalgamare' meaning 'to mix with mercury', from 'amalgama' (alloy of mercury).",
    "useCases": [
      {"context": "Business", "example": "The companies decided to amalgamate to increase efficiency."},
      {"context": "Culture", "example": "The festival amalgamated traditions from multiple countries."}
    ],
    "feeling": "Unified, combined, and merged. This word suggests bringing different elements together."
  },
  {
    "word": "Ameliorate",
    "pronunciation": "/əˈmēlyəˌrāt/",
    "origin": "From Latin 'melior' (better) through French 'améliorer'.",
    "useCases": [
      {"context": "Conditions", "example": "The new policies helped ameliorate poverty in the region."},
      {"context": "Relations", "example": "The apology helped ameliorate tensions between the groups."}
    ],
    "feeling": "Improved, bettered, and enhanced. This word suggests making something better."
  },
  {
    "word": "Amorphous",
    "pronunciation": "/əˈmôrfəs/",
    "origin": "From Greek 'amorphos' meaning 'shapeless', from 'a-' (without) + 'morphe' (form).",
    "useCases": [
      {"context": "Shape", "example": "The amorphous cloud drifted across the sky."},
      {"context": "Ideas", "example": "His plans were still amorphous and needed structure."}
    ],
    "feeling": "Shapeless, formless, and undefined. This word suggests something lacking clear form or structure."
  },
  {
    "word": "Anachronism",
    "pronunciation": "/əˈnakrəˌnizəm/",
    "origin": "From Greek 'anachronismos' meaning 'against time', from 'ana-' (against) + 'chronos' (time).",
    "useCases": [
      {"context": "Historical", "example": "Wristwatches in a medieval film would be an anachronism."},
      {"context": "Language", "example": "Using 'thou' in modern conversation is an anachronism."}
    ],
    "feeling": "Outdated, misplaced, and temporal. This word suggests something from a different time period."
  },
  {
    "word": "Analogous",
    "pronunciation": "/əˈnaləɡəs/",
    "origin": "From Greek 'analogos' meaning 'proportional', from 'ana-' (according to) + 'logos' (ratio).",
    "useCases": [
      {"context": "Comparison", "example": "The structure of an atom is analogous to the solar system."},
      {"context": "Relationships", "example": "The situation was analogous to what happened last year."}
    ],
    "feeling": "Similar, comparable, and parallel. This word suggests a meaningful similarity or correspondence."
  },
  {
    "word": "Anathema",
    "pronunciation": "/əˈnaTHəmə/",
    "origin": "From Greek 'anathema' meaning 'something dedicated' or 'cursed', originally a votive offering.",
    "useCases": [
      {"context": "Religion", "example": "The heresy was declared anathema by the church."},
      {"context": "Personal", "example": "Dishonesty was anathema to her moral code."}
    ],
    "feeling": "Detestable, abhorrent, and cursed. This word suggests something strongly disliked or condemned."
  },
  {
    "word": "Ancillary",
    "pronunciation": "/ˈansəˌlerē/",
    "origin": "From Latin 'ancillaris' meaning 'of a maidservant', from 'ancilla' (maidservant).",
    "useCases": [
      {"context": "Services", "example": "The hospital provided ancillary services like counseling."},
      {"context": "Support", "example": "Ancillary equipment was needed for the main operation."}
    ],
    "feeling": "Subordinate, supporting, and supplementary. This word suggests something that supports but is not primary."
  },
  {
    "word": "Anomalous",
    "pronunciation": "/əˈnämələs/",
    "origin": "From Greek 'anomalos' meaning 'irregular', from 'a-' (not) + 'homalos' (even, regular).",
    "useCases": [
      {"context": "Data", "example": "Scientists discovered an anomalous reading that needed investigation."},
      {"context": "Behavior", "example": "His anomalous response puzzled everyone in the room."}
    ],
    "feeling": "Irregular, abnormal, and unusual. This word suggests something that deviates from the norm."
  },
  {
    "word": "Antediluvian",
    "pronunciation": "/ˌantēdəˈlo͞ovēən/",
    "origin": "From Latin 'ante' (before) + 'diluvium' (flood), referring to the time before the Biblical flood.",
    "useCases": [
      {"context": "Age", "example": "The antediluvian tree had stood for thousands of years."},
      {"context": "Ideas", "example": "His antediluvian views on gender roles were outdated."}
    ],
    "feeling": "Ancient, outdated, and extremely old. This word suggests something from a very distant past."
  },
  {
    "word": "Antipathy",
    "pronunciation": "/anˈtipəTHē/",
    "origin": "From Greek 'antipatheia' meaning 'opposition of feeling', from 'anti-' (against) + 'pathos' (feeling).",
    "useCases": [
      {"context": "Emotion", "example": "She felt deep antipathy toward injustice."},
      {"context": "Relations", "example": "There was mutual antipathy between the two leaders."}
    ],
    "feeling": "Hostile, averse, and strongly opposed. This word suggests a deep-seated dislike or aversion."
  },
  {
    "word": "Aplomb",
    "pronunciation": "/əˈpläm/",
    "origin": "From French 'aplomb' meaning 'perpendicularity, self-possession', from 'à plomb' (according to the plummet).",
    "useCases": [
      {"context": "Composure", "example": "She handled the crisis with remarkable aplomb."},
      {"context": "Confidence", "example": "The speaker answered difficult questions with aplomb."}
    ],
    "feeling": "Confident, self-assured, and composed. This word suggests poise and self-confidence."
  },
  {
    "word": "Apocryphal",
    "pronunciation": "/əˈpäkrəfəl/",
    "origin": "From Greek 'apokryphos' meaning 'hidden, obscure', from 'apo-' (away) + 'kryptein' (to hide).",
    "useCases": [
      {"context": "Stories", "example": "The apocryphal tale had been told so many times it seemed true."},
      {"context": "Texts", "example": "The apocryphal gospels are not included in the canonical Bible."}
    ],
    "feeling": "Questionable, dubious, and unverified. This word suggests something of doubtful authenticity."
  },
  {
    "word": "Apposite",
    "pronunciation": "/ˈapəzit/",
    "origin": "From Latin 'appositus' meaning 'placed near, applied', from 'apponere' (to place near).",
    "useCases": [
      {"context": "Relevance", "example": "Her comment was particularly apposite to the discussion."},
      {"context": "Examples", "example": "He provided an apposite example that clarified his point."}
    ],
    "feeling": "Relevant, appropriate, and fitting. This word suggests something well-suited and pertinent."
  },
  {
    "word": "Arcane",
    "pronunciation": "/ärˈkān/",
    "origin": "From Latin 'arcanus' meaning 'secret, hidden', from 'arca' (chest, box).",
    "useCases": [
      {"context": "Knowledge", "example": "The arcane rituals were known only to the initiates."},
      {"context": "Language", "example": "The text was written in arcane symbols no one could decipher."}
    ],
    "feeling": "Secret, mysterious, and esoteric. This word suggests knowledge accessible only to initiates."
  },
  {
    "word": "Arduous",
    "pronunciation": "/ˈärjo͞oəs/",
    "origin": "From Latin 'arduus' meaning 'steep, difficult', related to 'ardere' (to burn).",
    "useCases": [
      {"context": "Tasks", "example": "The arduous journey through the mountains took weeks."},
      {"context": "Work", "example": "She completed the arduous task despite the challenges."}
    ],
    "feeling": "Difficult, strenuous, and exhausting. This word suggests requiring great effort and endurance."
  },
  {
    "word": "Ascetic",
    "pronunciation": "/əˈsetik/",
    "origin": "From Greek 'asketikos' meaning 'monkish, hermit-like', from 'askein' (to exercise, practice).",
    "useCases": [
      {"context": "Lifestyle", "example": "The ascetic monk lived with minimal possessions."},
      {"context": "Philosophy", "example": "Her ascetic approach to life rejected material comforts."}
    ],
    "feeling": "Self-disciplined, austere, and simple. This word suggests rigorous self-denial and simplicity."
  },
  {
    "word": "Assiduous",
    "pronunciation": "/əˈsijo͞oəs/",
    "origin": "From Latin 'assiduus' meaning 'sitting down to', from 'assidere' (to sit by, attend to).",
    "useCases": [
      {"context": "Work", "example": "Her assiduous attention to detail ensured high quality."},
      {"context": "Study", "example": "The assiduous student studied every night."}
    ],
    "feeling": "Diligent, persistent, and careful. This word suggests constant, careful application."
  },
  {
    "word": "Austere",
    "pronunciation": "/ôˈstir/",
    "origin": "From Greek 'austeros' meaning 'harsh, severe', from 'auein' (to dry, parch).",
    "useCases": [
      {"context": "Style", "example": "The austere architecture emphasized function over decoration."},
      {"context": "Personality", "example": "His austere manner intimidated some people."}
    ],
    "feeling": "Severe, strict, and simple. This word suggests sternness and lack of luxury or decoration."
  },
  {
    "word": "Avarice",
    "pronunciation": "/ˈavəris/",
    "origin": "From Latin 'avaritia' meaning 'greed', from 'avarus' (greedy), from 'avere' (to desire).",
    "useCases": [
      {"context": "Behavior", "example": "His avarice led him to exploit his workers."},
      {"context": "Character", "example": "The character's avarice was his tragic flaw."}
    ],
    "feeling": "Greedy, covetous, and insatiable. This word suggests excessive desire for wealth."
  },
  {
    "word": "Banal",
    "pronunciation": "/bəˈnal/",
    "origin": "From French 'banal' meaning 'commonplace', from 'ban' (proclamation, ban). Originally referred to something subject to feudal service.",
    "useCases": [
      {"context": "Conversation", "example": "The meeting was filled with banal small talk."},
      {"context": "Writing", "example": "The author's banal prose lacked originality."}
    ],
    "feeling": "Commonplace, trite, and unoriginal. This word suggests something lacking freshness or originality."
  },
  {
    "word": "Bellicose",
    "pronunciation": "/ˈbeləˌkōs/",
    "origin": "From Latin 'bellicosus' meaning 'warlike', from 'bellum' (war).",
    "useCases": [
      {"context": "Foreign policy", "example": "The bellicose rhetoric increased tensions between nations."},
      {"context": "Personality", "example": "His bellicose nature made him quick to argue."}
    ],
    "feeling": "Aggressive, warlike, and combative. This word suggests a readiness to fight or quarrel."
  },
  {
    "word": "Benevolent",
    "pronunciation": "/bəˈnevələnt/",
    "origin": "From Latin 'benevolens' meaning 'wishing well', from 'bene' (well) + 'volens' (wishing).",
    "useCases": [
      {"context": "Character", "example": "The benevolent king was loved by his subjects."},
      {"context": "Actions", "example": "Her benevolent gesture helped many families."}
    ],
    "feeling": "Kind, generous, and well-meaning. This word conveys genuine care and goodwill."
  },
  {
    "word": "Benign",
    "pronunciation": "/bəˈnīn/",
    "origin": "From Latin 'benignus' meaning 'kind, friendly', from 'bene' (well) + 'genus' (born).",
    "useCases": [
      {"context": "Medical", "example": "The doctor confirmed the tumor was benign."},
      {"context": "Nature", "example": "The benign climate was perfect for growing crops."}
    ],
    "feeling": "Gentle, kind, and harmless. This word suggests something mild and not threatening."
  },
  {
    "word": "Boisterous",
    "pronunciation": "/ˈboist(ə)rəs/",
    "origin": "From Middle English 'boistous' meaning 'rough, coarse', possibly from Old French 'boisteus' (lame, limping).",
    "useCases": [
      {"context": "Behavior", "example": "The boisterous children ran through the park."},
      {"context": "Atmosphere", "example": "The boisterous celebration lasted all night."}
    ],
    "feeling": "Loud, energetic, and rowdy. This word suggests noisy, energetic, and cheerful behavior."
  },
  {
    "word": "Bombastic",
    "pronunciation": "/bämˈbastik/",
    "origin": "From 'bombast', meaning 'cotton padding' used to stuff clothing, hence inflated language.",
    "useCases": [
      {"context": "Speech", "example": "The politician's bombastic rhetoric failed to impress voters."},
      {"context": "Writing", "example": "The author's bombastic style overwhelmed the simple story."}
    ],
    "feeling": "Pompous, inflated, and grandiose. This word suggests overblown, pretentious language."
  },
  {
    "word": "Bucolic",
    "pronunciation": "/byo͞oˈkälik/",
    "origin": "From Greek 'boukolikos' meaning 'pastoral', from 'boukolos' (cowherd), from 'bous' (cow).",
    "useCases": [
      {"context": "Setting", "example": "The bucolic countryside provided a peaceful retreat."},
      {"context": "Literature", "example": "The poet wrote bucolic verses about rural life."}
    ],
    "feeling": "Rural, pastoral, and idyllic. This word suggests the peaceful charm of country life."
  },
  {
    "word": "Cacophonous",
    "pronunciation": "/kəˈkäfənəs/",
    "origin": "From Greek 'kakophonia' meaning 'bad sound', from 'kakos' (bad) + 'phone' (sound).",
    "useCases": [
      {"context": "Sound", "example": "The cacophonous orchestra rehearsal was hard to endure."},
      {"context": "City", "example": "The cacophonous city streets were overwhelming."}
    ],
    "feeling": "Harsh, discordant, and jarring. This word suggests unpleasant, discordant sounds."
  },
  {
    "word": "Calamitous",
    "pronunciation": "/kəˈlamətəs/",
    "origin": "From Latin 'calamitosus' meaning 'disastrous', from 'calamitas' (disaster, misfortune).",
    "useCases": [
      {"context": "Events", "example": "The calamitous earthquake destroyed the city."},
      {"context": "Consequences", "example": "The decision had calamitous effects on the economy."}
    ],
    "feeling": "Disastrous, catastrophic, and tragic. This word suggests severe misfortune or disaster."
  },
  {
    "word": "Callous",
    "pronunciation": "/ˈkaləs/",
    "origin": "From Latin 'callosus' meaning 'hard-skinned', from 'callus' (hard skin).",
    "useCases": [
      {"context": "Emotion", "example": "His callous remarks hurt many people."},
      {"context": "Behavior", "example": "The callous treatment of workers sparked protests."}
    ],
    "feeling": "Unfeeling, insensitive, and hard-hearted. This word suggests emotional hardness or indifference."
  },
  {
    "word": "Candor",
    "pronunciation": "/ˈkandər/",
    "origin": "From Latin 'candor' meaning 'whiteness, brightness, sincerity', from 'candere' (to shine, be white).",
    "useCases": [
      {"context": "Communication", "example": "Her candor in the interview was refreshing."},
      {"context": "Honesty", "example": "I appreciate your candor about the situation."}
    ],
    "feeling": "Honest, open, and frank. This word suggests sincere, straightforward expression."
  },
  {
    "word": "Capricious",
    "pronunciation": "/kəˈpriSHəs/",
    "origin": "From Italian 'capriccioso' meaning 'whimsical', possibly from 'capo' (head) + 'riccio' (hedgehog).",
    "useCases": [
      {"context": "Weather", "example": "The capricious weather changed from sunny to stormy."},
      {"context": "Decision-making", "example": "Her capricious choices made planning difficult."}
    ],
    "feeling": "Unpredictable, whimsical, and changeable. This word suggests sudden, unpredictable changes."
  },
  {
    "word": "Cathartic",
    "pronunciation": "/kəˈTHärdik/",
    "origin": "From Greek 'katharsis' meaning 'cleansing, purging', from 'kathairein' (to cleanse).",
    "useCases": [
      {"context": "Emotion", "example": "Writing about the experience was cathartic."},
      {"context": "Art", "example": "The play provided a cathartic experience for the audience."}
    ],
    "feeling": "Cleansing, purging, and emotionally releasing. This word suggests emotional relief or purification."
  },
  {
    "word": "Caustic",
    "pronunciation": "/ˈkôstik/",
    "origin": "From Greek 'kaustikos' meaning 'burning', from 'kaiein' (to burn).",
    "useCases": [
      {"context": "Criticism", "example": "Her caustic remarks offended many listeners."},
      {"context": "Humor", "example": "His caustic wit was both admired and feared."}
    ],
    "feeling": "Sarcastic, biting, and corrosive. This word suggests sharp, harsh criticism or wit."
  },
  {
    "word": "Clandestine",
    "pronunciation": "/klanˈdestən/",
    "origin": "From Latin 'clandestinus' meaning 'secret', from 'clam' (secretly).",
    "useCases": [
      {"context": "Meetings", "example": "The rebels held clandestine meetings at night."},
      {"context": "Operations", "example": "The spy engaged in clandestine activities."}
    ],
    "feeling": "Secret, hidden, and furtive. This word suggests something done in secret."
  },
  {
    "word": "Cogent",
    "pronunciation": "/ˈkōjənt/",
    "origin": "From Latin 'cogens' meaning 'compelling', from 'cogere' (to compel, force together).",
    "useCases": [
      {"context": "Arguments", "example": "She presented a cogent argument that convinced everyone."},
      {"context": "Reasoning", "example": "His cogent analysis clarified the complex issue."}
    ],
    "feeling": "Convincing, compelling, and clear. This word suggests clear, logical, and persuasive reasoning."
  },
  {
    "word": "Commensurate",
    "pronunciation": "/kəˈmensərət/",
    "origin": "From Latin 'commensuratus' meaning 'measured together', from 'com-' (with) + 'mensura' (measure).",
    "useCases": [
      {"context": "Compensation", "example": "The salary should be commensurate with experience."},
      {"context": "Response", "example": "The punishment must be commensurate with the crime."}
    ],
    "feeling": "Proportional, corresponding, and appropriate. This word suggests proper proportion or equivalence."
  }
]

# Read existing words
with open('words.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

# Add new words (avoiding duplicates)
existing_words = {w['word'].lower() for w in words}
new_words = [w for w in additional_words if w['word'].lower() not in existing_words]

# Create a comprehensive list (I'll need to add more words in subsequent runs or expand this script)
# For now, let's add what we have and note we need more
words.extend(new_words)

print(f"Added {len(new_words)} new words. Total now: {len(words)}")
print(f"Still need {300 - len(words)} more words to reach 300")

# Save updated file
with open('words.json', 'w', encoding='utf-8') as f:
    json.dump(words, f, indent=2, ensure_ascii=False)

print("File updated successfully!")

