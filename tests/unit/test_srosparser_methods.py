"""Test available methods and generate an update to the readmedocs."""


def test_methods(sros_parser_7750):
    """
    Test extracting methods from class.
    """
    methods = [m for m in dir(sros_parser_7750) if m.startswith(("show", "get"))]
    with open("docs/methods.md", "w") as methd:
        methd.write("```" + "\n")
        for x in methods:
            methd.write(f"{x}\n")
        methd.write("```" + "\n")

    assert len(methods) == 56
