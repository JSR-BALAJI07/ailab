import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    return set(text.split())

def screen_resume(resume, job_description):
    resume_words = preprocess(resume)
    job_words = preprocess(job_description)

    matched = resume_words.intersection(job_words)
    missing = job_words - resume_words

    # Calculate percentage match
    score = (len(matched) / len(job_words)) * 100

    return matched, missing, score


# Job description
job_description = """
Python SQL Machine Learning Data Analysis Communication
Bachelor Programming Pandas NumPy
"""

# Candidate resume
resume = """
John Doe
Bachelor of Computer Science
Skills: Python, SQL, Machine Learning, Data Analysis,
Pandas, NumPy, Programming, Communication
"""

matched, missing, score = screen_resume(resume, job_description)

print("SMART AI RESUME SCREENING SYSTEM")
print("---------------------------------")

print("\nMatched Skills/Requirements:")
print(", ".join(sorted(matched)))

print("\nMissing Requirements:")
if missing:
    print(", ".join(sorted(missing)))
else:
    print("None")

print(f"\nResume Match Score: {score:.2f}%")

if score >= 70:
    print("Screening Result: Suitable for further review")
else:
    print("Screening Result: Requires further evaluation")

