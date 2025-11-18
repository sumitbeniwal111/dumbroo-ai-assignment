from src.auth import Admin
from src.main import run_query_for_admin

def print_df(df):
    if df.empty:
        print("(no rows)")
    else:
        print(df.to_string(index=False))

def main():
    admin = Admin(admin_id=1, name="Ravi", scope={"grade": 8, "class": "A", "region": "North"})
    examples = [
        "Which students haven't submitted their homework yet?",
        "Show me performance data for Grade 8 from last week",
        "List all upcoming quizzes scheduled for next week",
        "List students in grade 9",
    ]
    for q in examples:
        print("="*80)
        print("Q:", q)
        df, parsed, note = run_query_for_admin(admin, q)
        print("Parsed:", parsed)
        print("Note:", note)
        print("Results:")
        print_df(df)
    print("="*80)

if __name__ == "__main__":
    main()
