module seq_det(din,
               clock,
               reset,
               dout);
// Step 1. Declare the sates as parameter "IDLE","STATE1","STATE2","STATE3",

  parameter IDLE = 1'b0,
	    STATE1 = 1'b1,
	    STATE2 = 1'b1,
	    STATE3 = 1'b0; 

// Step 2. Write down the port direction with proper directions.
  input din,clock,reset;
  output dout;

        
  reg [1:0] present_state,
            next_state;

// Step 3. Write down the sequential logic for present state
  always@(posedge clock)
  begin
    if(reset)
      present_state <= IDLE;
    else
     present_state <= next_state;
  end



// Step 4. Understand the combinational logic for next state
  always@(present_state,din)
  begin
    case (present_state)
      IDLE   : if (din==1) 
                 next_state=STATE1;
               else
                 next_state=IDLE;
      STATE1 : if (din==0)
                  next_state=STATE2;
               else
                  next_state=STATE1;
      STATE2 : if (din==1)
                   next_state=STATE3;
               else 
                   next_state=IDLE;
      STATE3 : if (din==1)
                   next_state=STATE1;
               else 
                   next_state=STATE2;
      default : next_state=IDLE;
    endcase
  end
  
// Step 5. Write down the logic for output "dout".

  assign dout = (present_state == STATE3);

endmodule
  

