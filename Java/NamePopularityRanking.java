package sample;

import java.io.File;
import java.net.URL;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class BabyNamePopularityRanking extends Application {
  private Map<String, Integer>[] mapForMale = new HashMap[10];
  private Map<String, Integer>[] mapForFemale = new HashMap[10];
  
  private Button btFindRanking = new Button("Find Ranking");
  private ComboBox<Integer> cboYear = new ComboBox<>();
  private ComboBox<String> cboGender = new ComboBox<>();
  private TextField tfName = new TextField();
  private Label lblResult = new Label();

  //Johnny Rivera
  //This code gets the user's input on three different areas, the year, the gender, and the name of the baby. The code will return the babies name that the user entered as well as the information that was to be retrieved, in this case it was the ranking of the name in a
  //specified year. The code uses Hashmaps to get this data.

  @Override // Override the start method in the Application class
  public void start(Stage primaryStage) 
  {
    GridPane gridPane = new GridPane();
    gridPane.add(new Label("Select a year:"), 0, 0);
    gridPane.add(new Label("Boy or girl?"), 0, 1);
    gridPane.add(new Label("Enter a name:"), 0, 2);
    gridPane.add(cboYear, 1, 0);
    gridPane.add(cboGender, 1, 1);
    gridPane.add(tfName, 1, 2);
    gridPane.add(btFindRanking, 1, 3);
    gridPane.setAlignment(Pos.CENTER);
    gridPane.setHgap(5);
    gridPane.setVgap(5);
  
    BorderPane borderPane = new BorderPane();
    borderPane.setCenter(gridPane);
    borderPane.setBottom(lblResult);
    BorderPane.setAlignment(lblResult, Pos.CENTER);

    // Create a scene and place it in the stage
    Scene scene = new Scene(borderPane, 370, 160);
    primaryStage.setTitle("Baby Name Popularity Ranking"); // Set the stage title
    primaryStage.setScene(scene); // Place the scene in the stage
    primaryStage.show(); // Display the stage

    for (int year = 2001; year <= 2010; year++) 
    {
      cboYear.getItems().add(year);
    }
    cboYear.setValue(2001);
        
    cboGender.getItems().addAll("Male", "Female");
    cboGender.setValue("Male");
    
    btFindRanking.setOnAction(e -> findRanking());
    
    readNames();
  }

  public void findRanking() 
  {
    Map<Integer, Map<String, Integer>> male = new HashMap<>();
    Map<Integer, Map<String, Integer>> female = new HashMap<>();
    int key = cboYear.getValue();

    for (int i = 0; i <= 9; i++)
    {
      male.put(i + 2001, mapForMale[i]);
      female.put(i + 2001, mapForFemale[i]);
    }
    if (mapForMale[key - 2001].containsKey(tfName.getText()))
    {
      lblResult.setText(cboGender.getValue() + " name " + tfName.getText() + " is ranked #" + male.get(key).get(tfName.getText()) + " in year " + key);
    }
    else if (mapForFemale[key - 2001].containsKey(tfName.getText()))
    {
      lblResult.setText(cboGender.getValue() + " name " + tfName.getText() + " is ranked #" + female.get(key).get(tfName.getText()) + " in year " + key);
    }
    else if (!mapForMale[key - 2001].containsKey(tfName.getText()))
    {
      lblResult.setText(cboGender.getValue() + " name " + tfName.getText() + " is not ranked in year " + key);
    }
    else
      {
      lblResult.setText(cboGender.getValue() + " name " + tfName.getText() + " is not ranked in year " + key);
    }
  }

  private void readNames() 
  {
    try 
    {
      for (int i = 0; i <= 9; i++) 
      {
        File file = new File("src/sample/babynames/babynamesranking" + (2001 + i) + ".txt");
        Scanner input = new Scanner(file);

        mapForMale[i] = new HashMap<>();
        mapForFemale[i] = new HashMap<>();
        while (input.hasNext()) 
        {
          int ranking = input.nextInt();
          String maleName = input.next();
          input.nextInt();
          String femaleName = input.next();
          input.nextInt();

          mapForMale[i].put(maleName, ranking);
          mapForFemale[i].put(femaleName, ranking);
        }
      }
    }
    catch (Exception ex)
    {
      ex.printStackTrace();
    }
  }

  
  public static void main(String[] args)
  {
    launch(args);
  }
}
