
import java.util.Scanner;

public class tictactoe {
	
	public static final int EMPTY = 0;
	public static final int CROSS = 1;
	public static final int CIRCLE = 2;
	
	public static final int PLAYING = 0;
	public static final int DRAW = 1;
	public static final int CROSS_WON = 2;
	public static final int CIRCLE_WON = 3;
	
	public static final int ROWS = 3, COLS = 3;
	public static int[][] board = new int[ROWS][COLS];
	
	public static int currentState;
	public static int currentPlayer;
	public static int currentRow, currentCol;
	
	public static Scanner in = new Scanner(System.in);
	
	public static void initGame() {
		for(int row = 0; row < ROWS; ++row) {
			for(int col = 0; col < COLS; ++col) {
				board[row][col] = EMPTY;
			}
		}
		currentState = PLAYING;
		currentPlayer = CROSS;
	}
	
	public static void playerMove(int input) {
		boolean validMove = false;
		int row, col;
		do {
			if(input == CROSS) {
				System.out.print("Player 'X', enter your move\n(row[1-3]):");
				row = in.nextInt() - 1;
				System.out.print("(col[1-3]:");
				col = in.nextInt() - 1;
			} else {
				System.out.print("Player 'O', enter your move\n(row[1-3]):");
				row = in.nextInt() - 1;
				System.out.print("(col[1-3]):");
				col = in.nextInt() - 1;
			}
			if (row >= 0 && row < ROWS && col >= 0 && col < COLS && board[row][col] == EMPTY) {
				currentRow = row;
				currentCol = col;
				board[currentRow][currentCol] = input;
				validMove = true;
			} else {
				System.out.println("This move at (" + (row + 1) + "," + (col + 1) + ") is not a valid move. Try again.");
			}
		} while(!validMove);
	}
	
	public static boolean isDraw() {
	      for (int row = 0; row < ROWS; ++row) {
	         for (int col = 0; col < COLS; ++col) {
	            if (board[row][col] == EMPTY) {
	               return false;  
	            }
	         }
	      }
	      return true;  
	}
	
	public static boolean hasWon(int input, int currentRow, int currentCol) {
	      return (board[currentRow][0] == input         
	                   && board[currentRow][1] == input
	                   && board[currentRow][2] == input
	              || board[0][currentCol] == input      
	                   && board[1][currentCol] == input
	                   && board[2][currentCol] == input
	              || currentRow == currentCol            
	                   && board[0][0] == input
	                   && board[1][1] == input
	                   && board[2][2] == input
	              || currentRow + currentCol == 2  
	                   && board[0][2] == input
	                   && board[1][1] == input
	                   && board[2][0] == input);
	}
	
	public static void printCell(int content) {
	      switch (content) {
	         case EMPTY:  System.out.print("   "); break;
	         case CIRCLE: System.out.print(" O "); break;
	         case CROSS:  System.out.print(" X "); break;
	      }
	}
	
	public static void printBoard() {
	      for (int row = 0; row < ROWS; ++row) {
	         for (int col = 0; col < COLS; ++col) {
	            printCell(board[row][col]); 
	            if (col != COLS - 1) {
	               System.out.print("|");   
	            }
	         }
	         System.out.println();
	         if (row != ROWS - 1) {
	            System.out.println("-----------"); 
	         }
	      }
	      System.out.println();
	}
	
	public static void updateGame(int input, int currentRow, int currentCol) {
	      if (hasWon(input, currentRow, currentCol)) {  
	         currentState = (input == CROSS) ? CROSS_WON : CIRCLE_WON;
	      } else if (isDraw()) {  // check for draw
	         currentState = DRAW;
	      }
	      
	}
	
	public static void main(String[] args) {
	      // Initialize the game-board and current status
	      initGame();
	      // Play the game once
	      do {
	         playerMove(currentPlayer);
	         updateGame(currentPlayer, currentRow, currentCol); 
	         printBoard();
	         if (currentState == CROSS_WON) {
	            System.out.println("'X' won! Bye!");
	         } else if (currentState == CIRCLE_WON) {
	            System.out.println("'O' won! Bye!");
	         } else if (currentState == DRAW) {
	            System.out.println("It's a Draw! Bye!");
	         }
	         currentPlayer = (currentPlayer == CROSS) ? CIRCLE : CROSS;
	      } while (currentState == PLAYING); 
	}
}
