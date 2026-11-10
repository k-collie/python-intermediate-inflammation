from unittest.mock import Mock


def test_analyse_data_mock_source():
    from inflammation.compute_data import analyse_data

    data_source = Mock()
    # configure data_source mock
    mock_data = [[[0, 2, 0]], [[0, 1, 0]]]
    data_source.load_inflammation_data.return_value = mock_data

    analyse_data(data_source)
