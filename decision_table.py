def register_course(cgpa, prerequisites, seats,
                    course_count, already_registered, hold):

    if cgpa < 2.00 or cgpa > 4.00:
        return "Rejected"

    if not prerequisites:
        return "Rejected"

    if seats < 1:
        return "Rejected"

    if course_count < 1 or course_count > 6:
        return "Rejected"

    if already_registered:
        return "Rejected"

    if hold:
        return "Rejected"

    return "Registration Successful"
