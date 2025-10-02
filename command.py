import xml.etree.ElementTree as ET

XML_NAME = "report.xml" #xmlファイルの名前

def calc_coverages(xml_path):
    xml_root = ET.parse(xml_path).getroot() # xmlデータの取得
    coverages = {} # Map<クラス名,カバレッジ配列>

    # パッケージ -> ソースファイルの順で探索
    for xml_pkg in xml_root.findall("package"):
        for xml_src in xml_pkg.findall("sourcefile"):
            package_name = xml_pkg.get("name")  # ex) com/example
            src_name =  xml_src.get("name")     # ex) Main.java
            fqn = package_name + '/' + src_name # ex) com/example/Main.java

            xml_line = xml_src.findall("line")
            covered = [False] * (int(xml_line[-1].get("nr")) + 1)  # boolean配列 (size = 最後の命令行番号)

            for xl in xml_line:
                nr = int(xl.get("nr")) # line_number
                ci = int(xl.get("ci")) # covered_instructions
                covered[nr] = (ci > 0)

            coverages[fqn] = covered
            
    return coverages

def print_coverages(coverages):
    for cls, arr in coverages.items():
        print(f"Class: {cls}")
        for i in range(1, len(arr)):  # 行番号1から開始
            print(f"  Line {i}: {arr[i]}")


if __name__ == "__main__":
    
    coverages = calc_coverages(XML_NAME) # xml ファイルからカバレッジの取得
    print_coverages(coverages) 
    