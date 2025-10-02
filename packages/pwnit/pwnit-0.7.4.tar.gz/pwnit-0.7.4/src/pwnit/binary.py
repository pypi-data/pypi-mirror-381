from pathlib import Path
from pwn import ELF

from pwnit.utils import log

class Binary(ELF):
	def __init__(self, filepath: Path) -> None:
		super().__init__(filepath.expanduser(), checksec=False)

		# Create path objects
		self.path: Path = Path(self.path)
		self.debug_path: Path = self.path

		log.info(f"{type(self).__name__}: {self.path}")
