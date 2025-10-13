import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Method;
import java.lang.reflect.Modifier;

public class MethodParserAndRunnerForJUnit3 {
    public static void main(String[] args) throws Exception {
        // 1. 引数の数の確認
        if (args.length != 1) {
            System.err.println("Usage: java MethodParserAndRunnerForJUnit3 <TestClass>");
            System.exit(1);
        }

        // 2. 実行対象のテストクラス
        String className = args[0];

        // 3. xml_maker_junit3のパス。一番上の階層にいることを想定
        String cmdFilePath = "lib\\xml_maker_junit3.cmd"; // スクリプト名を変更

        // 4. テストクラスのロード
        Class<?> testClass;
        try {
            testClass = Class.forName(className);
        } catch (ClassNotFoundException e) {
            System.err.println("[ERROR]: Test class not found -> " + className);
            System.exit(1);
            return;
        }

        // 5. 'test'で始まるメソッドを順に処理 (JUnit 3形式)
        for (Method method : testClass.getDeclaredMethods()) {
            // JUnit 3の規約に合致するかチェック
            // 1. メソッド名が "test" で始まる
            // 2. public である
            // 3. 引数がない
            if (method.getName().startsWith("test")
                    && Modifier.isPublic(method.getModifiers())
                    && method.getParameterCount() == 0) {

                String methodName = method.getName();
                System.out.println("Running cmd for test method: " + methodName);

                // .cmd を引数付きで実行
                ProcessBuilder pb = new ProcessBuilder("cmd.exe", "/c", cmdFilePath, className, methodName);

                pb.redirectErrorStream(true);

                // コマンド実行
                Process process = pb.start();

                // 出力ログを標準出力に転送
                try (BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()))) {
                    String line;
                    while ((line = reader.readLine()) != null) {
                        System.out.println(line);
                    }
                }

                int exitCode = process.waitFor();
                System.out.println("xml_maker_junit3 finished with exit code:" + exitCode);
                System.out.println("----------------------------------");
            }
        }
    }
}