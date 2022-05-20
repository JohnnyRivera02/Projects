package sample;

import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.stage.Stage;

//Johnny Rivera
//This code creates a GUI and takes in 3 user inputs and finds the roots in the given quadratic equation. The code then displays the results in the fourth text field.
public class QuadraticEQSolver extends Application
{
    //Text Fields
    private TextField tfA = new TextField();
    private TextField tfB = new TextField();
    private TextField tfC = new TextField();
    private TextField tfAnswer = new TextField();
    private Button btOK = new Button("Solve");


    @Override
    public void start(Stage primaryStage)
    {
        BorderPane pane = new BorderPane();

        //Hbox 1
        HBox hbox1 = new HBox(15);
        hbox1.setPadding(new Insets(15,15,15,15));
        hbox1.getChildren().add(new Label("a:"));
        hbox1.getChildren().add(tfA);
        hbox1.getChildren().add(new Label("b:"));
        hbox1.getChildren().add(tfB);
        hbox1.getChildren().add(new Label("c:"));
        hbox1.getChildren().add(tfC);
        hbox1.getChildren().add(new Label("Roots of ax\u00B2 + bx + c:"));
        hbox1.getChildren().add(tfAnswer);

        //Hbox 2
        HBox hbox2 = new HBox(15);
        hbox2.setPadding(new Insets(15,15,15,15));
        hbox2.setAlignment(Pos.CENTER);
        hbox2.getChildren().add(btOK);

        //HBox assignment
        pane.setTop(hbox1);
        pane.setBottom(hbox2);

        btOK.setOnAction(e -> calculateQuadratic());

        //Set Scene
        Scene scene = new Scene(pane);
        primaryStage.setTitle("Quadratic equation solver");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    private void calculateQuadratic()
    {
        double a,b,c;
        //Parse textfield and catch if there is exception
        try
        {
            a = Double.parseDouble(tfA.getText());
        }
        catch (NumberFormatException e)
        {
            tfA.setText("0");
            a = 0;
        }
        try
        {
            b = Double.parseDouble(tfB.getText());
        }
        catch (NumberFormatException e)
        {
            tfB.setText("0");
            b = 0;
        }
        try
        {
            c = Double.parseDouble(tfC.getText());
        }
        catch (NumberFormatException e)
        {
            tfC.setText("0");
            c = 0;
        }

        //Deal with all cases of a,b,c and print tfAnswer
        if (a == 0)
        {
            if (b == 0 && c == 0)
            {
                tfAnswer.setText("All x");
            }
            else if (b == 0 && c != 0)
            {
                tfAnswer.setText("No x");
            }
            else if (b != 0 && c == 0)
            {
                tfAnswer.setText("0.0");
            }
            else
                {
                double x = -c / b;
                tfAnswer.setText(String.valueOf(x));
            }
        }
        else
            {
            double discriminant = b * b - 4 * a * c;
            if (discriminant > 0)
            {
                double x1 = ((-b + Math.sqrt(discriminant)) / (2 * a));
                double x2 = ((-b - Math.sqrt(discriminant)) / (2 * a));
                String tfAnswerString = String.valueOf(x1) + ", " +
                        String.valueOf(x2);
                tfAnswer.setText(tfAnswerString);
            }
            else if (discriminant < 0)
            {
                tfAnswer.setText("No x");
            }
            else if (discriminant == 0)
            {
                double x = -b / (2 * a);
                if (x == -0.0)
                    tfAnswer.setText("0.0");
                else
                    tfAnswer.setText(String.valueOf(x));
            }
        }
    }
}

