import pytest

def setup_function():
    print("\n=== 测试开始：初始化环境 ===")


def test_simple_assertion():
    assert 1 + 1 == 2

def teardown_function():
    print("\n=== 测试结束：清理环境 ===")