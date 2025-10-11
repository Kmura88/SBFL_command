import XmlAnalyzer as XA
from pathlib import Path
import sys
import logging

logging.basicConfig(
    level=logging.INFO, # INFOレベル以上のログを記録
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class LineExecutionCounter:
	def __init__(self,folder_path):
		self.logger = logging.getLogger(self.__class__.__name__)
		self.folder_path = Path(folder_path)  # xmlがあるファイルへのパス
		self.execution_counter = {}       # Map< クラス名, 各クラスの行ごとの実行回数int[] >
		self.total_counter = 0            # テストの実行回数
		self._calc_counter()

	def get_excutionCounter(self):
		return self.execution_counter
    
	def get_total_counter(self):
		return self.total_counter
	
	def print_excution_counter(self):
		for cls, arr in self.execution_counter.items():
			print(f"Class: {cls}")
			for i in range(1, len(arr)):  # 行番号は1スタート
				print(f"  Line {i}: {arr[i]}")

	def _calc_counter(self):
		xml_paths = self.folder_path.rglob('*') # .xmlファイルを全探索
		for xml_path in xml_paths:
			self.total_counter += 1
			XmlAnalyzer = XA.XmlAnalyzer(xml_path)
			coverages = XmlAnalyzer.get_coverages()
			for cls, bools in coverages.items():
				if cls not in self.execution_counter:
					self.execution_counter[cls] = [0] * len(bools) # 初回実行時の初期化
				for i, covered in enumerate(bools):
					if covered:
						self.execution_counter[cls][i] += 1  # 実行された回数を加算

		self.logger.info(f"Completed the LineExecutionCounter calculation for {self.folder_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("LineExecutionCounter.py [error] : 引数が指定されていません。")
    else :
        LEC = LineExecutionCounter(sys.argv[1])
        LEC.print_excution_counter()