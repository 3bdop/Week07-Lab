import unittest
from employeeManagementSystem import EMS, Employee


class TestEMS(unittest.TestCase):

    def setUp(self):
        self.ems = EMS()

    def test_add_employee(self):
        emp = Employee("Ali", 21, 1, "IT")
        self.ems.addNewEmployee("1", "Ali", "21", "IT")
        added_emp = self.ems.getEmployeeInfo("1")
        self.assertEqual(
            (added_emp.name, added_emp.age, added_emp.id, added_emp.department),
            (emp.name, emp.age, emp.id, emp.department),
        )

    def test_remove_employee(self):
        emp = Employee("Ali", 21, 1, "IT")
        self.ems.addNewEmployee("1", "Ali", "21", "IT")
        self.ems.deleteEmployeeInfo("1")
        try:
            self.ems.getEmployeeInfo("1")
        except ValueError:
            pass
        else:
            self.fail("ValueError not raised")

    def test_get_employee(self):
        emp = Employee("Abood", 21, 3, "IT")
        self.ems.addNewEmployee("3", "Abood", "21", "IT")
        added_emp = self.ems.getEmployeeInfo("3")
        self.assertEqual(
            (added_emp.name, added_emp.age, added_emp.id, added_emp.department),
            (emp.name, emp.age, emp.id, emp.department),
        )


if __name__ == "__main__":
    unittest.main()
