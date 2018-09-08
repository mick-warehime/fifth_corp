"""Tests for scene_library.py."""
import pytest

from controller.main_window_controller import MainWindow
from model.scene_library import example_scenes_and_resolutions
import app

app.initialize_globals()


def test_scene_library_missing_scene(qtbot):
    main = MainWindow()

    with pytest.raises(KeyError, match='missing'):
        main.library.get_scene_data('missing')


def test_scene_library_missing_resolution(qtbot):
    main = MainWindow()

    with pytest.raises(KeyError, match='missing'):
        main.library.get_resolution_data('missing')


def test_get_scene():
    scene_dict, _ = example_scenes_and_resolutions()
    scene_name = 'scene_1'
    assert scene_name in scene_dict

    scene_data = MainWindow().library.get_scene_data(scene_name)

    assert scene_data == scene_dict[scene_name]


def test_get_resolution():
    _, res_dict = example_scenes_and_resolutions()
    res_name = 'res_0'
    assert res_name in res_dict

    res_data = MainWindow().library.get_resolution_data(res_name)

    assert res_data == res_dict[res_name]
