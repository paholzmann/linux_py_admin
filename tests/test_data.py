import pytest
from src.data import GenerateUserData, FileHandler

"""
Unit tests
Integration tests
Exception tests
"""
class TestGenerateUserData:
    @classmethod
    def setup_class(cls):
        """
        
        """
        cls.generate_user_data = GenerateUserData()
        cls.file_handler = FileHandler()
        cls.input_data = [
            10,
            100,
            1000
        ]
        cls.invalid_input_data = [
            -10,
            0,
            "10"
        ]

        cls.ref_funcs = {
            "generate_users": lambda n: cls.generate_user_data.generate_users(n)
        }

    @pytest.mark.parametrize("func_name", [
        "generate_users"
    ])
    def test_data_outputs(self, func_name):
        """
        
        """
        func = getattr(self.generate_user_data, func_name)
        ref_func = self.ref_funcs[func_name]
        for n in self.input_data:
            output = func(n)
            expected = ref_func(n)
            assert len(output) == len(expected)
            assert type(output) == dict