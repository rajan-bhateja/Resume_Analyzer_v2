#!/usr/bin/env python
import traceback
import warnings

from resume_analyzer_v3.crew import ResumeAnalyzerV3

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        "resume": r"C:\Users\rajan\OneDrive\Desktop\Rajan_Bhateja_Resume_Jul25.pdf"
    }

    try:
        ResumeAnalyzerV3().crew().kickoff(inputs=inputs)
    except Exception as e:
        print("Full traceback:")
        traceback.print_exc()
        raise Exception(f"An error occurred while running the crew: {str(e)}")