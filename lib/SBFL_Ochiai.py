from SBFL_base import SBFL_base as SBFL
import math
import logging

logging.basicConfig(
    level=logging.INFO, # INFOレベル以上のログを記録
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


class SBFL_Ochiai(SBFL):
	def __init__(self):
		super().__init__()
		self.logger = logging.getLogger(self.__class__.__name__)
		self._calc_suspecious()

	def _calc_suspecious(self):
		for cls in self.ef.keys():
			ef_list = self.ef[cls]
			ep_list = self.ep.get(cls, [0]*len(ef_list))
			nf_list = self.nf.get(cls, [0]*len(ef_list))
			np_list = self.np.get(cls, [0]*len(ef_list))

			susp_list = []
			for ef, ep, nf, np in zip(ef_list, ep_list, nf_list, np_list):
				denom = math.sqrt((ef + nf) * (ef + ep))
				if denom == 0:
					susp_list.append(0.0)
				else:
					susp_list.append(ef / denom)

			self.suspecious[cls] = susp_list
		
		self.logger.info(f"Finished ra_suspecious calculation for {cls}")


if __name__ == "__main__":
	SB = SBFL_Ochiai()
	SB.print_execution_summary()
	SB.save_execution_summary()