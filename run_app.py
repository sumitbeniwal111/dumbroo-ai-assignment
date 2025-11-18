import streamlit.web.bootstrap
import sys

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "src/ui_streamlit.py"]
    streamlit.web.bootstrap.run("src/ui_streamlit.py", "", [], {})
