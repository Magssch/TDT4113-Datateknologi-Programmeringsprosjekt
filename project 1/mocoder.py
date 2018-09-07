
import arduino_connect  # This is the key import so that you can access the serial port.

# Codes for the 5 signals sent to this level from the Arduino

_dot = 0
_dash = 1
_symbol_pause = 2
_word_pause = 3
_reset = 4


# Morse Code Class
class mocoder():

# HOW TO WRITE MAGNUS:

#M:   11
#A:   01
#G:   110
#N:   10
#U:   001
#S:   000

    _morse_codes = {'01':'a','1000':'b','1010':'c','100':'d','0':'e','0010':'f','110':'g','0000':'h','00':'i','0111':'j',
               '101':'k','0100':'l','11':'m','10':'n','111':'o','0110':'p','1101':'q','010':'r','000':'s','1':'t',
               '001':'u','0001':'v','011':'w','1001':'x','1011':'y','1100':'z','01111':'1','00111':'2','00011':'3',
               '00001':'4','00000':'5','10000':'6','11000':'7','11100':'8','11110':'9','11111':'0'}

	# This is where you set up the connection to the serial port.
    def __init__(self,sport=True):
        if sport:
            self.serial_port = arduino_connect.pc_connect()
        self.reset()

    # Reset script
    def reset(self):
        self.current_message = ''
        self.current_word = ''
        self.current_symbol = ''

    # This receives an integer in range 0-4 from the Arduino via a serial port
    def read_one_signal(self,port=None):
        connection = port if port else self.serial_port
        while True:
            # Reads the input from the arduino serial connection
            data = connection.readline()
            if data:
                return data

    # Update the current symbol input.
    def update_current_symbol(self, signal):
        self.current_symbol += signal

    # End input of current symbol and begin new.
    def handle_symbol_end(self):
        try:
            code = self._morse_codes[self.current_symbol]
            self.update_current_word(code)
            print(code)
            self.current_symbol = ''
        except KeyError:
            print("Error: Invalid morse-code input")

    # Update the current word input.
    def update_current_word(self, symbol):
        self.current_word += symbol

    # End input of current word and begin new.
    def handle_word_end(self):
        self.handle_symbol_end()
        print("\t"+self.current_word)
        self.reset()

    def decoding_loop(self):
        while True:
            s = self.read_one_signal(self.serial_port)
            print(s)
            for byte in s:
                self.process_signal(int(chr(byte)))
     
     # Classify input type
    def process_signal(self, sig):
        if sig == 0 or sig == 1:
            self.update_current_symbol(str(sig))
        elif sig == 2:
            self.handle_symbol_end()
        elif sig == 3:
            self.handle_word_end()
        elif sig == 4:
            print("\nMORSE RESET\n")
            self.reset()

    # Run methods.
def run():
    m = mocoder()
    m.decoding_loop()
run()
