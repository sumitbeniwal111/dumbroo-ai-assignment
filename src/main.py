from src.query_parser import parse_question
from src.query_executor import execute_parsed_query

def run_query_for_admin(admin, question):
    parsed = parse_question(question)
    return execute_parsed_query(admin, parsed)
