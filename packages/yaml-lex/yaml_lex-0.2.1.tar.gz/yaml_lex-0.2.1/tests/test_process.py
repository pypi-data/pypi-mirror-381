import pytest

from yaml_lex import process_node


@pytest.mark.parametrize(
    "data,char_limit,expected_substr",
    [
        ({"caption": "A very long caption that should wrap"}, 20, "wrap"),
        ({"content": "Some very long content that must wrap nicely"}, 15, "content"),
    ],
)
def test_process_node_dict(data, char_limit, expected_substr):
    processed = process_node(data, char_limit=char_limit)
    assert expected_substr in processed[list(data.keys())[0]]
    assert "\n" in processed[list(data.keys())[0]]


@pytest.mark.parametrize(
    "data,char_limit,expected_substr",
    [
        (["Short", "This is a long string"], 10, "This"),
        (["Another short one", "Another very very long string"], 12, "long"),
    ],
)
def test_process_node_list(data, char_limit, expected_substr):
    processed = process_node(data, char_limit=char_limit)
    assert any(expected_substr in str(item) for item in processed)


@pytest.mark.parametrize(
    "scalar,char_limit,expected_in",
    [
        ("This is a very long string", 10, "This"),
        ("Another quite lengthy example string", 15, "example"),
    ],
)
def test_process_node_scalar(scalar, char_limit, expected_in):
    result = process_node(scalar, parent_key=None, char_limit=char_limit)
    assert expected_in in str(result)
    assert "\n" in str(result)
