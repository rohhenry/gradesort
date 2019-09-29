import re
from os import listdir

#CONSTANTS:
MAX_YEAR_LEVEL = 2
MIN_YEAR_LEVEL = 2
MIN_AVERAGE = 0

def requirements(info):
    if info[0] == "UBC" and info[6] == "OVERALL" and re.match("\d+.*", info[10]) is not None:
        average = float(info[10])
        class_code = int(info[4])
        return MIN_YEAR_LEVEL * 100 <= class_code <= (MAX_YEAR_LEVEL + 1) * 100 and average >= MIN_AVERAGE
    else:
        return 0

if __name__ == "__main__":
    courses = []
    for f in listdir("dataset"):
        with open("dataset/" + f, "r") as course_file:
            for line in course_file:
                course = []
                info = line.split(",")
                if "\"" in info[7] and "\"" in info[8] and "\"" in info[9]:
                    info[7] = info[7]+ info[8]
                    info.pop(8)
                if requirements(info):
                    course = [info[3]] + [info[4]] + [float(info[10])]
                    courses.append(course)

courses.sort(key=lambda course: course[2], reverse=1)

with open("output.txt", "w") as output_file:
    for c in courses:
        output_file.write("{0} {1}: {2}\n".format(c[0], c[1], c[2]))