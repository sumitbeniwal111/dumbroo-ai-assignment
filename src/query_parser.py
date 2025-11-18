import re
from datetime import datetime, timedelta
import dateparser

def week_range_from(when: str):
    today = datetime.now().date()
    weekday = today.weekday()
    this_monday = today - timedelta(days=weekday)

    if when == "next":
        start = this_monday + timedelta(weeks=1)
    elif when == "last":
        start = this_monday - timedelta(weeks=1)
    else:
        start = this_monday

    return start, start + timedelta(days=6)

def parse_date_phrase(phrase: str):
    phrase = phrase.lower()

    if "next week" in phrase:
        return week_range_from("next")
    if "last week" in phrase:
        return week_range_from("last")

    return None

def rule_based_parse(question: str):
    q = question.lower()

    parsed = {
        "intent": "list",
        "target": None,
        "filters": [],
        "date_range": None,
        "note": ""
    }

    if "haven't submitted" in q or "not submitted" in q:
        parsed["target"] = "homework"
        parsed["filters"].append({"field": "homework_submitted", "op": "=", "value": False})
        return parsed

    if "quiz" in q:
        parsed["target"] = "quiz"
        parsed["date_range"] = parse_date_phrase(q)
        return parsed

    if "grade" in q:
        g = re.search(r"grade\s*(\d+)", q)
        if g:
            parsed["target"] = "performance"
            parsed["filters"].append({"field": "grade", "op": "=", "value": int(g.group(1))})
            parsed["date_range"] = parse_date_phrase(q)
            return parsed

    parsed["note"] = "fallback"
    return parsed

def parse_question(question: str, use_llm=False, llm_fn=None):
    return rule_based_parse(question)
