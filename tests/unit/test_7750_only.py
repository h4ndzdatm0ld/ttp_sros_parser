"""Test specific 7750 configurations."""


def test_get_connectors(sros_parser_7750, parsed_connectors):
    """
    Test extracting connector ports.
    """
    result = sros_parser_7750.get_connectors()
    assert result == parsed_connectors


def test_get_lags(sros_parser_7750, parsed_lags):
    """
    Test extracting connector ports.
    """
    result = sros_parser_7750.get_lags()
    assert result == parsed_lags


def test_get_lsps(sros_parser_7750_R3, parsed_lsps):
    """
    Test extracting MPLS LSPs.
    """
    result = sros_parser_7750_R3.get_lsps()
    assert result == parsed_lsps


def test_get_lags_group2(sros_parser_7750_R2, parsed_lags_1):
    """
    Test extracting connector ports.
    """
    result = sros_parser_7750_R2.get_lags()
    assert result == parsed_lags_1
    assert len(result["configure"]["lag"]) == 6
    assert result["configure"]["lag"][5]["name"] == "myLag105"


# add testting for get_python_declaration_configuration
def test_get_python_declaration_configuration(sros_parser_7750, parsed_python_declaration):
    """
    Test extracting python declaration configuration.
    """
    result = sros_parser_7750.get_python_declaration_configuration()
    assert result == parsed_python_declaration


# add testting for get_python_configuration
def test_get_python_configuration(sros_parser_7750, parsed_python_configuration):
    """
    Test extracting python configuration.
    """
    result = sros_parser_7750.get_python_configuration()
    assert result == parsed_python_configuration
