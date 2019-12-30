import java.sql.*;
import java.util.Scanner;
import java.util.Properties;

public class Bookstore {
	static Statement statement;
	static ResultSet results;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		int Task = 0;
		
		
		while (Task != 5) {
			//Menu for action selection and user input
			System.out.println("Please choose from the menu below");
			System.out.println("1. = Enter book"
				+" "+ "2. = Update Book"
				+ " "+"3. = Delete Book"
				+ " "+"4. = Search Book"
				+ "5. = Exit"); 
			;
			Task = input.nextInt();
		try(
                //Creating table connection and statement
                Connection conn = DriverManager.getConnection(
                		"jdbc:mysql://localhost:3306/ebookstore?useSSL=false&allowPublicKeyRetrieval=true" , "myuser" ,
                		"Banzi@20");

                Statement stmt = conn.createStatement();
                ){
		    //Getting details for the new book i.e title,author,id and qty
			if (Task == 1) {
				input.nextLine();//This enable the user to input more than 1 word
				System.out.println("Please enter the title of the new book:");
				String title = input.nextLine();
				System.out.println("Please enter the author of the new book:");
				String author = input.nextLine();
				System.out.println("Please enter the id of the new book:");
				int id = input.nextInt();
				System.out.println("Please enter the qty of the new book:");
				int qty = input.nextInt();
				String sqlInsert = "insert into books(title,author,id,qty)"
				+ " values('"+ title +"','"+ author +"'," + id +"," + qty + ")";
				System.out.println("The SQL query is: " + sqlInsert);
				int Inserted = stmt . executeUpdate ( sqlInsert );
				System . out . println ( Inserted + " records inserted.\n" );
				
			//Updating the bookstore books	
			}else if (Task == 2) {
				System.out.println("Please enter the id you would like to update the quantity");
				int id = input.nextInt();
				System.out.println("Please enter the new Qty");
				int NewQty = input.nextInt();
				String StrUpdate = "update books set qty " + " = " + NewQty +" "+ "where id "+ "="+ id;
				System.out.println("The SQL query is : " + StrUpdate);
				int countUpdated = stmt.executeUpdate(StrUpdate);
				System . out . println ( countUpdated + " records affected." );
						
			// deleting/taking out the books sold from the database	
			}else if (Task == 3) {
				input.nextLine();//This enables the user to input more than 1 word
				System.out.println("Please enter the title of the book you would like to delete:  ");
				String deltitle = input.nextLine();
				String sqlDelete = "delete from books where title =" +"'" +  deltitle +"'" ;
				System.out.println("The SQL query is : " + sqlDelete);
				int countDeleted = stmt.executeUpdate(sqlDelete);
				System.out.println(countDeleted + " records deleted.\n");
				
			//Searching for books by  id	
			}else if (Task == 4) {
				System.out.println("Please enter the id of the book that you looking for: ");
				int idSearch = input.nextInt();
				String StrSelect = "select * from books where id = "+ idSearch;
				System.out.println("The SQL query is : "+ StrSelect);
				ResultSet rset = stmt.executeQuery(StrSelect);
				
				// move the cursor to the next row
				while ( rset . next ()) {
                	System . out . println ( 
                	 rset . getString ( "author" ) + ", "
                	+ rset . getString ( "title" ) + ", "
                	+ rset.getInt("id")
                	+ rset . getInt ( "qty" ));
                	}
				
			}else if (Task == 5) {	
				System.out.println("Good bye!");
				
			}else {//invalid entry handler
				System.out.println("Sorry, that isnt a valid input.");
				
				
			}
		    }catch(
		    		
		    SQLException ex	)
		   {
		    ex.printStackTrace();
		   }
		}
	} 
		
}									
//Now it's updating the database and works very well, if I may say so myself
	


