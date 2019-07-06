//Question:-
//You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.
//
//Write a function to compute all possible states of the string after one valid move.
//Example string ="++++"

import java.util.ArrayList;
import java.util.List;

public class FlipGame {
	public static List<String> generatePossibleNextMoves(String input){
		List<String> possibleMoves=new ArrayList<>();
		int i=0;
		while(i<input.length()) {
			int nextMove;
			if(i==0) {
				nextMove=input.indexOf("++");
			}
			else {
				nextMove=input.indexOf("++",i);
			}
			//if no such index can be found by the index of function then return an empty arraylist
			if(nextMove==-1) {
				return possibleMoves;
			}
			else {
				String nextState=input.substring(0, nextMove)+ "--" + input.substring(nextMove+2);
				possibleMoves.add(nextState);
				i=nextMove+1;
			}
		}
		return possibleMoves;
	}
	public static void main(String args[]) {
		String input="++++";
		List<String> answerList=generatePossibleNextMoves(input);
		for(String s:answerList) {
			System.out.println(s);
		}
	}
}
