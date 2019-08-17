// If there is ambient light then the led should turn on!!
int sensepin = 1;// Defining the ldr sensor at A1
int ledpin = 13;
void setup() 
{
  analogReference(DEFAULT);// It's not needed as it is done by arduino itself
  pinMode(ledpin, OUTPUT);// Initialising the led as output
  pinMode(sensepin, INPUT);

}

void loop() 
{
  int val = analogRead(sensepin);//Reading the value and storing it in another variable
  
  if(val >= 500)
  {
    digitalWrite(ledpin, LOW);
  }
  else
  {
    digitalWrite(ledpin, HIGH);
  }
  
  

}
