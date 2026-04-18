import random
import json

# Original student entries
students = [
    {
        "name": "Amina",
        "country": "Nigeria",
        "field": "Computer Science",
        "level": "Bachelor",
        "language": "English",
        "budget": 5000,
        "grades": "A",
    },
    # ... (other original student entries)
]

# Original university entries
universities = [
    {
        "name": "University of Helsinki",
        "country": "Finland",
        "field": "Computer Science",
        "level": "Bachelor",
        "language": "English",
        "tuition": 0,
        "rank": 120,
        "requirements": "Grades A, IELTS 6.5+",
    },
    # ... (other original university entries)
]

# Configuration for data generation
random.seed(42)  # For reproducibility

# ========================
# STUDENT GENERATION (1000 total)
# ========================
student_countries = ['Nigeria', 'India', 'Spain', 'USA', 'Japan', 'Italy',
                    'China', 'Germany', 'Brazil', 'France', 'Canada', 'Mexico']
student_fields = ['Computer Science', 'Business', 'Law', 'Engineering',
                 'Medicine', 'Arts', 'Physics', 'Education', 'Mathematics']
student_levels = ['Bachelor', 'Master', 'PhD']
student_grades = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']

country_language_map = {
    'Nigeria': ['English', 'Hausa'],
    'India': ['Hindi', 'English'],
    'Spain': ['Spanish'],
    'USA': ['English'],
    'Japan': ['Japanese', 'English'],
    'Italy': ['Italian'],
    'China': ['Chinese'],
    'Germany': ['German', 'English'],
    'Brazil': ['Portuguese'],
    'France': ['French'],
    'Canada': ['English', 'French'],
    'Mexico': ['Spanish']
}

# Generate additional students
for _ in range(1000 - len(students)):
    country = random.choice(student_countries)
    level = random.choice(student_levels)
    
    # Language selection logic
    if country in country_language_map:
        lang_options = country_language_map[country]
        language = random.choice(lang_options + ['English']*(len(lang_options)+1))
    else:
        language = 'English'
    
    # Budget based on level and country
    base_budget = {
        'Bachelor': (4000, 15000),
        'Master': (8000, 25000),
        'PhD': (12000, 35000)
    }[level]
    budget = random.randint(*base_budget) * (1 + (country in ['USA', 'UK']))

    students.append({
        "name": f"Student_{len(students)+1}",
        "country": country,
        "field": random.choice(student_fields),
        "level": level,
        "language": language,
        "budget": budget,
        "grades": random.choice(student_grades),
    })

# ========================
# UNIVERSITY GENERATION (100 total)
# ========================
uni_countries = ['Finland', 'Sweden', 'USA', 'UK', 'Japan', 'Spain',
                'Germany', 'Canada', 'Australia', 'Netherlands', 'Switzerland']
uni_fields = ['Computer Science', 'Business', 'Law', 'Engineering',
             'Medicine', 'Arts', 'Architecture', 'Economics']
uni_levels = ['Bachelor', 'Master', 'PhD']

# Generate additional universities
for _ in range(100 - len(universities)):
    country = random.choice(uni_countries)
    level = random.choice(uni_levels)
    
    # Tuition calculation
    if country in ['USA', 'UK']:
        tuition = random.randint(15000, 50000)
    elif country in ['Germany', 'Finland']:
        tuition = random.randint(0, 2000)
    else:
        tuition = random.randint(5000, 25000)
    
    # Ranking and requirements
    rank = random.randint(1, 300)
    grade_req = 'A' if rank < 50 else 'B+' if rank < 150 else 'B'
    ielts_req = f"{random.uniform(6.0, 7.5):.1f}+" if rank < 100 else "6.0+"
    
    universities.append({
        "name": f"{country} University of {random.choice(['Technology', 'Science', 'Arts', 'Business'])}",
        "country": country,
        "field": random.choice(uni_fields),
        "level": level,
        "language": 'English' if random.random() > 0.3 else country_language_map.get(country, ['English'])[0],
        "tuition": tuition,
        "rank": rank,
        "requirements": f"Grades {grade_req}, IELTS {ielts_req}",
    })

# Saving the data to JSON files
with open('students_data.json', 'w') as students_file:
    json.dump(students, students_file, indent=4)

with open('universities_data.json', 'w') as universities_file:
    json.dump(universities, universities_file, indent=4)

# Final dataset sizes
print(f"Generated {len(students)} students and {len(universities)} universities")
print("Data saved to 'students_data.json' and 'universities_data.json'")
