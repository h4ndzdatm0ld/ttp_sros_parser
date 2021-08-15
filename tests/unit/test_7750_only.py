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
