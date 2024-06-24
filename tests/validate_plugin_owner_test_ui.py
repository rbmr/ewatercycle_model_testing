"""
module containing tests for the plugin owner test ui.
"""

import unittest

import pytest

from ewatercycle_model_testing.test import Test


# Some data fixtures for testing
@pytest.fixture
def test_groups1():
    """
    fixture to have test banks
    """
    return {
        "Spec Tests": [Test(name=f"Test {i}",
                            description=f"Description {i}",
                            critical=True,
                            enabled=False) for i in range(1, 6)],
        "Error Tests": [Test(name=f"Test {i}",
                             description=f"Description {i}",
                             critical=True,
                             enabled=True) for i in range(6, 11)],
        "Business Tests": [Test(name=f"Test {i}",
                                description=f"Description {i}",
                                critical=False,
                                enabled=True) for i in range(11, 16)]
    }

@pytest.fixture
def test_groups2():
    """
    fixture to have a group of tests
    """
    tests = [
        Test(name="Test 1", description="Description 1", critical=True, enabled=False),
        Test(name="Test 2", description="Description 2", critical=False, enabled=False),
        Test(name="Test 3", description="Description 3", critical=True, enabled=False),
    ]
    return {"Group 1": tests}


#Used only for manual testing of the UI, should be commented out by default
# 
# def validate_opens1(test_groups1):
#     root = ttk.Window(themename="darkly")
#     app = TestSelector(root, test_groups1)
#     root.mainloop()
#
# 
# def validate_opens2(test_groups2):
#     root = ttk.Window(themename="darkly")
#     app = TestSelector(root, test_groups2)
#     root.mainloop()

test_groups = {
    "Group 1": [Test(name=f"Test {i}",
                     description=f"Description {i}",
                     critical=True,
                     enabled=False) for i in range(1, 6)],
    "Group 2": [Test(name=f"Test {i}",
                     description=f"Description {i}",
                     critical=False,
                     enabled=False) for i in range(6, 11)],
    "Group 3": [Test(name=f"Test {i}",
                     description=f"Description {i}",
                     critical=True,
                     enabled=False) for i in range(11, 16)]
}

# Gitlab does not have window to open UI. Therefore these tests will throw an error.
# They are commented out so that the pipeline passes.
# class TestTestSelector(unittest.TestCase):
#     def setUp(self):
#         self.root = ttk.Window(themename="darkly")
#         self.selector = TestSelector(self.root, test_groups)
#
#     def validate_initial_state(self):
#         # Verify initial state
#         for group_name in self.selector.test_groups:
#             self.assertTrue(self.selector.check_vars[group_name].get())
#             for test in self.selector.test_groups[group_name]:
#                 self.assertEqual(self.selector.check_vars[test.name].get(),
#                                  test.enabled)
#
#     def validate_update_group_checks(self):
#         group_name = "Group 1"
#         self.selector.check_vars[group_name].set(False)
#         self.selector.update_group_checks(group_name)
#         for test in self.selector.test_groups[group_name]:
#             self.assertFalse(self.selector.check_vars[test.name].get())
#         self.selector.check_vars[group_name].set(True)
#         self.selector.update_group_checks(group_name)
#         for test in self.selector.test_groups[group_name]:
#             self.assertTrue(self.selector.check_vars[test.name].get())
#
#     @mock.patch.object(messagebox, 'showinfo')
#     def validate_run_selected_tests(self, mock_info):
#         self.selector.run_selected_tests()
#         mock_info.assert_called_once_with("No Tests Selected",
#                                           "No tests selected to run.")
#         self.assertFalse(self.selector.success)
#
#         self.selector.check_vars["Test 1"].set(True)
#         self.selector.check_vars["Test 6"].set(True)
#         self.selector.run_selected_tests()
#         mock_info.assert_called_with("Selected Tests",
#                                       "Running tests: Test 1, Test 6")
#         self.assertTrue(self.selector.success)
#
#     def validate_empty(self):
#         empty_test_groups = {}
#         root = ttk.Window(themename="darkly")
#         selector = TestSelector(root, empty_test_groups)
#         with mock.patch.object(messagebox, 'showinfo') as mock_info:
#             selector.run_selected_tests()
#             mock_info.assert_called_once_with("No Tests Selected",
#                                               "No tests selected to run.")
#             self.assertFalse(selector.success)
#         root.destroy()
#
#     def validate_empty_tests(self):
#         single_group_empty_tests = {"Group 1": []}
#         root = ttk.Window(themename="darkly")
#         selector = TestSelector(root, single_group_empty_tests)
#         with mock.patch.object(messagebox, 'showinfo') as mock_info:
#             selector.run_selected_tests()
#             mock_info.assert_called_once_with("No Tests Selected",
#                                               "No tests selected to run.")
#             self.assertFalse(selector.success)
#         root.destroy()


if __name__ == '__main__':
    unittest.main()
