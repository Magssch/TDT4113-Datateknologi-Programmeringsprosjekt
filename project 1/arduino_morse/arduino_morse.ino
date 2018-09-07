const int button = 13;
const int led1 = 12; 
const int led2 = 8; 
const int led3 = 7; 

int buttonState = LOW;                        // previous button-state
int _buttonState = LOW;                       // current button-state
int timeCounter = 0;                          // time since last change of state
int pauseCounter = 0;                         // time of pause
int pressCounter = 0;                         // time of press
int debounceBuffer = 80;                      // buffer to avoid electrical interference
bool started = false;                         // toggle to deactivate system

void setup() {
  pinMode(button, INPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  timeCounter = millis();
  Serial.begin(9600);
}

void morseAlong(bool buttonPress) {           // Send byte to python script and display visual feedback
  if(buttonPress) {
    if(pressCounter <= 300) {
      Serial.print('0');                      // dot
      displayCode(0,1,0);
    } else if(pressCounter <= 900) {
      Serial.print('1');                      // dash
      displayCode(1,1,1);
    } else if(pressCounter > 1200) {
      Serial.print('4');                      // Reset if pressed for too long
      displayCode(1,0,0);                     // Cool reset animation ;-)
      delay(100);
      displayCode(0,1,0);
      delay(100);
      displayCode(0,0,1);
      delay(100);
      displayCode(1,0,1);
      delay(1500);
      started = false;                        // Deactivate system
    }
  } else {
    if(pauseCounter >= 600 && pauseCounter <= 1500) {
      Serial.print('2');                      // short pause (symbol)
    } else if(pauseCounter > 1500) {
      Serial.print('3');                      // long pause (word)
    }   
  }
}

void displayCode(int _led1, int _led2, int _led3) {
   digitalWrite(led1, _led1);
   digitalWrite(led2, _led2);
   digitalWrite(led3, _led3);
}

void loop() {

  _buttonState = digitalRead(button);

  
  if(millis()-timeCounter > 150) {            // Remove visual light before symbol time limit in order to aid the user.
    displayCode(0,0,0);
  }
  
  if(!started && _buttonState == HIGH) {      // If system is inactive and button is pressed, begin message.
    buttonState = LOW;                        // Reset parameters and counters.
    started = true;
    pauseCounter = 0;
    pressCounter = 0;
    timeCounter = 0;
  }

  if(_buttonState != buttonState && (millis()-timeCounter > debounceBuffer) && started) {     
                                              // ^Check if button state has changed,
                                              // using debouncing and checking if message has begun.
    if(_buttonState == HIGH) {                // Was button not pressed previously?
      pauseCounter = millis() - timeCounter;  // Set time of pause
      morseAlong(false);                      // Pass along signal to Python script
      buttonState = HIGH;                     // Set current buttonState to HIGH
    } else {
      pressCounter = millis() - timeCounter;  // Set time of press
      morseAlong(true);                       // Pass along signal to Python script
      buttonState = LOW;                      // Set current buttonState to HIGH
    }
      timeCounter = millis();                 // Reset counter
  }

}
