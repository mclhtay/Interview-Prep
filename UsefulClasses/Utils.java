public class Utils{

  public void p(int val){
    System.out.println(val);
  }

  public void p(String val){
    System.out.println(val);
  }

  public void p(double val){
    System.out.println(val);
  }
  public void p(char val){
    System.out.println(val);
  }

  public void p(long val){
    System.out.println(val);
  }


  public void traverse(Object [] array){
    System.out.println();
    for(Object o : array){
      System.out.print(o.toString()+" ");
    }
    System.out.println();
  }

  public void traverse(int [] array){
    System.out.println();
    for(int o : array){
      System.out.print(o+ " ");
    }
    System.out.println();
  }
  public void traverse(double [] array){
    System.out.println();
    for(double o : array){
      System.out.print(o+ " ");
    }
    System.out.println();
  }
  public void traverse(char [] array){
    System.out.println();
    for(char o : array){
      System.out.print(o+ " ");
    }
    System.out.println();
  }
}