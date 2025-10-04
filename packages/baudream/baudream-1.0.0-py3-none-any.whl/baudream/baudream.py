import subprocess, sys
from asyncio.log import logger
from pathlib import Path
import browsers


def open_file(file_path):
    try:
        if sys.platform == 'linux':
            subprocess.run(['xdg-open', file_path])
        elif sys.platform == 'darwin':
            subprocess.run(['open', file_path])
        else:
            logger.error('Unsupported OS')
    except Exception as e:
        raise RuntimeError(f"Failed to open file: {e}")

def open_pdf(file_path):
    p = Path(file_path).resolve()
    if not p.exists():
        raise FileNotFoundError(f"Fichier introuvable: {p}")
    available_browsers = [b.get('browser_type') for b in list(browsers.browsers())]
    print(available_browsers)
    if 'firefox' in available_browsers:
        browsers.launch('firefox', url=p.as_uri())
    elif 'safari' in available_browsers:
        browsers.launch("safari", url=p.as_uri())
    elif 'chrome' in available_browsers:
        browsers.launch("chrome", url=p.as_uri())
    else:
        logger.error('Unsupported OS')

def main():
    pdf_path = Path(__file__).resolve().parent / "ressources" / "Plan_cours.pdf"
    open_pdf(pdf_path)