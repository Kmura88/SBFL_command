from SBFL_base import SBFL_base as SBFL
import math

class SBFL_Ochiai(SBFL):
	def __init__(self):
		super().__init__()
		self._calc_suspecious()

	def _calc_suspecious(self):
		for cls in self.ef.keys():
			ef_list = self.ef[cls]
			ep_list = self.ep.get(cls, [0]*len(ef_list))
			nf_list = self.nf.get(cls, [0]*len(ef_list))
			np_list = self.np.get(cls, [0]*len(ef_list))

			susp_list = []
			for ef, ep, nf, np in zip(ef_list, ep_list, nf_list, np_list):
				fail_part = ef / (ef + nf) if (ef + nf) > 0 else 0.0
				pass_part = ep / (ep + np) if (ep + np) > 0 else 0.0
				denom = fail_part + pass_part
				if denom == 0:
					susp_list.append(0.0)
				else:
					susp_list.append(fail_part / denom)

			self.suspecious[cls] = susp_list


if __name__ == "__main__":
	SB = SBFL_Ochiai()
	SB.print_execution_summary()
	SB.save_execution_summary()