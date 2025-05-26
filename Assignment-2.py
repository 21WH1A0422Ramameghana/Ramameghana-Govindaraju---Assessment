university_data = {
"S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

#Q1: Print all student names and their majors
for s in university_data.values():
    print(s["name"], "-", s["major"])

#Q2: Average score per course per student 
for s in university_data.values():
    print("\n", s["name"])
    for course, scores in s["courses"].items():
        avg = sum(scores.values()) / 3
        print(course, "Average:", avg)

#Q3: Find students who scored >90 in final of Python101
for s in university_data.values():
    if "Python101" in s["courses"]:
        if s["courses"]["Python101"]["final"] > 90:
            print(s["name"]) 

#Q4: Add new course AI101 for student S101
university_data["S101"]["courses"]["AI101"] = {
    "midterm": 75, "final": 98, "project": 92
}
print(university_data)

#Q5: Print average for each course
course = {}
for i in university_data.values():
    for i, j in i["courses"].items():
        avg = sum(j.values()) / 3
        if i in course:
            course[i].append(avg)
        else:
            course[i] = [avg]
for i, avgs in course.items():
    print(i, "Overall Average:", sum(avgs)/len(avgs))



