import java.io.Console;
import java.util.List;
import java.util.ListIterator;
import java.util.Scanner;

import javax.smartcardio.ATR;
import javax.smartcardio.Card;
import javax.smartcardio.CardChannel;
import javax.smartcardio.CardException;
import javax.smartcardio.CardTerminal;
import javax.smartcardio.CardTerminals;
import javax.smartcardio.CommandAPDU;
import javax.smartcardio.ResponseAPDU;
import javax.smartcardio.TerminalFactory;

public class PCSC {
	public static void main(String[] args){

		CardTerminal terminals = new CardTerminals();
		terminals = TerminalFactory.getDefault().terminals().list();
		String name = terminals.getName();	      
		System.out.println("Detected "  + name);

		if(!isCardPresent()){
			System.out.println("Thread started... Waiting for card...");
			cardTerminal.waitForCardPresent(100);
		}
		if(isCardPresent()){System.out.println("Card found");}
		card = cardTerminal.connect("*");
		cardChannel = card.getBasicChannel();
		if(authenticate())
		{
			int UID = getUID();
			System.out.println("User identified as :" + String.valueOf(UID));
		}
	}}
