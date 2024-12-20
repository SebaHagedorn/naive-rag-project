from pathlib import Path

from decouple import config

OPENAI_API_KEY = config('OPENAI_API_KEY', default='')

DIR_PATH = Path(__file__).cwd().parent
