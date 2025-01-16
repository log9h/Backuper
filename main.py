import sys
import os
import zipfile
import time

from typing import List

from PyQt5 import QtWidgets

import design  # .py QtDesigner ui


class Backuper(QtWidgets.QMainWindow, design.Ui_MainWindow):
    ProcessLabelSuccessCSS = (
        'border: 1.5px solid #5cb85c;'
        'border-radius: 5px;'
        'color: #5cb85c;'
    )
    ProcessLabelDangerCSS = (
        'border: 1.5px solid #d9534f;'
        'border-radius: 5px;'
        'color: #d9534f;'
    )
    ProcessLabelWarningCSS = (
        'border: 1.5px solid #f0ad4e;'
        'border-radius: 5px;'
        'color: #f0ad4e;'
    )

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.source_folder = ''
        self.target_folder = ''

        self.BackupFolderButton.clicked.connect(self.browse_backup_folder)
        self.TargetFolderButton.clicked.connect(self.browse_target_folder)
        self.BackupButton.clicked.connect(self.create_backup)

    def browse_backup_folder(self) -> None:
        self.source_folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Browse backup folder")

        if self.source_folder:
            self.ProcessLabel.setStyleSheet(self.ProcessLabelSuccessCSS)
            label_text = 'Backup Folder Selected'
        else:
            self.ProcessLabel.setStyleSheet(self.ProcessLabelWarningCSS)
            label_text = 'You canceled the operation'
        self.ProcessLabel.setText(label_text)

    def browse_target_folder(self) -> None:
        self.target_folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Browse target folder")

        if self.target_folder:
            self.ProcessLabel.setStyleSheet(self.ProcessLabelSuccessCSS)
            label_text = 'Target Folder Selected'
        else:
            self.ProcessLabel.setStyleSheet(self.ProcessLabelWarningCSS)
            label_text = 'You canceled the operation'
        self.ProcessLabel.setText(label_text)

    @staticmethod
    def get_all_file_paths(source: str) -> List[str]:
        filepaths = []
        for root, dirs, files in os.walk(source):
            for filename in files:
                filepath = os.path.join(root, filename)
                filepaths.append(filepath)
        return filepaths

    def create_backup(self) -> None:
        if not (self.source_folder and self.target_folder):
            self.ProcessLabel.setStyleSheet(self.ProcessLabelDangerCSS)
            self.ProcessLabel.setText('You didn\'t select necessary folders')
            return

        today = self.target_folder + os.sep + time.strftime('%Y.%m.%d')

        if not os.path.exists(today):
            os.mkdir(today)

        target = today + os.sep + time.strftime('%H%M%S') + \
            self.CommentLineEdit.text().replace(' ', '_') + '.zip'
        file_paths = self.get_all_file_paths(self.source_folder)

        with zipfile.ZipFile(target, 'w') as zip_w:
            for file in file_paths:
                zip_w.write(file)
        self.ProcessLabel.setStyleSheet(self.ProcessLabelSuccessCSS)

        zip_size = os.path.getsize(target)
        if (size_mb := round(zip_size / 1000000, 2)) == 0:
            size_str = f'{round(zip_size / 1000)}KB'
        else:
            size_str = f'{size_mb}MB'
        self.ProcessLabel.setText(f'Success! (Archive size: {size_str})')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Backuper()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
