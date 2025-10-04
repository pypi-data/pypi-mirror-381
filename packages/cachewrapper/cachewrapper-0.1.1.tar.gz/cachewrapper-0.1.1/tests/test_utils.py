import unittest
from cachewrapper import utils
import os

# useful for debugging during development
try:
    from ipydex import IPS, activate_ips_on_exception

    activate_ips_on_exception()
except ImportError:
    pass

class TestCore(unittest.TestCase):

    def test_u01(self):
        # Test dict_converter_factory

        # Create custom dict classes for testing
        class SourceDict(dict):
            pass

        class TargetDict(dict):
            pass

        # Create converter
        converter = utils.dict_converter_factory(SourceDict, TargetDict)

        # Test basic conversion
        source_obj = SourceDict({'a': 1, 'b': 2})
        result = converter(source_obj)

        self.assertIsInstance(result, TargetDict)
        self.assertEqual(result, {'a': 1, 'b': 2})
        self.assertNotIsInstance(result, SourceDict)

        # Test nested conversion
        nested_source = SourceDict({
            'outer': SourceDict({'inner': 3}),
            'list': [SourceDict({'item': 4})],
            'regular_dict': {'normal': 5},
            'string': "foo",
            'int': 123,
            'float': 123.0,
        })

        nested_result = converter(nested_source)

        self.assertIsInstance(nested_result, TargetDict)
        self.assertIsInstance(nested_result['outer'], TargetDict)
        self.assertIsInstance(nested_result['list'][0], TargetDict)
        self.assertIsInstance(nested_result['regular_dict'], dict)
        self.assertIsInstance(nested_result['string'], str)
        self.assertIsInstance(nested_result['int'], int)
        self.assertIsInstance(nested_result['float'], float)
        self.assertNotIsInstance(nested_result['regular_dict'], TargetDict)

        # Test non-dict objects are unchanged
        non_dict = "string"
        self.assertEqual(converter(non_dict), "string")
