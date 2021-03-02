import pytest
import sprint_1


def test_task_1():
    sprint_1.task_1()
    result = open(task.FILE_INPUT_PATH, 'rb').read()
    expected = open(TEST_DATA_DIR / 'expected_1.pkl', 'rb').read()

