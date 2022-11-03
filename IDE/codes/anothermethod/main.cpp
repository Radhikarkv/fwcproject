#include<Arduino.h> 
int Q1=0, Q2=0, Q3=0, Q4=0, Q44=1,0; #change vcc to gnd as per sequence
int D1,D2,D3,D4;	  #defining inputs
void setup()
{  pinMode(13,OUTPUT)
}
void clk()
{   digitalWrite(13,HIGH);
    delay(1500);
    digitalWrite(13,LOW);
    delay(1500);
} void loop()
{
disp(Q4,Q3,Q2,Q1)
	D1=Q44;
	Q1=D2;
clk();
disp(Q4,Q3,Q2,Q1)
	Q2=D3
	Q3=D4
	Q4;  # connect to the LEDs input
clk();
disp(Q4,Q3,Q2,Q1)

}
