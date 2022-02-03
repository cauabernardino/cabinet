import os

HOME = os.environ["HOME"]
UTENSILS_DIR = ".utensils"
UTENSILS_DIR_FULL_PATH = os.path.join(HOME, UTENSILS_DIR)

SUPPORTED_FILETYPES = {
    ".py": "python3",
    ".go": "go run",
}
