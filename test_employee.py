from employee import employee_details

def test_employee_details():
    result = employee_details("Rohan", "EMP101", "IT", "50000")

    expected = "Name: Rohan\nEmployee ID: EMP101\nDepartment: IT\nSalary: 50000"

    assert result == expected