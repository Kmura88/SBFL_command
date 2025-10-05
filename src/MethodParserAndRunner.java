import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Method;

import org.junit.Test;

public class MethodParserAndRunner {
    public static void main(String[] args) throws Exception {
    	// 1. 引数の数の確認
        if (args.length != 1) {
            System.err.println("Usage: java MethodParserAndRunner <TestClass>");
	        System.exit(1);
	    }
        
        // 2. 実行対象のテストクラス
        String className = args[0];
        
        // 3. xml_maker_junit4のパス。一番上の階層にいることを想定
        String cmdFilePath = "lib\\xml_maker_junit4.cmd";

        // 4. テストクラスのロード
        Class<?> testClass;
        try {
            testClass = Class.forName(className);
        } catch (ClassNotFoundException e) {
            System.err.println("[ERROR]: Test class not found -> " + className);
            System.exit(1);
            return;
        }

        // 5. @Test の付いたメソッドを順に処理
        for (Method method : testClass.getDeclaredMethods()) {
            if (method.isAnnotationPresent(Test.class)) {
            	
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
                System.out.println("xml_maker_junit4 finished with exit code:" + exitCode);
                System.out.println("----------------------------------");
            }
        }
    }
}