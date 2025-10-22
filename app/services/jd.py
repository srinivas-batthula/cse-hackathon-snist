# app/services/jd.py
import re
from difflib import get_close_matches
from typing import List, Dict
import spacy
from spacy.matcher import PhraseMatcher
from data.skills import LEARNING_PATH_DB
from data.skills import SKILL_ORDER


def extract_skills_from_jd(jd_text: str) -> List[str]:
    KNOWN_SKILLS = list(LEARNING_PATH_DB.keys())
    
    nlp = spacy.load("en_core_web_sm")
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    patterns = [nlp.make_doc(skill) for skill in KNOWN_SKILLS]
    matcher.add("SKILLS", patterns)
    
    doc = nlp(jd_text)
    matches = matcher(doc)
    extracted = set()
    for match_id, start, end in matches:
        span = doc[start:end]
        extracted.add(span.text)
    return list(extracted)


def reorder_skills(skills: list[str]) -> list[str]:
    """
    Reorders extracted skills based on a predefined learning order.
    """
    order_map = {skill: i for i, skill in enumerate(SKILL_ORDER)}
    
    def sort_key(skill):
        return order_map.get(skill.lower(), len(SKILL_ORDER))  # Unmatched skills go last

    return sorted(skills, key=sort_key)


def generate_learning_path(extracted_keywords: List[str]) -> List[Dict[str, List[str]]]:
    path = []

    matched_skills = map_to_known_skills(extracted_keywords)

    for skill in matched_skills:
        content = LEARNING_PATH_DB.get(skill)
        if content:
            path.append({
                "skill": skill,
                "content": content
            })
    return path


def normalize(text: str) -> str:
    return re.sub(r"[^a-zA-Z0-9+.# ]", "", text).lower().strip()

def map_to_known_skills(extracted: List[str]) -> List[str]:
    """
    Try to map extracted keywords to known LEARNING_PATH_DB skills
    using 'fuzzy matching'.
    """
    known_skills = list(LEARNING_PATH_DB.keys())
    matched_skills = []

    for phrase in extracted:
        norm_phrase = normalize(phrase)

        # Try fuzzy match (threshold = 0.75 similarity)
        match = get_close_matches(norm_phrase, [normalize(skill) for skill in known_skills], n=1, cutoff=0.7)
        if match:
            # Map back to original skill casing
            original = next((s for s in known_skills if normalize(s) == match[0]), None)
            if original and original not in matched_skills:
                matched_skills.append(original)

    return matched_skills
