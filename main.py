import os
import sys
import re
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtCore import QThread, pyqtSignal
from yt_dlp import YoutubeDL

class DownloadThread(QThread):
    progress_changed = pyqtSignal(int)
    finished = pyqtSignal(str)

    def __init__(self, url, output_path, format_type, parent=None):
        super().__init__(parent)
        self.url = url
        self.output_path = output_path
        self.format_type = format_type

    def run(self):
        ydl_opts = {
            'format': 'bestaudio/best' if self.format_type == 'MP3' else 'bestvideo+bestaudio/best',
            'outtmpl': self.output_path,
            'progress_hooks': [self.progress_hook],
            'merge_output_format': 'mp4' if self.format_type == 'MP4' else None,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }] if self.format_type == 'MP3' else [],
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept-Language': 'en-US,en;q=0.5',
            },
        }

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
            self.finished.emit(f"Arquivo salvo em: {self.output_path}")
        except Exception as e:
            self.finished.emit(f"Erro: {e}")

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            # Extrai o percentual do progresso, removendo caracteres ANSI
            percent_str = d['_percent_str']
            clean_percent_str = re.sub(r'\x1b\[[0-9;]*m', '', percent_str).strip('% ')
            try:
                percent = float(clean_percent_str)
                self.progress_changed.emit(int(percent))
            except ValueError:
                pass  # Em caso de falha na conversão, não atualize a barra de progresso

class YouTubeToMP3Converter(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('YouTube to MP3/MP4 Converter')
        self.setGeometry(100, 100, 500, 150)

        layout = QtWidgets.QVBoxLayout()

        form_layout = QtWidgets.QFormLayout()
        self.url_input = QtWidgets.QLineEdit(self)
        form_layout.addRow('URL do vídeo do YouTube:', self.url_input)

        self.format_combo = QtWidgets.QComboBox(self)
        self.format_combo.addItems(['MP3', 'MP4'])
        form_layout.addRow('Formato:', self.format_combo)

        layout.addLayout(form_layout)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        layout.addWidget(self.progress_bar)

        self.download_button = QtWidgets.QPushButton('Baixar e Converter', self)
        self.download_button.clicked.connect(self.on_download_click)
        layout.addWidget(self.download_button)
        
        self.setLayout(layout)
        self.dark_mode()

    def dark_mode(self):
        dark_mode_css = """
        QWidget {
            background-color: #2e2e2e;
            color: #ffffff;
        }
        QLineEdit {
            background-color: #3e3e3e;
            color: #ffffff;
            border: 1px solid #5e5e5e;
        }
        QPushButton {
            background-color: #5e5e5e;
            color: #ffffff;
            border: 1px solid #7e7e7e;
        }
        QProgressBar {
            background-color: #3e3e3e;
            color: #66cc00;
            border: 1px solid #5e5e5e;
        }
        QProgressBar::chunk {
            background-color: #6a6a6a;
        }
        QMessageBox {
            background-color: #2e2e2e;
            color: #ffffff;
        }
        """
        self.setStyleSheet(dark_mode_css)

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def show_message(self, message):
        QtWidgets.QMessageBox.information(self, "Informação", message)

    def on_download_click(self):
        url = self.url_input.text()
        format_choice = self.format_combo.currentText()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Escolha o diretório")
        if not directory:
            QtWidgets.QMessageBox.warning(self, "Atenção", "Por favor, escolha um diretório para salvar o arquivo.")
            return
        if url:
            output_path = os.path.join(directory, '%(title)s.%(ext)s')
            self.thread = DownloadThread(url, output_path, format_choice)
            self.thread.progress_changed.connect(self.update_progress)
            self.thread.finished.connect(self.show_message)
            self.thread.start()
        else:
            QtWidgets.QMessageBox.warning(self, "Atenção", "Por favor, insira a URL do vídeo do YouTube.")

def main():
    app = QtWidgets.QApplication(sys.argv)
    converter = YouTubeToMP3Converter()
    converter.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
