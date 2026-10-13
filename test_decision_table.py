from decision_table import register_course

def test_valid_registration():
    assert register_course(
        3.2, True, 10, 4, False, False
    ) == "Registration Successful"


def test_low_cgpa():
    assert register_course(
        1.8, True, 10, 4, False, False
    ) == "Rejected"


def test_missing_prerequisites():
    assert register_course(
        3.2, False, 10, 4, False, False
    ) == "Rejected"


def test_no_available_seats():
    assert register_course(
        3.2, True, 0, 4, False, False
    ) == "Rejected"
