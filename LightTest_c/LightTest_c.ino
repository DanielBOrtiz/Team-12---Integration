// declare input string
String inputString;

// PWM Variables
int A = 0;
int B = 0;
int AOld = 0;
int BOld = 0;

// Pins for PWMs
int led = 6;

void setup() 
{
  pinMode(led, OUTPUT);
  analogWrite(led, 0);
  
  Serial.begin(9600);
  Serial.println("Ready!");
  inputString = "";
}

void loop() 
{
  if (Serial.available())
  {
    String inputString = "";
    String strArr[2]; // Size of array should equal number of inputs
    
    // See if buffer is available
    while (Serial.available()) 
    {
      // Delay allows for buffer to arrive
      delay(2);
      // Read character from buffer
      char l = Serial.read();
      // Add that character to string
      inputString += l;
    }
      
      int strStart = 0;
      int arrIndex = 0;
      
      for (int i = 0; i < inputString.length(); ++i) 
      {
        if (inputString.charAt(i) == ',')
        {
          // If we detect a comma clear the previous array values
          strArr[arrIndex] = "";
          // Save that substring into an array
          strArr[arrIndex] = inputString.substring(strStart, i);
          // Set new string to starting input
          strStart = (i + 1);
          arrIndex++;
        }
      }
      
      // Save values from array as variables
      String val1 = strArr[0];
      String val2 = strArr[1];
      
      // Convert stirng to integer if needed
      AOld = A;
      BOld = B;
      A = val1.toInt();
      B = val2.toInt();
      light(A);
//      Serial.println(A);
//      Serial.println(B);
    }
}

void light(int pwm)
{
  for (int i = 0; i <= pwm; ++i) 
  {
    analogWrite(led, i);
    Serial.println(i);
    delay(50);
  }
  
  for (int i = 0; i <= pwm; ++i)
  {
    analogWrite(led, 255 - i);
    Serial.println(255 - i);
    delay(50);
  }
}


