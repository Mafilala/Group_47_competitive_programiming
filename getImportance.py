class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        importance = 0
        employees_with_id = [-1 for _ in range(2001)] 
        for employee in employees:
            i = employee.id
            if employee.id == id:
                root = employee
            employees_with_id[i] = employee
        def dfs(emp):
            nonlocal importance
            importance += emp.importance
            for sub_id in emp.subordinates:
                new_emp = employees_with_id[sub_id]
                dfs(new_emp)
        
        dfs(root)
        return importance
