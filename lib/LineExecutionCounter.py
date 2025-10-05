import XmlAnalyzer as XA #XA.XmlAnalyzer(".")
from pathlib import Path
import sys


class LineExcutionCounter:
	def __init__(self,file_path):
		self.file_path = Path(file_path)  # xmlがあるファイルへのパス
		self.excution_counter = {}        # Map< クラス名, 各クラスの行ごとの実行回数int[] >
		self.total_counter = 0            # テストの実行回数
		self._calc_counter()

	def get_excutionCounter(self):
		return self.excution_counter
    
	def get_total_counter(self):
		return self.total_counter
	
	def print_excution_counter(self):
		for cls, arr in self.excution_counter.items():
			print(f"Class: {cls}")
			for i in range(1, len(arr)):  # 行番号は1スタート
				print(f"  Line {i}: {arr[i]}")

	def _calc_counter(self):
		xml_paths = self.file_path.rglob('*') # .xmlファイルを全探索
		for xml_path in xml_paths:
			XmlAnalyzer = XA.XmlAnalyzer(xml_path)
			coverages = XmlAnalyzer.get_coverages()
			for cls, bools in coverages.items():
				if cls not in self.excution_counter:
					self.excution_counter[cls] = [0] * len(bools) # 初回実行時の初期化
				for i, covered in enumerate(bools):
					if covered:
						self.excution_counter[cls][i] += 1  # 実行された回数を加算

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("LineExcutionCounter.py [error] : 引数が指定されていません。")
    else :
        LEC = LineExcutionCounter(sys.argv[1])
        LEC.print_excution_counter()