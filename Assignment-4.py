class Department:
    count = 0
    def __init__(self, deptname, deptid, loc, hodname):
        self.deptname = deptname
        self.deptid = deptid
        self.loc = loc
        self.hodname = hodname
        Department.count += 1
    def display_department_info(self):
        print("Department Information:")
        print("-" * 30)
        print(f"Department ID : {self.deptid}")
        print(f"Department Name   : {self.deptname}")
        print(f"Location        : {self.loc}")
        print(f"HOD Name        : {self.hodname}")
        print("-" * 30)
    @classmethod
    def get_total_departments(cls):
        return cls.count
no_of_dept = int(input("Enter number of departments: "))
departments_by_name = {}
departments_by_id = {}
for i in range(no_of_dept):
    print(f"\nEnter details for Department {i + 1}:")
    dept_id = int(input("Enter Department ID: "))
    name = input("Enter Department Name: ")
    location = input("Enter Location: ")
    hod = input("Enter HOD Name: ")
    dept = Department(name, dept_id, location, hod)
    departments_by_name[name] = dept
    departments_by_id[dept_id] = dept
print("\n--- All Department Information ---")
for dept in departments_by_name.values():
    dept.display_department_info()
search_name = input("\nEnter Department Name to search: ").lower()
found = False
for name, dept in departments_by_name.items():
    if search_name in name:
        print("\nMatching Department Found (by name):")
        dept.display_department_info()
        found = True
if not found:
    print("Department not found with the given name criteria.")
search_id_input = input("\nEnter Department ID to search: ")
if search_id_input.isdigit():
    search_id = int(search_id_input)
    if search_id in departments_by_id:
        print("\nMatching Department Found (by ID):")
        departments_by_id[search_id].display_department_info()
    else:
        print("Department not found with the given ID.")
else:
    print("Invalid ID entered. Please enter a numeric value.")
print(f"\nTotal Departments in Organization: {Department.get_total_departments()}")
