/* Defines Deck and Card and related classes */

class Deck {
  // Does not change; is always a list of the cards in order
  Card[] cards;
  ShuffleMethod shuffleMethod;
  // Each shuffle, adds the starting deck order to the list.
  // Each card in the deck order is represented by an integer between 0 and cards.length
  ArrayList<int[]> allOrders;
  
  Deck(int numCards) {
    allOrders = new ArrayList<int[]>();
    cards = new Card[numCards];
    shuffleMethod = new ShuffleMethod0();
    int[] firstOrder = new int[numCards];
    for (int i=0; i<numCards; ++i) {
      cards[i] = new Card(i);
      firstOrder[i] = i;
    }
    allOrders.add(firstOrder);
  }
  
  /* Draws every ordering the deck has been in since creation */
  void displayDeckHistory() {
     for (int i=0; i<allOrders.size(); ++i) {
       displayDeck(i);
     }
  }
  
  /* Draws one ordering of the deck (from allOrders) */
  void displayDeck(int iteration) {
    for (int i=0; i<cards.length; ++i) {
      int origIndex = allOrders.get(iteration)[i];
      cards[origIndex].displayCard(i, cards.length, iteration);
    }
  }
  
  /* Shuffles the cards, adding a new ordering to allOrders */
  void shuffle() {
    int[] newOrdering = shuffleMethod.shuffle(allOrders.get(allOrders.size()-1));
    allOrders.add(newOrdering);
  }
}


class Card {
  // Which card place it would be in the sorted deck (0 - 51, for a regular deck)
  private int originalPlace;
  // Info about how to draw a card
  
  Card(int place) {
    originalPlace = place;  
  }
  
  public int getPlace() {
    return originalPlace;
  }
  
  void displayCard(int currentPlace, int totalPlaces, int iteration) {
    int leftOffset = CardVisInfo.leftOffset;
    int topOffset = CardVisInfo.topOffset;
    int w = CardVisInfo.w, h = CardVisInfo.h;
    int paddingW = CardVisInfo.paddingW, paddingH = CardVisInfo.paddingH;
    int x = leftOffset + currentPlace * (w + paddingW);
    int y = topOffset + iteration * (h + paddingH);
    fill(getCardColor(totalPlaces));
    rect(x, y, w, h);
  }
  
  color getCardColor(int totalPlaces) {
    int r = (originalPlace * 255)/totalPlaces;
    int g = 255 - r;
    int b = 255;
    return color(r, g, b);
  }
}

static class CardVisInfo {
  public static int leftOffset = 10;
  public static int topOffset = 10;
  public static int w = 10;
  public static int h = 40;
  public static int paddingW = 5; 
  public static int paddingH = 15;
}
