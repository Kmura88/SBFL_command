package example;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

/**
 * All test cases correspond to Myers's 14 questions.
 */
public class TriangleTest {

  @Test public void testScalene1() {
    int type = MaxFinder.findMax(9, 5, 2); // Q1
    assertEquals(9, type);
  }

  @Test public void testEquiliteral() {
    int type = MaxFinder.findMax(5, 9, 2); // Q1
    assertEquals(9, type);
  }

  @Test public void testIsoscele1() {
    int type = MaxFinder.findMax(5, 2,9); // Q1
    assertEquals(9, type);
  }

  @Test public void testIsoscele2() {
    int type = MaxFinder.findMax(9, 9, 5); // Q1
    assertEquals(9, type);
  }

  @Test public void testIsoscele3() {
    int type = MaxFinder.findMax(9, 2, 9); // Q1
    assertEquals(9, type);
  }

  @Test public void testInvalid1() {
    int type = MaxFinder.findMax(2, 2, 2); // Q1
    assertEquals(2, type);
  }

  // Q12, float checking, cannot be executed on typed language.
  // Q13, short args, also cannot be executed on java.
  // Ofc, Q14 is considered on all the above test cases.
}