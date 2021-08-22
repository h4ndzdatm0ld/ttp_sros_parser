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
