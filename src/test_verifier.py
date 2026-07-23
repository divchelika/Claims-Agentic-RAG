from src.services.verifier_service import VerifierService


def main():

    verifier = VerifierService()

    context = """
MRI requires pre-certification unless
ordered in an emergency department.
"""

    answer = (
        "MRI requires pre-certification unless ordered "
        "in an emergency department."
    )

    result = verifier.verify(
        question="Does MRI require preauthorization?",
        answer=answer,
        context=context,
    )

    print(result)


if __name__ == "__main__":
    main()