import xml.etree.ElementTree as ET
import os

def parse_jacoco_with_source(xml_path, source_root):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    class_coverages = {}

    for cls in root.findall(".//class"):
        class_name = cls.get("name")  # e.g. com/example/Main
        sourcefile = cls.get("sourcefilename")  # e.g. Main.java

        # パッケージ構造をパスに変換
        package = cls.getparent().get("name") if hasattr(cls, "getparent") else None
        if package:
            src_path = os.path.join(source_root, package.replace(".", "/"), sourcefile)
        else:
            src_path = os.path.join(source_root, sourcefile)

        if not os.path.exists(src_path):
            print(f"Warning: source file not found for {class_name}: {src_path}")
            continue

        # ソースコードの総行数
        with open(src_path, "r", encoding="utf-8") as f:
            source_lines = f.readlines()
        total_lines = len(source_lines)

        # boolean 配列を全行分用意
        covered = [False] * (total_lines + 1)  # 行番号は1始まり

        # JaCoCoの行情報を反映
        for line in cls.findall("line"):
            nr = int(line.get("nr"))
            ci = int(line.get("ci"))  # covered instructions
            covered[nr] = (ci > 0)

        class_coverages[class_name] = covered

    return class_coverages


# 使い方例
if __name__ == "__main__":
    coverages = parse_jacoco_with_source("report.xml", "src/main/java")

    for cls, arr in coverages.items():
        print(f"Class: {cls}")
        for i in range(1, len(arr)):  # 行番号1から開始
            print(f"  Line {i}: {arr[i]}")
