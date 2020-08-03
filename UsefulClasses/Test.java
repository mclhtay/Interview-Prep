import static org.junit.Assert.*;

public class Test<T>{
  private static Utils u = new Utils();
  public void verify(T arg1, T arg2){
   if(arg1.getClass().getName() == "TreeNode"){
      var result = verifyTree((TreeNode)arg1,(TreeNode) arg2);
      if(result == true){
        u.p("Passed");
      }else{
        u.p("Failed");
      }
    }
    else{
      assertEquals(arg1, arg2);
      u.p("Passed");
     
    }

  }

  public void verify(T[] a1, T[] a2){
      assertArrayEquals(a1, a2);
      u.p("Passed");
  }

  public boolean verifyTree(TreeNode t1, TreeNode t2){
    if(t1 == null && t2 == null) return true;
    if(t1 == null || t2 == null) return false;

    if(t1.val != t2.val) return false;

    return verifyTree(t1.left, t2.left) && verifyTree(t1.right, t2.right);

  }

}