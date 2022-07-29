from sample.lambda_function import get_instances

def test_get_instances(load_env):
    assert get_instances() == "foo"


