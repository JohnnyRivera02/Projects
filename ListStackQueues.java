package sample;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;

//Johnny Rivera
//This program generates expressions to equal 24 using the deck of cards folder in the directory. It will display the card pictures and use their values accordingly. There is 3 buttons, one is to find the solution expression, one is to shuffle the card pictures to new ones, and the last button
//verifies that the expression the user put in with the the numbers of the cards adds up to 24 as well. It will display the result of the calculation accordingly.

public class HW9 extends Application {
  private ArrayList<Integer> list = new ArrayList<>();
  private ImageView imageView1 = new ImageView();
  private ImageView imageView2 = new ImageView();
  private ImageView imageView3 = new ImageView();
  private ImageView imageView4 = new ImageView();
  private TextField tfExpression = new TextField();
  private TextField tfSolution = new TextField();
  
  @Override // Override the start method in the Application class
  public void start(Stage primaryStage) throws FileNotFoundException
  {
    for (int i = 1; i <= 52; i++)
    {
      list.add(i);
    }
 
    VBox vBox = new VBox(5);
    
    ArrayList<Integer> list = new ArrayList<>();
    for (int i = 1; i <= 52; i++)
    {
      list.add(i);
    }
    
    refresh();
    
    HBox hBox = new HBox(5);
    hBox.setAlignment(Pos.CENTER);
    hBox.getChildren().addAll(imageView1, imageView2, imageView3, imageView4);
   
    Label lblStatus = new Label();
    Button btSolution = new Button("Find a Solution");
    Button btShuffle = new Button("Refresh");
    HBox hBoxTop = new HBox(5);
    hBoxTop.setAlignment(Pos.CENTER_RIGHT);
    hBoxTop.getChildren().addAll(btSolution, tfSolution, btShuffle);
    
    HBox hBoxBottom = new HBox(5);
    hBoxBottom.setAlignment(Pos.CENTER);
    Button btVerify = new Button("Verify");
    hBoxBottom.getChildren().addAll(
      new Label("Enter an expression: "), tfExpression, btVerify);

    vBox.getChildren().addAll(hBoxTop, hBox, hBoxBottom, lblStatus);
    
    // Create a scene and place it in the stage
    Scene scene = new Scene(vBox, 370, 200);
    primaryStage.setTitle("Exercise20_15"); // Set the stage title
    primaryStage.setScene(scene); // Place the scene in the stage
    primaryStage.show(); // Display the stage

    btShuffle.setOnAction(e -> {
      try
      {
        refresh();
      } catch (FileNotFoundException exception)
      {
        exception.printStackTrace();
      }
    });
    
    btVerify.setOnAction(e -> {
        if (!correctNumbers())
        {
          lblStatus.setText("The numbers in the expression don't \nmatch the numbers in the set ");
        }
        else
          {
          if (evaluate())
          {
            lblStatus.setText("Correct");
          }
          else
            {
            lblStatus.setText("Incorrect result");
            }
        }
    });
    
    btSolution.setOnAction(e -> tfSolution.setText(Solution()));
  }

  private void refresh() throws FileNotFoundException
  {
    Collections.shuffle(list);

    InputStream stream1 = new FileInputStream("C:\\Users\\crazy\\IdeaProjects\\360JavaFX\\src\\sample\\card\\" + list.get(0) + ".png");
    Image image1 = new Image(stream1);
    imageView1.setImage(image1);

    InputStream stream2 = new FileInputStream("C:\\Users\\crazy\\IdeaProjects\\360JavaFX\\src\\sample\\card\\" + list.get(1) + ".png");
    Image image2 = new Image(stream2);
    imageView2.setImage(image2);

    InputStream stream3 = new FileInputStream("C:\\Users\\crazy\\IdeaProjects\\360JavaFX\\src\\sample\\card\\" + list.get(2) + ".png");
    Image image3 = new Image(stream3);
    imageView3.setImage(image3);

    InputStream stream4 = new FileInputStream("C:\\Users\\crazy\\IdeaProjects\\360JavaFX\\src\\sample\\card\\" + list.get(3) + ".png");
    Image image4 = new Image(stream4);
    imageView4.setImage(image4);

    tfSolution.setText(" ");
    tfExpression.setText(" ");
    //TODO shuffle the card
  }
  
  private boolean evaluate()
  {
    return evaluateExpression(tfExpression.getText().trim()) == 24;
  }
    
  private boolean correctNumbers()
  {
    // Get the card values from the expression
    String[] values = tfExpression.getText().trim().split("[()+-/* ]");
    //String[] values = jtfExpression.getText().trim().split("[+|-|\\*|/| |(|)]");
    ArrayList<Integer> valueList = new ArrayList<>();
    
    ArrayList<Integer> currentCardValues = new ArrayList<>();
    currentCardValues.add((list.get(0) - 1) % 13 + 1);
    currentCardValues.add((list.get(1) - 1) % 13 + 1);
    currentCardValues.add((list.get(2) - 1) % 13 + 1);
    currentCardValues.add((list.get(3) - 1) % 13 + 1);

    for (int i = 0; i < values.length; i++)
    {
      if (values[i].length() > 0)
      {
        valueList.add(Integer.parseInt(values[i]));
      }
    }

    Collections.sort(valueList);
    Collections.sort(currentCardValues);

    if (valueList.equals(currentCardValues))
    {
      return true;
    }
    else
      {
      return false;
      }
  }

    /** Evaluate an expression */
    public  double evaluateExpression(String expression)
    {
    	//TODO evaluate the expression
      Stack<Double> operandStack = new Stack<>();

      // Create operatorStack to store operators
      Stack<Character> operatorStack = new Stack<>();

      expression = insertBlanks(expression);
      // Extract operands and operators
      String[] tokens = expression.split(" ");

      for (String token: tokens)
      {
        if (token.length() == 0)
        {// Blank space
          continue; // Back to the while loop to extract the next token
        }
        else if (token.charAt(0) == '+' || token.charAt(0) == '-')
        {
          // Process all +, -, *, / in the top of the operator stack
          while (!operatorStack.isEmpty() && (operatorStack.peek() == '+' || operatorStack.peek() == '-' || operatorStack.peek() == '*' || operatorStack.peek() == '/'))
          {
            processAnOperator(operandStack, operatorStack);
          }
          // Push the + or - operator into the operator stack
          operatorStack.push(token.charAt(0));
        }
        else if (token.charAt(0) == '*' || token.charAt(0) == '/')
        {
          // Process all *, / in the top of the operator stack
          while (!operatorStack.isEmpty() && (operatorStack.peek() == '*' || operatorStack.peek() == '/'))
          {
            processAnOperator(operandStack, operatorStack);
          }

          // Push the * or / operator into the operator stack
          operatorStack.push(token.charAt(0));
        }
        else if (token.trim().charAt(0) == '(')
        {
          operatorStack.push('('); // Push '(' to stack
        }
        else if (token.trim().charAt(0) == ')')
        {
          // Process all the operators in the stack until seeing '('
          while (operatorStack.peek() != '(')
          {
            processAnOperator(operandStack, operatorStack);
          }

          operatorStack.pop(); // Pop the '(' symbol from the stack
        }
        else
          { // An operand scanned
          // Push an operand to the stack
          operandStack.push((double) Integer.parseInt(token));
          }
      }

      // Phase 2: process all the remaining operators in the stack
      while (!operatorStack.isEmpty())
      {
        processAnOperator(operandStack, operatorStack);
      }
      // Return the result
      return operandStack.pop();
    }

    /**
     * Process one operator: Take an operator from operatorStack and apply it on
     * the operands in the operandStack
     */
    public void processAnOperator(Stack<Double> operandStack, Stack<Character> operatorStack)
    {
      double op1, op2;
      if (operatorStack.peek() == '+')
      {
        operatorStack.pop();
        op1 = Double.parseDouble(String.valueOf(operandStack.pop()));
        op2 = Double.parseDouble(String.valueOf(operandStack.pop()));
        operandStack.push(op2 + op1);
      }
      else if (operatorStack.peek() == '-')
      {
        operatorStack.pop();
        op1 = Double.parseDouble(String.valueOf(operandStack.pop()));
        op2 = Double.parseDouble(String.valueOf(operandStack.pop()));
        operandStack.push(op2 - op1);
      }
      else if (operatorStack.peek() == '*')
      {
        operatorStack.pop();
        op1 = Double.parseDouble(String.valueOf(operandStack.pop()));
        op2 = Double.parseDouble(String.valueOf(operandStack.pop()));
        operandStack.push(op2 * op1);
      }
      else if (operatorStack.peek() == '/')
      {
        operatorStack.pop();
        op1 = Double.parseDouble(String.valueOf(operandStack.pop()));
        op2 = Double.parseDouble(String.valueOf(operandStack.pop()));
        operandStack.push(op2 / op1);
      }
    }

  public static String insertBlanks(String s)
  {
    String result = "";

    for (int i = 0; i < s.length(); i++)
    {
      if (s.charAt(i) == '(' || s.charAt(i) == ')' || s.charAt(i) == '+' || s.charAt(i) == '-' || s.charAt(i) == '*' || s.charAt(i) == '/')
      {
        result += " " + s.charAt(i) + " ";
      }
      else
        {
        result += s.charAt(i);
        }
    }
    return result;
  }
  /* Get four card values and find a solution */
  public String Solution()
  {
    int a = (list.get(0) - 1) % 13 + 1;
    int b = (list.get(1) - 1) % 13 + 1;
    int c = (list.get(2) - 1) % 13 + 1;
    int d = (list.get(3) - 1) % 13 + 1;
    String finalResult = findSolution(a, b, c, d);
    if (!finalResult.equals("No solution"))
    {
      finalResult = finalResult + " = 24";
    }
    return finalResult;
  }

  public String findSolution(int a, int b, int c, int d)
  {
	//TODO find a solution automatically
    String solution;
    String noSolution = "No solution";
    String[] operators = {"+", "-", "*", "/"};
    int[][] allCombinations = {{a, b, c, d}, {d, a, b, c}, {c, d, a, b}, {b, c, d, a}, {a, b, d, c}, {c, a, b, d},
            {d, c, a, b}, {b, d, c, a}, {a, d, c, b}, {b, a, d, c}, {c, b, a, d}, {d, c, b, a}, {a, c, b, d},
            {d, a, c, b}, {b, d, a, c}, {c, b, d, a}, {b, a, c, d}, {d, b, a, c}, {c, d, b, a}, {a, c, d, b},
            {a, d, b, c}, {c, a, d, b}, {b, c, a, d}, {d, b, c, a}};

    for (String firstOp : operators)
    {
      for (String secondOp : operators)
      {
        for (String thirdOp : operators)
        {
          for (int[] cardNums : allCombinations)
          {
            for (int i = 0; i < 3; i++)
            {
              for (int j = 0; j < 5; j++)
              {
                if (i == 0)
                {
                  if (j == 0)
                  {
                    solution = cardNums[0] + firstOp + cardNums[1] + secondOp + cardNums[2] + thirdOp + cardNums[3];
                    if (evaluateExpression(solution) == 24)
                    {
                      return solution;
                    }
                  }
                  else if (j == 1)
                  {
                    solution = "(" + cardNums[0] + firstOp + cardNums[1] + ")" + secondOp + cardNums[2] + thirdOp + cardNums[3];
                    if (evaluateExpression(solution) == 24)
                    {
                      return solution;
                    }
                  }
                  else if (j == 2)
                  {
                    solution = cardNums[0] + firstOp + "(" + cardNums[1] + secondOp + cardNums[2] + ")" + thirdOp + cardNums[3];
                    if (evaluateExpression(solution) == 24)
                    {
                      return solution;
                    }
                  }
                  else if (j == 3)
                  {
                    solution = cardNums[0] + firstOp + cardNums[1] + secondOp + "(" + cardNums[2] + thirdOp + cardNums[3] + ")";
                    if (evaluateExpression(solution) == 24)
                    {
                      return solution;
                    }
                  }
                  else if (j == 4)
                  {
                    solution = "(" + cardNums[0] + firstOp + cardNums[1] + ")" + secondOp + "(" + cardNums[2] + thirdOp + cardNums[3] + ")";
                    if (evaluateExpression(solution) == 24)
                    {
                      return solution;
                    }
                  }
                }
                else if (i == 1)
                {
                  if (j == 0)
                  {
                    solution = "(" + cardNums[0] + firstOp + cardNums[1] + secondOp + cardNums[2] + ")" + thirdOp + cardNums[3];
                    if (evaluateExpression(solution) == 24)
                    {
                      return solution;
                    }
                  }
                  else if (j == 1)
                  {
                    solution = "((" + cardNums[0] + firstOp + cardNums[1] + ")" + secondOp + cardNums[2] + ")" + thirdOp + cardNums[3];
                    if (evaluateExpression(solution) == 24)
                    {
                      return solution;
                    }
                  }
                  else if (j == 2)
                  {
                    solution = "(" + cardNums[0] + firstOp + "(" + cardNums[1] + secondOp + cardNums[2] + "))" + thirdOp + cardNums[3];
                    if (evaluateExpression(solution) == 24)
                    {
                      return solution;
                    }
                  }
                }
                else if (i == 2)
                {
                  if (j == 0)
                  {
                    solution = cardNums[0] + firstOp + "(" + cardNums[1] + secondOp + cardNums[2] + thirdOp + cardNums[3] + ")";
                    if (evaluateExpression(solution) == 24)
                    {
                      return solution;
                    }
                  }
                  else if (j == 1)
                  {
                    solution = cardNums[0] + firstOp + "((" + cardNums[1] + secondOp + cardNums[2] + ")" + thirdOp + cardNums[3] + ")";
                    if (evaluateExpression(solution) == 24)
                    {
                      return solution;
                    }
                  }
                  else if (j == 2)
                  {
                    solution = cardNums[0] + firstOp + "(" + cardNums[1] + secondOp + "(" + cardNums[2] + thirdOp + cardNums[3] + "))";
                    if (evaluateExpression(solution) == 24)
                    {
                      return solution;
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    return noSolution;
  }
  
  /**
   * The main method is only needed for the IDE with limited
   * JavaFX support. Not needed for running from the command line.
   */
  public static void main(String[] args)
  {
    launch(args);
  }
}
