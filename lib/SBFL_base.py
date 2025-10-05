import LineExecutionCounter as LEC
import csv
import os

FAIL_PATH = "../.SBFL_data/fail_test"
PASS_PATH = "../.SBFL_data/pass_test"
CSV_PATH =  "../summary.csv"

class SBFL_base:
	def __init__(self):
		fail_counter = LEC.LineExecutionCounter(FAIL_PATH)
		pass_counter = LEC.LineExecutionCounter(PASS_PATH)
		self.ef = fail_counter.get_excutionCounter()	# Map< クラス名, 各クラスの行ごとのef >
		self.ep = pass_counter.get_excutionCounter()	# Map< クラス名, 各クラスの行ごとのep >
		self.tf = fail_counter.get_total_counter()		# failtestの実行回数
		self.tp = pass_counter.get_total_counter()		# passtestの実行回数
		self.nf = {i:[self.tf - k for k in j]
					for i, j in self.ef.items()}		# Map< クラス名, 各クラスの行ごとのnf >
		self.np = {i:[self.tp - k for k in j]
					for i, j in self.ep.items()}		# Map< クラス名, 各クラスの行ごとのnp >
		self.suspecious = {i:[0.0] * len(j)
					for i, j in self.ef.items()}		# Map< クラス名, 各クラスの行ごとのsuspecious double[] >

	def get_suspecious(self):
		return self.suspecious
    
	def get_ef(self):
		return self.ef 
	
	def get_nf(self):
		return self.nf
	
	def get_ep(self):
		return self.ep
	
	def get_np(self):
		return self.np 
		
	def print_execution_summary(self):
		for cls in self.ef.keys():
			print(f"=== {cls} ===")
			ef_list = self.ef.get(cls, [])
			ep_list = self.ep.get(cls, [])
			nf_list = self.nf.get(cls, [])
			np_list = self.np.get(cls, [])
			sus_list = self.suspecious.get(cls, [])
			print(f"{'Line':>4} | {'ef':>4} | {'ep':>4} | {'nf':>4} | {'np':>4} | {'sus':>8}")
			print("-" * 44)
			max_len = max(len(ef_list), len(ep_list), len(nf_list), len(np_list), len(sus_list))
			for i in range(max_len):
				ef = ef_list[i] if i < len(ef_list) else "-"
				ep = ep_list[i] if i < len(ep_list) else "-"
				nf = nf_list[i] if i < len(nf_list) else "-"
				np = np_list[i] if i < len(np_list) else "-"
				sus = f"{sus_list[i]:.4f}" if i < len(sus_list) else "-"
				print(f"{i:>4} | {ef:>4} | {ep:>4} | {nf:>4} | {np:>4} | {sus:>8}")
			print()
	
	def save_execution_summary(self, file_path=CSV_PATH):
		dir_name = os.path.dirname(file_path) # ディレクトリ名を取得

		if dir_name:
			os.makedirs(dir_name, exist_ok=True) # ディレクトリ指定がある場合のみ作成

		with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
			writer = csv.writer(csvfile)
			writer.writerow(["ClassName", "Line", "ef", "ep", "nf", "np", "suspecious"])

			for cls in self.ef.keys():
				ef_list = self.ef.get(cls, [])
				ep_list = self.ep.get(cls, [])
				nf_list = self.nf.get(cls, [])
				np_list = self.np.get(cls, [])
				sus_list = self.suspecious.get(cls, [])

				max_len = max(len(ef_list), len(ep_list), len(nf_list), len(np_list), len(sus_list))
				for i in range(max_len):
					ef = ef_list[i] if i < len(ef_list) else ""
					ep = ep_list[i] if i < len(ep_list) else ""
					nf = nf_list[i] if i < len(nf_list) else ""
					np = np_list[i] if i < len(np_list) else ""
					sus = sus_list[i] if i < len(np_list) else ""
					writer.writerow([cls, i, ef, ep, nf, np, sus])

		print(f"✅ 実行サマリCSVを書き出しました → {file_path}")

	def _calc_suspecious(self):
		None