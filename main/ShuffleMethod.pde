abstract class ShuffleMethod {
  String name;
  abstract int[] shuffle(int[] ordering);
  int[int[]] cut(int[] ordering) {
    // Margin is how imprecise you are at cutting the deck (from 0 - 0.5)
    int margin = 0.1;
    int middle = random(ordering.length*(0.5-margin), ordering.length*(0.5+margin));
    int[] firstHalf = new int[middle];
    int[] secondHalf = new int[ordering.length-middle];
    for (int i=0; i<middle; ++i) {
      firstHalf[i] = ordering[i]; 
    }
    for (int i=middle; i<ordering.length; ++i) {
      secondHalf[i-middle] = ordering[i]; 
    }
    return {firstHalf, secondHalf};
  }
}

class ShuffleMethod0 extends ShuffleMethod {
  ShuffleMethod0() {}
  
  int[] shuffle(int[] ordering) {
    int[] newOrdering = new int[ordering.length];
    // THIS IS NOT A REAL SHUFFLE THIS IS JUST FOR TESTS
    for (int i=0; i<ordering.length; ++i) {
      newOrdering[i] = ordering[ordering.length-i-1]; 
    }
    return newOrdering;
  }
}

class BridgeShuffle extends ShuffleMethod {
  BridgeShuffle() {}
  int[] shuffle(int[] ordering) {
    
  } 
}
