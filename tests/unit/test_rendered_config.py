from tests.conftest import FIXTURES, SRC, confgen


def test_confgen_rendered_config():
    """Test that the rendered config is correct."""
    result = confgen(
        config_data=f"{FIXTURES}/data/example.yml", template_name="main.j2", directory_path=f"{SRC}/templates/general"
    )
