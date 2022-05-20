package sample;
import javafx.application.Application;
import javafx.scene.control.*;
import javafx.scene.input.KeyCombination;
import javafx.scene.layout.Pane;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Line;
import javafx.scene.shape.Ellipse;

import java.io.*;
// Johnny Rivera
//This code is for a TicTacToe game where it will add the characters 'O' or 'X' depending on who's turn it is, by default the code makes 'X' start first. There is also a menu system on the window so that the user can restart a new game to clear the game board, there is a "Save as" option
//which saves the current state of the game, a "Load game" option where the user can load in previously saved games, and also an exit menu button which closes the game.

public class TicTacToe extends Application
{
    private char whoseTurn = 'X';

    private Cell[][] cell = new Cell[3][3];

    private Label lblStatus = new Label("X's turn to play");

    @Override
    public void start(Stage primaryStage)
    {
        GridPane pane = new GridPane();
        for(int i = 0; i < 3; i++)
        {
            for(int j = 0; j<3; j++)
            {
                pane.add(cell[i][j] =  new Cell(), j ,i);
            }
        }
        BorderPane borderPane = new BorderPane();
        borderPane.setCenter(pane);
        borderPane.setBottom(lblStatus);

        MenuBar menuBar = new MenuBar();
        Menu menuFile = new Menu("File");
        menuBar.getMenus().addAll(menuFile);
        borderPane.setTop(menuBar);
        MenuItem menuItemNewGame = new MenuItem("New Game");
        MenuItem menuItemSaveAs = new MenuItem("Save As...");
        MenuItem menuItemLoadGame = new MenuItem("Load Game");
        MenuItem menuItemExit = new MenuItem("Exit");
        menuFile.getItems().addAll(menuItemNewGame, new SeparatorMenuItem(), menuItemSaveAs, menuItemLoadGame, new SeparatorMenuItem(), menuItemExit);
        menuItemNewGame.setOnAction(e -> newGame());
        menuItemSaveAs.setOnAction(e -> {
            try
            {
                saveAs(primaryStage);
            }
            catch (IOException ignored)
            {

            } });
        menuItemLoadGame.setOnAction(e ->
        {
            try
            {
                loadGame(primaryStage);
            }
            catch (IOException | ClassNotFoundException ignored)
            {

            } });
        menuItemExit.setOnAction(e -> System.exit(0));

        menuItemNewGame.setAccelerator(
                KeyCombination.keyCombination("Ctrl+N"));
        menuItemSaveAs.setAccelerator(
                KeyCombination.keyCombination("Ctrl+S"));
        menuItemLoadGame.setAccelerator(
                KeyCombination.keyCombination("Ctrl+L"));
        menuItemExit.setAccelerator(
                KeyCombination.keyCombination("Ctrl+X"));

        Scene scene = new Scene(borderPane, 450, 170);
        primaryStage.setTitle("TicTacToe");
        primaryStage.setScene(scene);
        primaryStage.show();
    }
    public void saveAs(Stage primaryStage) throws IOException
    {
        FileChooser fileChooser = new FileChooser();
        fileChooser.setInitialDirectory(new File("."));
        fileChooser.setTitle("Enter file name");
        fileChooser.getExtensionFilters().add(new FileChooser.ExtensionFilter("Tic-Tac-Toe files", "*.ttt"));
        File selectedFile = fileChooser.showSaveDialog(primaryStage);
        try (
                ObjectOutputStream output = new ObjectOutputStream(new FileOutputStream(selectedFile))
        )
        {
            output.writeChar(whoseTurn);
            char[][] cellChars = new char[3][3];
            for( int i = 0; i < 3; i++ )
            {
                for(int j = 0; j < 3; j++)
                {
                    cellChars[i][j] = cell[i][j].getToken();
                }
            }
            output.writeObject(cellChars);
        }
    }

    public void loadGame(Stage primaryStage) throws IOException, ClassNotFoundException {
        FileChooser fileChooser = new FileChooser();
        fileChooser.setInitialDirectory(new File("."));
        fileChooser.getExtensionFilters().add(new FileChooser.ExtensionFilter("Tic-Tac-Toe files", "*.ttt"));
        File selectedFile = fileChooser.showOpenDialog(primaryStage);
        try (
                ObjectInputStream input = new ObjectInputStream(new FileInputStream(selectedFile))
        )
        {
            whoseTurn = input.readChar();
            lblStatus.setText(whoseTurn + "'s turn");
            for(int i = 0; i < 3; i++)
            {
                for(int j = 0;  j < 3; j++)
                {
                    cell[i][j].setToken(' ');
                }
            }
            char[][] cellChar = (char[][])(input.readObject());
            for(int i = 0; i < 3; i++)
            {
                for(int j = 0;  j < 3; j++)
                {
                   cell[i][j].setToken(cellChar[i][j]);
                }
            }
        }
    }
    public void newGame()
    {
        lblStatus.setText(" ");
        whoseTurn = 'X';
        for(int i = 0; i < 3; i++)
        {
            for(int j = 0;  j < 3; j++)
            {
                cell[i][j].setToken(' ');
            }
        }
    }
    public boolean isFull()
    {
        for(int i = 0; i < 3; i++)
        {
            for(int j = 0;  j < 3; j++)
            {
                if(cell[i][j].getToken() == ' ')
                {
                    return false;
                }
            }
        }
        return true;
    }
    public boolean isWon(char token)
    {
        for(int i = 0; i < 3; i++)
        {
            if(cell[i][0].getToken() == token
                    && cell[i][1].getToken() == token
                    && cell[i][2].getToken() == token)
            {
                return true;
            }
        }

        for(int j = 0; j < 3; j++)
        {
            if(cell[0][j].getToken() == token
                    && cell[1][j].getToken() == token
                    && cell[2][j].getToken() == token)
            {
                return true;
            }
        }

        if(cell[0][0].getToken() == token
                && cell[1][1].getToken() == token
                && cell[2][2].getToken() == token)
        {
            return true;
        }

        return cell[0][2].getToken() == token
                && cell[1][1].getToken() == token
                && cell[2][0].getToken() == token;
    }

    public class Cell extends Pane
    {
        private char token = ' ';

        public Cell()
        {
            setStyle("-fx-border-color: black");
            this.setPrefSize(2000,2000);
            this.setOnMouseClicked(e -> handleMouseClick());
        }

        public char getToken()
        {
            return token;
        }

        public void setToken(char c)
        {
            token = c;

            if(token == 'X')
            {
                Line line1 = new Line(10,10, this.getWidth() - 10, this.getHeight() - 10);
                line1.endXProperty().bind(this.widthProperty().subtract(10));
                line1.endYProperty().bind(this.heightProperty().subtract(10));
                Line line2 = new Line(10, this.getHeight() - 10, this.getWidth() - 10, 10);
                line2.startYProperty().bind(this.heightProperty().subtract(10));
                line2.endXProperty().bind(this.widthProperty().subtract(10));
                this.getChildren().addAll(line1,line2);
            }
            else if(token == 'O')
            {
                Ellipse ellipse = new Ellipse(this.getWidth() / 2, this.getHeight() / 2, this.getWidth() / 2 - 10,this.getHeight() / 2 -10);
                ellipse.centerXProperty().bind(this.widthProperty().divide(2));
                ellipse.centerYProperty().bind(this.heightProperty().divide(2));
                ellipse.radiusXProperty().bind(this.widthProperty().divide(2).subtract(10));
                ellipse.radiusYProperty().bind(this.heightProperty().divide(2).subtract(10));
                ellipse.setStroke(Color.BLACK);
                ellipse.setFill(Color.WHITE);
                getChildren().add(ellipse);
            }
            else if(token == ' ')
            {
                this.getChildren().clear();
            }
        }
        private void handleMouseClick()
        {
            if(token == ' ' && whoseTurn != ' ')
            {
                setToken(whoseTurn);
            }
            if(isWon(whoseTurn))
            {
                lblStatus.setText(whoseTurn + " won! The game is over.");
                whoseTurn = ' ';
            }
            else if(isFull())
            {
                lblStatus.setText("Draw! The game is over.");
                whoseTurn = ' ';
            }
            else
            {
                whoseTurn = (whoseTurn == 'X') ? 'O' : 'X';
                lblStatus.setText(whoseTurn + "'s turn");
            }
        }

    }
}
