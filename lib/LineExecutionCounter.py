import XmlAnalyzer as XA #XA.XmlAnalyzer(".")
import sys


class LineExcutionCounter:
	def __init__(self,file_path):
		self.file_path = file_path  # xmlがあるファイルへのパス
		self.excution_counter = {}  # Map< クラス名, 各クラスの行ごとの実行回数int[] >
		self.total_counter = 0      # テストの実行回数
		self.xml_path = XA.XmlAnalyzer(".")

	def get_excutionCounter(self):
		return self.excution_counter
    
	def get_total_counter(self):
		return self.total_counter
	
	def print_excution_counter(self):
		for cls, arr in self.coverages.items():
			print(f"Class: {cls}")
			for i in range(1, len(arr)):  # 行番号は1スタート
				print(f"  Line {i}: {arr[i]}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("LineExcutionCounter.py [error] : 引数が指定されていません。")
    else :
        LEC = LineExcutionCounter(sys.argv[1])
        LEC.print_excution_counter()