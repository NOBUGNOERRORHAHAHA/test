import pytest
import logging
from six.moves import input


def execute_manual_step(info):
    # Pauses test execution until user sets the step status.
    print(("[MANUAL STEP INFO] %s" % info))
    capture_manager = pytest.config.pluginmanager.getplugin('capturemanager')
    capture_manager.suspend_global_capture(in_=True)

    while True:
        result = input('Result:').lower()

        if result in ['fail', 'block']:
            comments = input('Comments:')
            if comments:
                break
        elif result in ['pass']:
            break

    capture_manager.resume_global_capture()

    if result == 'fail':
        logging.warning(comments)
        pytest.fail(comments)
    elif result == 'block':
        logging.warning(comments)
        pytest.skip(comments)

def execute_manual_input(info):
    # Pauses test execution until user input the value.
    print(("[MANUAL INPUT INFO] %s" % info))
    capture_manager = pytest.config.pluginmanager.getplugin('capturemanager')
    capture_manager.suspend_global_capture(in_=True)

    result = input('Input:')

    return result
