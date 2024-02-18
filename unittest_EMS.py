import unittest
from employeeManagementSystem import EMS, Employee


class TestEMS(unittest.TestCase):

    def setUp(self):
        self.ems = EMS()

    def test_add_employee(self):
        emp = Employee("Ali", 21, 1, "Software Engineer")
        self.ems.addNewEmployee("Ali", 21, "Software Engineer")
        self.assertEqual(self.ems.getEmployeeInfo(1), emp, True)

    def test_remove_employee(self):
        emp = Employee("Ali", 21, 1, "Software Engineer")
        self.ems.addNewEmployee("Ali", 21, "Software Engineer")
        self.ems.deleteEmployeeInfo(1)
        self.assertIsNone(self.ems.getEmployeeInfo(1), True)

    def test_get_employee(self):
        emp = Employee("Ali", 21, 1, "Software Engineer")
        self.ems.addNewEmployee("Ali", 21, "Software Engineer")
        self.assertEqual(self.ems.getEmployeeInfo(1), emp, True)


if __name__ == "__main__":
    unittest.main()
