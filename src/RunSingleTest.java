// RunSingleTest.java
import org.junit.runner.JUnitCore;
import org.junit.runner.Request;
import org.junit.runner.Result;

public class RunSingleTest {
	public static void main(String[] args) throws Exception {
		// 1. 引数の数の確認
        if (args.length != 2) {
            System.err.println("Usage: java RunSingleTest <TestClass> <TestMethod>");
	        System.exit(1);
	    }
        
        // 2. 引数の格納
	    String className = args[0];
	    String methodName = args[1];
	    
	    // 3. 実行
	    Class<?> testClass = Class.forName(className);
	    Request request = Request.method(testClass, methodName);
	    Result result = new JUnitCore().run(request);
	    
	    // 4. 終了
	    if (result.wasSuccessful()) {
	        System.exit(0); // テストが成功したら0を返す
	    }else {
	    	System.exit(1); // テストが成功したら1を返す
	    }
	}
}
