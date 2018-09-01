"""Module for transmitting information between widgets."""
from PyQt5.QtCore import QObject, pyqtSignal


class Signals(QObject):
    """
    This is a signal. It has connect and emit methods.
    Usage:

    Suppose there is a function my_fun which takes a DecisionSceneData object
    as input.
    Then:

    load_decision_scene.connect(my_fun)
    links this signal to that function.

    When load_decision_scene.emit(data) is invoked,
    this calls my_fun(data).
    I.e. a signal is sent out containing data, and is received by my_fun.


    """
    # We would pass DecisionSceneData instead of object, but this causes
    # circular import issues.
    load_decision_scene = pyqtSignal(object)
