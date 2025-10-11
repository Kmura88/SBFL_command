import xml.etree.ElementTree as ET
import sys

IGNORE_LIST = ["/RunSingleTest.java","/MethodParserAndRunner.java"]

class XmlAnalyzer:
    def __init__(self,xml_path):
        self.xml_path=xml_path  # .xmlファイルへのパス
        self.coverages = {}     # Map< クラス名, 各クラスの行ごとのカバレッジboolean[] >
        self._calc_coverages()  # xml解析

    def print_coverages(self):
        for cls, arr in self.coverages.items():
            print(f"Class: {cls}")
            for i in range(1, len(arr)):  # 行番号は1スタート
                print(f"  Line {i}: {arr[i]}")

    def get_coverages(self):
        return self.coverages 
    
    def _calc_coverages(self):
        xml_root = ET.parse(self.xml_path).getroot() # xmlデータの取得

        # パッケージ -> ソースファイルの順で xmlを探索
        for xml_pkg in xml_root.findall("package"):
            for xml_src in xml_pkg.findall("sourcefile"):
                package_name = xml_pkg.get("name")  # ex) com/example
                src_name =  xml_src.get("name")     # ex) Main.java
                fqn = package_name + '/' + src_name # ex) com/example/Main.java

                if fqn.endswith("Test.java") or fqn in IGNORE_LIST: # 不要なクラス、テストクラスのカバレッジは無視
                    continue

                xml_line = xml_src.findall("line")

                if not xml_line:
                    print(f"[Warning] No <line> tags found in {fqn}. Skipping this file.")
                    continue

                covered = [False] * (int(xml_line[-1].get("nr")) + 1)  # boolean配列サイズ = 最後の命令行

                for xl in xml_line:
                    nr = int(xl.get("nr")) # line_number
                    ci = int(xl.get("ci")) # covered_instructions
                    covered[nr] = (ci > 0)

                self.coverages[fqn] = covered

    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("XmlAnalyzer.py [error] : 引数が指定されていません。")
    else :
        XA = XmlAnalyzer(sys.argv[1])
        XA.print_coverages()
