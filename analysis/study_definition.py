from databuilder import codelist, table


class Cohort:
    population = table("patients").exists()
    dob = table("patients").first_by("patient_id").get("date_of_birth")
    age = table("patients").age_as_of("2020-01-01")
    prescribed_med = (
        table("prescriptions")
        .filter("processing_date", between=["2020-01-01", "2020-01-31"])
        .filter(
            "prescribed_dmd_code", is_in=codelist(["0010", "0050"], system="dmd")
        )
        .exists()
    )
    admitted = (
        table("hospital_admissions")
        .filter("admission_date", between=["2020-01-01", "2020-01-31"])
        .filter(primary_diagnosis="N05", episode_is_finished=True)
        .filter("admission_method", between=[20, 29])
        .exists()
    )
