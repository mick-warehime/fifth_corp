import os
from typing import List
from subprocess import call

PYQT_DIRECTORY = '../pyqt'


def find_ui_files() -> List[str]:
    ui_files = []
    for file in os.listdir(PYQT_DIRECTORY):
        if file.endswith(".ui"):
            ui_files.append(os.path.join(PYQT_DIRECTORY, file))
    return ui_files


def output_name(ui_file: str) -> str:
    return ui_file[:-3] + '_form.py'


def compile_ui() -> None:
    ui_files = find_ui_files()
    output_files = [output_name(f) for f in ui_files]
    for ui, output in zip(ui_files, output_files):
        call(['pyuic5', ui, '-o', output])


if __name__ == '__main__':
    compile_ui()
