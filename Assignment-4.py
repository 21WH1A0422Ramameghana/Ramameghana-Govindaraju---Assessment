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
        print("-" * 23)
        print(f"Department Name : {self.deptname}")
        print(f"Department ID   : {self.deptid}")
        print(f"Location        : {self.loc}")
        print(f"HOD Name        : {self.hodname}")
        print("-" * 30)
    @classmethod
    def get_total_departments(cls):
        return cls.count
no_of_dept = int(input("Enter number of departments: "))
departments = {}
for i in range(no_of_dept):
    print(f"\nEnter details for Department {i + 1}:")
    name = input("Enter Department Name: ")
    dept_id = int(input("Enter Department ID: "))
    location = input("Enter Location: ")
    hod = input("Enter HOD Name: ")
    dept = Department(name, dept_id, location, hod)
    departments[name.lower()] = dept
print("\n--- All Department Information ---")
for dept in departments.values():
    dept.display_department_info()
search_name = input("\nEnter Department Name to search: ")
found = False
for name, dept in departments.items():
    if (name.startswith(search_name) or 
        name.endswith(search_name) or 
        search_name in name):
        print("\nMatching Department Found:")
        dept.display_department_info()
        found = True
if not found:
    print("Department not found with the given name criteria.")
print(f"\nTotal Departments in Organization: {Department.get_total_departments()}")