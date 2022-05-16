package sample;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Pane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Line;
import javafx.stage.Stage;
//Johnny Rivera
//This code takes in two user inputs, the number of branches to create and the the number of swirls to add as well. Whether it be hitting enter on either both the first or second text box it will update the picture. This code also generates a random color for the branches to be.
public class Swirls extends Application
{
    @Override // Override the start method in the Application class
    public void start(Stage primaryStage)
    {
        SwirlPane pane = new SwirlPane();
        TextField tfOrder = new TextField();
        TextField tfBranches = new TextField();
        tfOrder.setOnAction(e -> pane.setDepth(Integer.parseInt(tfOrder.getText()),Integer.parseInt(tfBranches.getText())));
        tfOrder.setPrefColumnCount(4);
        tfOrder.setAlignment(Pos.BOTTOM_RIGHT);
        tfBranches.setOnAction(e -> pane.setDepth(Integer.parseInt(tfOrder.getText()),Integer.parseInt(tfBranches.getText())));
        tfBranches.setPrefColumnCount(4);
        tfBranches.setAlignment(Pos.BOTTOM_RIGHT);


        // Pane to hold label, text field, and a button
        HBox hBox = new HBox(10);
        hBox.getChildren().addAll(new Label("Enter an order: "), tfOrder);
        hBox.getChildren().addAll(new Label("Enter branches: "), tfBranches);
        hBox.setAlignment(Pos.CENTER);

        BorderPane borderPane = new BorderPane();
        borderPane.setCenter(pane);
        borderPane.setBottom(hBox);

        // Create a scene and place it in the stage
        Scene scene = new Scene(borderPane, 200, 210);
        primaryStage.setTitle("Swirls"); // Set the stage title
        primaryStage.setScene(scene); // Place the scene in the stage
        primaryStage.show(); // Display the stage

        scene.widthProperty().addListener(ov -> pane.paintSwirls());
        scene.heightProperty().addListener(ov -> pane.paintSwirls());
    }

    /** Pane for displaying triangles */
    static class SwirlPane extends Pane
    {
        private int depth = 0;
        private int branches = 0;
        private double angleFactor = Math.PI / 5;
        private final double SIZE_FACTOR = 0.58;

        public void setDepth(int depth, int branches)
        {
            this.depth = depth;
            this.branches = branches;
            paintSwirls();
        }


        public void paintSwirls()
        {
            getChildren().clear();

            paintBranch(depth, getWidth() / 2, getHeight() / 2,
                    getHeight() / 4, Math.PI / 12, Color.color(Math.random(), Math.random(), Math.random()));
        }

        public void paintBranch(int depth, double x1, double y1, double length, double angle, Color color)
        {
            if (depth >= 0)
            {
                color = Color.color(Math.random(), Math.random(), Math.random());
                for (int i = 1; i <= branches; i++)
                {
                    double x2 = x1 + Math.cos(angle) * length;
                    double y2 = y1 - Math.sin(angle) * length;

                    Line line = new Line(x1, y1, x2, y2);
                    line.setStroke(color);
                    getChildren().add(line);
                    angle += 2 * Math.PI / branches;

                    paintBranch(depth - 1, x2, y2, length * 0.4, angle + Math.PI / 3, color);
                }
            }
        }
    }

    public static void main(String[] args) {
        launch(args);
    }
}
