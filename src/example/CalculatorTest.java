package example;

public class CalculatorTest {
    public static void main(String[] args) {
        Calculator calc = new Calculator();

        // Test add method
        if (calc.add(2, 3) == 5) {
            System.out.println("Test add: PASSED");
        } else {
            System.out.println("Test add: FAILED");
        }

        // Test multiply method with zero
        if (calc.multiply(5, 100) == 500) {
            System.out.println("Test multiply (zero): PASSED");
        } else {
            System.out.println("Test multiply (zero): FAILED");
        }
        
        // subtractメソッドはテストしない
    }
}

/*
 * package example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class CalculatorTest {

    // Calculatorのインスタンスを生成
    private final Calculator calc = new Calculator();

    @Test
    void testAdd() {
        // assertEquals(期待される値, 実際の値, "テスト失敗時のメッセージ");
        assertEquals(5, calc.add(2, 3), "addメソッドのテストが失敗しました");
    }

    @Test
    void testMultiply() {
        assertEquals(500, calc.multiply(5, 100), "multiplyメソッドのテストが失敗しました");
    }

    // subtractメソッドはテストしない
}
 */