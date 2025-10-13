// RunSingleTestForJUnit3.java
import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import junit.textui.TestRunner;
import junit.framework.TestResult;

public class RunSingleTestForJUnit3 {
    public static void main(String[] args) throws Exception {
        // 1. 引数の数の確認
        if (args.length != 2) {
            System.err.println("Usage: java RunSingleTestForJUnit3 <TestClass> <TestMethod>");
            System.exit(1);
        }

        // 2. 引数の格納
        String className = args[0];
        String methodName = args[1];

        // 3. テストクラスのロード
        Class<?> testClass;
        try {
            testClass = Class.forName(className);
        } catch (ClassNotFoundException e) {
            System.err.println("[ERROR]: Test class not found -> " + className);
            System.exit(1);
            return;
        }

        // 4. 実行したいテストメソッドを指定してTestSuiteを構築
        TestSuite suite = new TestSuite();
        // TestCase(String name)コンストラクタを使い、特定のテストインスタンスを生成
        Test test = (Test) testClass.getConstructor(String.class).newInstance(methodName);
        suite.addTest(test);

        // 5. TestRunnerで実行
        TestResult result = TestRunner.run(suite);

        // 6. 終了
        if (result.wasSuccessful()) {
            System.exit(0); // テストが成功したら0を返す
        } else {
            System.exit(1); // テストが失敗したら1を返す
        }
    }
}