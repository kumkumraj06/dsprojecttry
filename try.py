import streamlit as st
st.title("Automated verilog code generator for adders and multiplier")
st.markdown("Project by Sneha, Dheekshitha and Kumkum")
def generate_verilog_code(bit_width, operation, type):
    # Generate Verilog code based on selected options
    code = f"""
    // Verilog code for {"Kogge-stone"} {"Adder"} with {8}-bit inputs
    module function1(output G,P,input Gi,Pi,GiPrev,PiPrev);
wire a;
and(a,Pi,GiPrev);
or(G,a,Gi);
and(P,Pi,PiPrev);
endmodule
module function2(output Ci,input Gi);
buf(Ci,Gi);
endmodule
module function3(output G,P,input Ai,Bi);
and(G,Ai,Bi);
xor(P,Ai,Bi);
endmodule
module function4(output Si,input Pi,CiPrev);
xor(Si,Pi,CiPrev);
endmodule
module KSA8(output [7:0]sum,output cout,input [7:0]a,b);
wire cin=1'b0;
wire [7:0]c;
wire [7:0]g,p;
function3 sq[7:0](g,p,a,b);
wire [7:1]g2,p2;
function2 sc0_0(c[0],g[0]);
function1 f10[7:1](g2[7:1],p2[7:1],g[7:1],p[7:1],g[6:0],p[6:0]);
wire [7:3]g3,p3;
function2 f21[2:1](c[2:1],g2[2:1]);
function1 f11[7:3](g3[7:3],p3[7:3],g2[7:3],p2[7:3],g2[5:1],p2[5:1]);
wire [7:7]g4,p4;
function2 f22[6:3](c[6:3],g3[6:3]);
function1 f12_7(g4[7],p4[7],g3[7],p3[7],g3[3],p3[3]);
function2 f23_7(c[7],g4[7]);
function4 f40(sum[0],p[0],cin);
function4 f4[7:1](sum[7:1],p[7:1],c[6:0]);
buf(cout,c[7]);
endmodule

// Verilog code for {"Kogge-stone"} {"Adder"} with {16}-bit inputs
module KSA16(output [15:0]sum,output cout,input [15:0]a,b);
wire cin=1'b0;
wire [15:0]c;
wire [15:0]g,p;
function3 f3[15:0](g,p,a,b);
wire [15:1]g2,p2;
function2 f20_0(c[0],g[0]);
function1 f10[15:1](g2[15:1],p2[15:1],g[15:1],p[15:1],g[14:0],p[14:0]);
wire [15:3]g3,p3;
function2 f21[2:1](c[2:1],g2[2:1]);
function1 f11[15:3](g3[15:3],p3[15:3],g2[15:3],p2[15:3],g2[13:1],p2[13:1]);
wire [15:7]g4,p4;
function2 f22[6:3](c[6:3],g3[6:3]);
function1 f12[15:7](g4[15:7],p4[15:7],g3[15:7],p3[15:7],g3[11:3],p3[11:3]);
wire [15:15]g5,p5;
function2 f23[14:7](c[14:7],g4[14:7]);
function1 f13_15(g5[15],p5[15],g4[15],p4[15],g4[7],p4[7]);
function2 f24_15(c[15],g5[15]);
function4 f40(sum[0],p[0],cin);
function4 f4[15:1](sum[15:1],p[15:1],c[14:0]);
buf(cout,c[15]);
endmodule

// Verilog code for {"Kogge-stone"} {"Adder"} with {32}-bit inputs
module KSA32(output [31:0]sum,output cout,input [31:0]a,b);
wire cin=1'b0;
wire [31:0]c;
wire [31:0]g,p;
function3 f3[31:0](g,p,a,b);
wire [31:1]g2,p2;
function2 f20_0(c[0],g[0]);
function1 f10[31:1](g2[31:1],p2[31:1],g[31:1],p[31:1],g[30:0],p[30:0]);
wire [31:3]g3,p3;
function2 f21[2:1](c[2:1],g2[2:1]);
function1 f11[31:3](g3[31:3],p3[31:3],g2[31:3],p2[31:3],g2[29:1],p2[29:1]);
wire [31:7]g4,p4;
function2 f22[6:3](c[6:3],g3[6:3]);
function1 f12[31:7](g4[31:7],p4[31:7],g3[31:7],p3[31:7],g3[27:3],p3[27:3]);
wire [31:15]g5,p5;
function2 f23[14:7](c[14:7],g4[14:7]);
function1 f13[31:15](g5[31:15],p5[31:15],g4[31:15],p4[31:15],g4[23:7],p4[23:7]);
wire [31:31]g6,p6;
function2 f24[30:15](c[30:15],g5[30:15]);
function1 f14_31(g6[31],p6[31],g5[31],p5[31],g5[15],p5[15]);
function2 f25_31(c[31],g6[31]);
function4 f40(sum[0],p[0],cin);
function4 f4[31:1](sum[31:1],p[31:1],c[30:0]);
buf(cout,c[31]);
endmodule

    """
    return code

#maincode

import streamlit as st

def generate_verilog_code(bit_width, operation, type):
    # Generate Verilog code based on selected options
    code = ""
    if bit_width == 8 and operation == "Adder" and type == "Kogge-stone":
        # Verilog code for 8-bit Kogge-stone Adder
        code = """
        // Verilog code for 8-bit Kogge-stone Adder
        module function1(output G,P,input Gi,Pi,GiPrev,PiPrev);
wire a;
and(a,Pi,GiPrev);
or(G,a,Gi);
and(P,Pi,PiPrev);
endmodule
module function2(output Ci,input Gi);
buf(Ci,Gi);
endmodule
module function3(output G,P,input Ai,Bi);
and(G,Ai,Bi);
xor(P,Ai,Bi);
endmodule
module function4(output Si,input Pi,CiPrev);
xor(Si,Pi,CiPrev);
endmodule
module KSA8(output [7:0]sum,output cout,input [7:0]a,b);
wire cin=1'b0;
wire [7:0]c;
wire [7:0]g,p;
function3 sq[7:0](g,p,a,b);
wire [7:1]g2,p2;
function2 sc0_0(c[0],g[0]);
function1 f10[7:1](g2[7:1],p2[7:1],g[7:1],p[7:1],g[6:0],p[6:0]);
wire [7:3]g3,p3;
function2 f21[2:1](c[2:1],g2[2:1]);
function1 f11[7:3](g3[7:3],p3[7:3],g2[7:3],p2[7:3],g2[5:1],p2[5:1]);
wire [7:7]g4,p4;
function2 f22[6:3](c[6:3],g3[6:3]);
function1 f12_7(g4[7],p4[7],g3[7],p3[7],g3[3],p3[3]);
function2 f23_7(c[7],g4[7]);
function4 f40(sum[0],p[0],cin);
function4 f4[7:1](sum[7:1],p[7:1],c[6:0]);
buf(cout,c[7]);
endmodule

//Testbench
`timescale 1ns/1ps
module KSAtb8();
reg [7:0]a;
reg [7:0]b;
wire [7:0]sum;
wire cout;
KSA8 uut(sum,cout,a,b);
initial
begin
a=8'b00110110;b=8'b00011100;
#5
a=8'b11111000;b=8'b10011100;
#5
$finish();
end
endmodule

        """
    elif bit_width == 16 and operation == "Adder" and type == "Kogge-stone":
        # Verilog code for 16-bit Kogge-stone Adder
        code = """
        // Verilog code for 16-bit Kogge-stone Adder
        module function1(output G,P,input Gi,Pi,GiPrev,PiPrev);
wire a;
and(a,Pi,GiPrev);
or(G,a,Gi);
and(P,Pi,PiPrev);
endmodule
module function2(output Ci,input Gi);
buf(Ci,Gi);
endmodule
module function3(output G,P,input Ai,Bi);
and(G,Ai,Bi);
xor(P,Ai,Bi);
endmodule
module function4(output Si,input Pi,CiPrev);
xor(Si,Pi,CiPrev);
endmodule
        module KSA16(output [15:0]sum,output cout,input [15:0]a,b);
        wire cin=1'b0;
        wire [15:0]c;
        wire [15:0]g,p;
        function3 f3[15:0](g,p,a,b);
        wire [15:1]g2,p2;
        function2 f20_0(c[0],g[0]);
        function1 f10[15:1](g2[15:1],p2[15:1],g[15:1],p[15:1],g[14:0],p[14:0]);
        wire [15:3]g3,p3;
        function2 f21[2:1](c[2:1],g2[2:1]);
        function1 f11[15:3](g3[15:3],p3[15:3],g2[15:3],p2[15:3],g2[13:1],p2[13:1]);
        wire [15:7]g4,p4;
        function2 f22[6:3](c[6:3],g3[6:3]);
        function1 f12[15:7](g4[15:7],p4[15:7],g3[15:7],p3[15:7],g3[11:3],p3[11:3]);
        wire [15:15]g5,p5;
        function2 f23[14:7](c[14:7],g4[14:7]);
        function1 f13_15(g5[15],p5[15],g4[15],p4[15],g4[7],p4[7]);
        function2 f24_15(c[15],g5[15]);
        function4 f40(sum[0],p[0],cin);
        function4 f4[15:1](sum[15:1],p[15:1],c[14:0]);
        buf(cout,c[15]);
         endmodule
         
        // Testbench
        `timescale 1ns/1ps
module KSAtb16();
reg [15:0]a;
reg [15:0]b;
wire [15:0]sum;
wire cout;
KSA16 uut(sum,cout,a,b);
initial
begin
a=16'b0010101010010110;b=16'b0011110000011100;
#5
a=16'b1111100011101000;b=16'b1001100111001100;
#5
$finish();
end
endmodule
        """
    elif bit_width == 32 and operation == "Adder" and type == "Kogge-stone":
        # Verilog code for 32-bit Kogge-stone Adder
        code = """
        // Verilog code for 32-bit Kogge-stone Adder
        module function1(output G,P,input Gi,Pi,GiPrev,PiPrev);
wire a;
and(a,Pi,GiPrev);
or(G,a,Gi);
and(P,Pi,PiPrev);
endmodule
module function2(output Ci,input Gi);
buf(Ci,Gi);
endmodule
module function3(output G,P,input Ai,Bi);
and(G,Ai,Bi);
xor(P,Ai,Bi);
endmodule
module function4(output Si,input Pi,CiPrev);
xor(Si,Pi,CiPrev);
endmodule
        module KSA32(output [31:0]sum,output cout,input [31:0]a,b);
wire cin=1'b0;
wire [31:0]c;
wire [31:0]g,p;
function3 f3[31:0](g,p,a,b);
wire [31:1]g2,p2;
function2 f20_0(c[0],g[0]);
function1 f10[31:1](g2[31:1],p2[31:1],g[31:1],p[31:1],g[30:0],p[30:0]);
wire [31:3]g3,p3;
function2 f21[2:1](c[2:1],g2[2:1]);
function1 f11[31:3](g3[31:3],p3[31:3],g2[31:3],p2[31:3],g2[29:1],p2[29:1]);
wire [31:7]g4,p4;
function2 f22[6:3](c[6:3],g3[6:3]);
function1 f12[31:7](g4[31:7],p4[31:7],g3[31:7],p3[31:7],g3[27:3],p3[27:3]);
wire [31:15]g5,p5;
function2 f23[14:7](c[14:7],g4[14:7]);
function1 f13[31:15](g5[31:15],p5[31:15],g4[31:15],p4[31:15],g4[23:7],p4[23:7]);
wire [31:31]g6,p6;
function2 f24[30:15](c[30:15],g5[30:15]);
function1 f14_31(g6[31],p6[31],g5[31],p5[31],g5[15],p5[15]);
function2 f25_31(c[31],g6[31]);
function4 f40(sum[0],p[0],cin);
function4 f4[31:1](sum[31:1],p[31:1],c[30:0]);
buf(cout,c[31]);
endmodule

//Testbench
`timescale 1ns/1ps
module KSAtb32();
reg [31:0]a;
reg [31:0]b;
wire [31:0]sum;
wire cout;
KSA32 uut(sum,cout,a,b);
initial
begin
a=32'b00000011110000111100000001110110;b=32'b11100010100000110101011000111100;
#5
a=32'b11111111111101100000000000000000;b=32'b10100101010101000010100010111100;
#5
$finish();
end
endmodule
        """
    if bit_width == 8 and operation == "Adder" and type == "Brent Kung":
        # Verilog code for 8-bit Brent Kung Adder
        code = """
        // Verilog code for 8-bit Kogge-stone Adder//
        """
    elif bit_width == 16 and operation == "Adder" and type == "Brent Kung":
        # Verilog code for 16-bit Brent Kung Adder
        code = """
        """
    elif bit_width == 16 and operation == "Adder" and type == "Brent Kung":
        # Verilog code for 16-bit Brent Kung Adder
        code = """
        """
    if bit_width == 8 and operation == "Multiplier" and type == "Wallace Tree":
        # Verilog code for 8-bit Wallace Tree
        code = """
        // Verilog code for 8-bit Wallace Tree//
        module fa(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum=a^b^cin;
assign cout=a&b|b&cin|cin&a;
endmodule
module ha(a,b,sum,cout);
input a,b;
output sum,cout;
assign sum=a^b;
assign cout=a&b;
endmodule
module wall8bit(a,b,asn);
input [7:0]a;
input [7:0]b;
output [15:0]asn;
wire [7:0] p1,p2,p3,p4,p5,p6,p7,p8;
wire [15:0] c1p1,c1p2,c1p3,c1p4,c1p5,c1p6;
wire [15:0] s1p1,s1p2,s1p3,s1p4,s1p5,s1p6;
wire c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12;
assign p1[0] = a[0]&b[0];
assign p1[1] = a[1]&b[0];
assign p1[2] = a[2]&b[0];
assign p1[3] = a[3]&b[0];
assign p1[4] = a[4]&b[0];
assign p1[5] = a[5]&b[0];
assign p1[6] = a[6]&b[0];
assign p1[7] = a[7]&b[0];
assign p2[0] = a[0]&b[1];
assign p2[1] = a[1]&b[1];
assign p2[2] = a[2]&b[1];
assign p2[3] = a[3]&b[1];
assign p2[4] = a[4]&b[1];
assign p2[5] = a[5]&b[1];
assign p2[6] = a[6]&b[1];
assign p2[7] = a[7]&b[1];
assign p3[0] = a[0]&b[2];
assign p3[1] = a[1]&b[2];
assign p3[2] = a[2]&b[2];
assign p3[3] = a[3]&b[2];
assign p3[4] = a[4]&b[2];
assign p3[5] = a[5]&b[2];
assign p3[6] = a[6]&b[2];
assign p3[7] = a[7]&b[2];
assign p4[0] = a[0]&b[3];
assign p4[1] = a[1]&b[3];
assign p4[2] = a[2]&b[3];
assign p4[3] = a[3]&b[3];
assign p4[4] = a[4]&b[3];
assign p4[5] = a[5]&b[3];
assign p4[6] = a[6]&b[3];
assign p4[7] = a[7]&b[3];
assign p5[0] = a[0]&b[4];
assign p5[1] = a[1]&b[4];
assign p5[2] = a[2]&b[4];
assign p5[3] = a[3]&b[4];
assign p5[4] = a[4]&b[4];
assign p5[5] = a[5]&b[4];
assign p5[6] = a[6]&b[4];
assign p5[7] = a[7]&b[4];
assign p6[0] = a[0]&b[5];
assign p6[1] = a[1]&b[5];
assign p6[2] = a[2]&b[5];
assign p6[3] = a[3]&b[5];
assign p6[4] = a[4]&b[5];
assign p6[5] = a[5]&b[5];
assign p6[6] = a[6]&b[5];
assign p6[7] = a[7]&b[5];
assign p7[0] = a[0]&b[6];
assign p7[1] = a[1]&b[6];
assign p7[2] = a[2]&b[6];
assign p7[3] = a[3]&b[6];
assign p7[4] = a[4]&b[6];
assign p7[5] = a[5]&b[6];
assign p7[6] = a[6]&b[6];
assign p7[7] = a[7]&b[6];
assign p8[0] = a[0]&b[7];
assign p8[1] = a[1]&b[7];
assign p8[2] = a[2]&b[7];
assign p8[3] = a[3]&b[7];
assign p8[4] = a[4]&b[7];
assign p8[5] = a[5]&b[7];
assign p8[6] = a[6]&b[7];
assign p8[7] = a[7]&b[7];
assign s1p1[0] = p1[0];
ha h0( p1[1],p2[0],s1p1[1],c1p1[0] );
fa h1(p1[2],p2[1],p3[0],s1p1[2],c1p1[1]);
fa h2(p1[3],p2[2],p3[1],s1p1[3],c1p1[2]);
fa h3(p1[4],p2[3],p3[2],s1p1[4],c1p1[3]);
fa h4(p1[5],p2[4],p3[3],s1p1[5],c1p1[4]);
fa h5(p1[6],p2[5],p3[4],s1p1[6],c1p1[5]);
fa h6(p1[7],p2[6],p3[5],s1p1[7],c1p1[6]);
ha h7(p2[7],p3[6],s1p1[8],c1p1[7]);
assign s1p1[9] = p3[7];
assign s1p2[0] = p4[0];
ha h9( p4[1],p5[0],s1p2[1],c1p2[0] );
fa h10(p4[2],p5[1],p6[0],s1p2[2],c1p2[1]);
fa h11(p4[3],p5[2],p6[1],s1p2[3],c1p2[2]);
fa h12(p4[4],p5[3],p6[2],s1p2[4],c1p2[3]);
fa h13(p4[5],p5[4],p6[3],s1p2[5],c1p2[4]);
fa h14(p4[6],p5[5],p6[4],s1p2[6],c1p2[5]);
fa h15(p4[7],p5[6],p6[5],s1p2[7],c1p2[6]);
ha h16(p5[7],p6[6],s1p2[8],c1p2[7]);
assign s1p2[9] = p6[7];
assign s1p3[0] = s1p1[0];
assign s1p3[1] = s1p1[1];
ha h17(s1p1[2],c1p1[0],s1p3[2],c1p3[0]);
fa h18(s1p1[3],c1p1[1],s1p2[0],s1p3[3],c1p3[1]);
fa h19(s1p1[4],c1p1[2],s1p2[1],s1p3[4],c1p3[2]);
fa h20(s1p1[5],c1p1[3],s1p2[2],s1p3[5],c1p3[3]);
fa h21(s1p1[6],c1p1[4],s1p2[3],s1p3[6],c1p3[4]);
fa h22(s1p1[7],c1p1[5],s1p2[4],s1p3[7],c1p3[5]);
fa h23(s1p1[8],c1p1[6],s1p2[5],s1p3[8],c1p3[6]);
fa h24(s1p1[9],c1p1[7],s1p2[6],s1p3[9],c1p3[7]);
assign s1p3[10] = s1p2[7];
assign s1p3[11] = s1p2[8];
assign s1p3[12] = s1p2[9];
assign s1p4[0] = c1p2[0];
ha h25(c1p2[1],p7[0],s1p4[1],c1p4[0]);
fa h26(c1p2[2],p7[1],p8[0],s1p4[2],c1p4[1]);
fa h27(c1p2[3],p7[2],p8[1],s1p4[3],c1p4[2]);
fa h28(c1p2[4],p7[3],p8[2],s1p4[4],c1p4[3]);
fa h29(c1p2[5],p7[4],p8[3],s1p4[5],c1p4[4]);
fa h30(c1p2[6],p7[5],p8[4],s1p4[6],c1p4[5]);
fa h31(c1p2[7],p7[6],p8[5],s1p4[7],c1p4[6]);
ha h32(p7[7],p8[6],s1p4[8],c1p4[7]);
assign s1p4[9] = p8[7];
assign s1p5[0] = s1p3[0];
assign s1p5[1] = s1p3[1];
assign s1p5[2] = s1p3[2];
ha h33(s1p3[3],c1p3[0],s1p5[3],c1p5[0]);
ha h41(s1p3[4],c1p3[1],s1p5[4],c1p5[1]);
fa h34(s1p3[5],c1p3[2],s1p4[0],s1p5[5],c1p5[2]);
fa h35(s1p3[6],c1p3[3],s1p4[1],s1p5[6],c1p5[3]);
fa h36(s1p3[7],c1p3[4],s1p4[2],s1p5[7],c1p5[4]);
fa h37(s1p3[8],c1p3[5],s1p4[3],s1p5[8],c1p5[5]);
fa h38(s1p3[9],c1p3[6],s1p4[4],s1p5[9],c1p5[6]);
fa h39(s1p3[10],c1p3[7],s1p4[5],s1p5[10],c1p5[7]);
ha h40(s1p3[11],s1p4[6],s1p5[11],c1p5[8]);
ha h42(s1p3[12],s1p4[7],s1p5[12],c1p5[9]);
assign s1p5[13] = s1p4[8];
assign s1p5[14] = s1p4[9];
assign s1p6[0] = s1p5[0];
assign s1p6[1] = s1p5[1];
assign s1p6[2] = s1p5[2];
assign s1p6[3] = s1p5[3];
ha h43(s1p5[4],c1p5[0],s1p6[4],c1p6[0]);
ha h44(s1p5[5],c1p5[1],s1p6[5],c1p6[1]);
ha h45(s1p5[6],c1p5[2],s1p6[6],c1p6[2]);
fa f1(s1p5[7],c1p5[3],c1p4[0],s1p6[7],c1p6[3]);
fa f2(s1p5[8],c1p5[4],c1p4[1],s1p6[8],c1p6[4]);
fa f3(s1p5[9],c1p5[5],c1p4[2],s1p6[9],c1p6[5]);
fa f4(s1p5[10],c1p5[6],c1p4[3],s1p6[10],c1p6[6]);
fa f5(s1p5[11],c1p5[7],c1p4[4],s1p6[11],c1p6[7]);
fa f6(s1p5[12],c1p5[8],c1p4[5],s1p6[12],c1p6[8]);
fa f7(s1p5[13],c1p5[9],c1p4[6],s1p6[13],c1p6[9]);
ha h46(s1p5[14],c1p4[7],s1p6[14],c1p6[10]);
assign asn[0] = s1p6[0];
assign asn[1] = s1p6[1];
assign asn[2] = s1p6[2];
assign asn[3] = s1p6[3];
assign asn[4] = s1p6[4];
ha h47(s1p6[5],c1p6[0],asn[5],c1);
fa h48(s1p6[6],c1p6[1],c1,asn[6],c2);
fa h49(s1p6[7],c1p6[2],c2,asn[7],c3);
fa h50(s1p6[8],c1p6[3],c3,asn[8],c4);
fa h51(s1p6[9],c1p6[4],c4,asn[9],c5);
fa h52(s1p6[10],c1p6[5],c5,asn[10],c6);
fa h53(s1p6[11],c1p6[6],c6,asn[11],c7);
fa h54(s1p6[12],c1p6[7],c7,asn[12],c8);
fa h55(s1p6[13],c1p6[8],c8,asn[13],c9);
fa h56(s1p6[14],c1p6[9],c9,asn[14],c10);
ha h57(c1p6[10],c10,asn[15],c11);
endmodule

//Testbench
`timescale 1ns/1ps
module code2tb();
reg [7:0]a;
reg [7:0]b;
wire [15:0]asn;
wall8bit uut(a,b,asn);
initial
begin
a=8'b00100110;b=8'b10101011;
#5
a=8'b01110011;b=8'b10010111;
#5
$finish();
end
endmodule

//Testbench
`timescale 1ns/1ps
module code2tb();
reg [7:0]a;
reg [7:0]b;
wire [15:0]asn;
wall8bit uut(a,b,asn);
initial
begin
a=8'b00100110;b=8'b10101011;
#5
a=8'b01110011;b=8'b10010111;
#5
$finish();
end
endmodule

        """
    if bit_width == 16 and operation == "Multiplier" and type == "Wallace Tree":
        # Verilog code for 8-bit Wallace Tree
        code = """
        // Verilog code for 16-bit Wallace Tree//
        module fa(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum=a^b^cin;
assign cout=a&b|b&cin|cin&a;
endmodule
module ha(a,b,sum,cout);
input a,b;
output sum,cout;
assign sum=a^b;
assign cout=a&b;
endmodule
module wall8bit(a,b,asn);
input [7:0]a;
input [7:0]b;
output [15:0]asn;
wire [7:0] p1,p2,p3,p4,p5,p6,p7,p8;
wire [15:0] c1p1,c1p2,c1p3,c1p4,c1p5,c1p6;
wire [15:0] s1p1,s1p2,s1p3,s1p4,s1p5,s1p6;
wire c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12;
assign p1[0] = a[0]&b[0];
assign p1[1] = a[1]&b[0];
assign p1[2] = a[2]&b[0];
assign p1[3] = a[3]&b[0];
assign p1[4] = a[4]&b[0];
assign p1[5] = a[5]&b[0];
assign p1[6] = a[6]&b[0];
assign p1[7] = a[7]&b[0];
assign p2[0] = a[0]&b[1];
assign p2[1] = a[1]&b[1];
assign p2[2] = a[2]&b[1];
assign p2[3] = a[3]&b[1];
assign p2[4] = a[4]&b[1];
assign p2[5] = a[5]&b[1];
assign p2[6] = a[6]&b[1];
assign p2[7] = a[7]&b[1];
assign p3[0] = a[0]&b[2];
assign p3[1] = a[1]&b[2];
assign p3[2] = a[2]&b[2];
assign p3[3] = a[3]&b[2];
assign p3[4] = a[4]&b[2];
assign p3[5] = a[5]&b[2];
assign p3[6] = a[6]&b[2];
assign p3[7] = a[7]&b[2];
assign p4[0] = a[0]&b[3];
assign p4[1] = a[1]&b[3];
assign p4[2] = a[2]&b[3];
assign p4[3] = a[3]&b[3];
assign p4[4] = a[4]&b[3];
assign p4[5] = a[5]&b[3];
assign p4[6] = a[6]&b[3];
assign p4[7] = a[7]&b[3];
assign p5[0] = a[0]&b[4];
assign p5[1] = a[1]&b[4];
assign p5[2] = a[2]&b[4];
assign p5[3] = a[3]&b[4];
assign p5[4] = a[4]&b[4];
assign p5[5] = a[5]&b[4];
assign p5[6] = a[6]&b[4];
assign p5[7] = a[7]&b[4];
assign p6[0] = a[0]&b[5];
assign p6[1] = a[1]&b[5];
assign p6[2] = a[2]&b[5];
assign p6[3] = a[3]&b[5];
assign p6[4] = a[4]&b[5];
assign p6[5] = a[5]&b[5];
assign p6[6] = a[6]&b[5];
assign p6[7] = a[7]&b[5];
assign p7[0] = a[0]&b[6];
assign p7[1] = a[1]&b[6];
assign p7[2] = a[2]&b[6];
assign p7[3] = a[3]&b[6];
assign p7[4] = a[4]&b[6];
assign p7[5] = a[5]&b[6];
assign p7[6] = a[6]&b[6];
assign p7[7] = a[7]&b[6];
assign p8[0] = a[0]&b[7];
assign p8[1] = a[1]&b[7];
assign p8[2] = a[2]&b[7];
assign p8[3] = a[3]&b[7];
assign p8[4] = a[4]&b[7];
assign p8[5] = a[5]&b[7];
assign p8[6] = a[6]&b[7];
assign p8[7] = a[7]&b[7];
assign s1p1[0] = p1[0];
ha h0( p1[1],p2[0],s1p1[1],c1p1[0] );
fa h1(p1[2],p2[1],p3[0],s1p1[2],c1p1[1]);
fa h2(p1[3],p2[2],p3[1],s1p1[3],c1p1[2]);
fa h3(p1[4],p2[3],p3[2],s1p1[4],c1p1[3]);
fa h4(p1[5],p2[4],p3[3],s1p1[5],c1p1[4]);
fa h5(p1[6],p2[5],p3[4],s1p1[6],c1p1[5]);
fa h6(p1[7],p2[6],p3[5],s1p1[7],c1p1[6]);
ha h7(p2[7],p3[6],s1p1[8],c1p1[7]);
assign s1p1[9] = p3[7];
assign s1p2[0] = p4[0];
ha h9( p4[1],p5[0],s1p2[1],c1p2[0] );
fa h10(p4[2],p5[1],p6[0],s1p2[2],c1p2[1]);
fa h11(p4[3],p5[2],p6[1],s1p2[3],c1p2[2]);
fa h12(p4[4],p5[3],p6[2],s1p2[4],c1p2[3]);
fa h13(p4[5],p5[4],p6[3],s1p2[5],c1p2[4]);
fa h14(p4[6],p5[5],p6[4],s1p2[6],c1p2[5]);
fa h15(p4[7],p5[6],p6[5],s1p2[7],c1p2[6]);
ha h16(p5[7],p6[6],s1p2[8],c1p2[7]);
assign s1p2[9] = p6[7];
assign s1p3[0] = s1p1[0];
assign s1p3[1] = s1p1[1];
ha h17(s1p1[2],c1p1[0],s1p3[2],c1p3[0]);
fa h18(s1p1[3],c1p1[1],s1p2[0],s1p3[3],c1p3[1]);
fa h19(s1p1[4],c1p1[2],s1p2[1],s1p3[4],c1p3[2]);
fa h20(s1p1[5],c1p1[3],s1p2[2],s1p3[5],c1p3[3]);
fa h21(s1p1[6],c1p1[4],s1p2[3],s1p3[6],c1p3[4]);
fa h22(s1p1[7],c1p1[5],s1p2[4],s1p3[7],c1p3[5]);
fa h23(s1p1[8],c1p1[6],s1p2[5],s1p3[8],c1p3[6]);
fa h24(s1p1[9],c1p1[7],s1p2[6],s1p3[9],c1p3[7]);
assign s1p3[10] = s1p2[7];
assign s1p3[11] = s1p2[8];
assign s1p3[12] = s1p2[9];
assign s1p4[0] = c1p2[0];
ha h25(c1p2[1],p7[0],s1p4[1],c1p4[0]);
fa h26(c1p2[2],p7[1],p8[0],s1p4[2],c1p4[1]);
fa h27(c1p2[3],p7[2],p8[1],s1p4[3],c1p4[2]);
fa h28(c1p2[4],p7[3],p8[2],s1p4[4],c1p4[3]);
fa h29(c1p2[5],p7[4],p8[3],s1p4[5],c1p4[4]);
fa h30(c1p2[6],p7[5],p8[4],s1p4[6],c1p4[5]);
fa h31(c1p2[7],p7[6],p8[5],s1p4[7],c1p4[6]);
ha h32(p7[7],p8[6],s1p4[8],c1p4[7]);
assign s1p4[9] = p8[7];
assign s1p5[0] = s1p3[0];
assign s1p5[1] = s1p3[1];
assign s1p5[2] = s1p3[2];
ha h33(s1p3[3],c1p3[0],s1p5[3],c1p5[0]);
ha h41(s1p3[4],c1p3[1],s1p5[4],c1p5[1]);
fa h34(s1p3[5],c1p3[2],s1p4[0],s1p5[5],c1p5[2]);
fa h35(s1p3[6],c1p3[3],s1p4[1],s1p5[6],c1p5[3]);
fa h36(s1p3[7],c1p3[4],s1p4[2],s1p5[7],c1p5[4]);
fa h37(s1p3[8],c1p3[5],s1p4[3],s1p5[8],c1p5[5]);
fa h38(s1p3[9],c1p3[6],s1p4[4],s1p5[9],c1p5[6]);
fa h39(s1p3[10],c1p3[7],s1p4[5],s1p5[10],c1p5[7]);
ha h40(s1p3[11],s1p4[6],s1p5[11],c1p5[8]);
ha h42(s1p3[12],s1p4[7],s1p5[12],c1p5[9]);
assign s1p5[13] = s1p4[8];
assign s1p5[14] = s1p4[9];
assign s1p6[0] = s1p5[0];
assign s1p6[1] = s1p5[1];
assign s1p6[2] = s1p5[2];
assign s1p6[3] = s1p5[3];
ha h43(s1p5[4],c1p5[0],s1p6[4],c1p6[0]);
ha h44(s1p5[5],c1p5[1],s1p6[5],c1p6[1]);
ha h45(s1p5[6],c1p5[2],s1p6[6],c1p6[2]);
fa f1(s1p5[7],c1p5[3],c1p4[0],s1p6[7],c1p6[3]);
fa f2(s1p5[8],c1p5[4],c1p4[1],s1p6[8],c1p6[4]);
fa f3(s1p5[9],c1p5[5],c1p4[2],s1p6[9],c1p6[5]);
fa f4(s1p5[10],c1p5[6],c1p4[3],s1p6[10],c1p6[6]);
fa f5(s1p5[11],c1p5[7],c1p4[4],s1p6[11],c1p6[7]);
fa f6(s1p5[12],c1p5[8],c1p4[5],s1p6[12],c1p6[8]);
fa f7(s1p5[13],c1p5[9],c1p4[6],s1p6[13],c1p6[9]);
ha h46(s1p5[14],c1p4[7],s1p6[14],c1p6[10]);
assign asn[0] = s1p6[0];
assign asn[1] = s1p6[1];
assign asn[2] = s1p6[2];
assign asn[3] = s1p6[3];
assign asn[4] = s1p6[4];
ha h47(s1p6[5],c1p6[0],asn[5],c1);
fa h48(s1p6[6],c1p6[1],c1,asn[6],c2);
fa h49(s1p6[7],c1p6[2],c2,asn[7],c3);
fa h50(s1p6[8],c1p6[3],c3,asn[8],c4);
fa h51(s1p6[9],c1p6[4],c4,asn[9],c5);
fa h52(s1p6[10],c1p6[5],c5,asn[10],c6);
fa h53(s1p6[11],c1p6[6],c6,asn[11],c7);
fa h54(s1p6[12],c1p6[7],c7,asn[12],c8);
fa h55(s1p6[13],c1p6[8],c8,asn[13],c9);
fa h56(s1p6[14],c1p6[9],c9,asn[14],c10);
ha h57(c1p6[10],c10,asn[15],c11);
endmodule
module wall16bit (a,b,asn);
input [15:0] a;
input [15:0] b;
output [31:0] asn;
wire [15:0] in1,tmp1,tmp2,tmp3,tmp4;
wire [23:0] in2,in3;
wire [31:0] in4;
wall8bit w1(a[7:0],b[7:0],tmp1);
wall8bit w2(a[7:0],b[15:8],tmp2);
wall8bit w3(a[15:8],b[7:0],tmp3);
wall8bit w4(a[15:8],b[15:8],tmp4);
assign in1 = tmp1;
assign in2 = tmp2<<8;
assign in3 = tmp3<<8;
assign in4 = tmp4<<16;
assign asn = in1+in2+in3+in4;
endmodule

//Testbench
`timescale 1ns/1ps
module code2tb();
reg [15:0]a;
reg [15:0]b;
wire [31:0]asn;
wall16bit uut(a,b,asn);
initial
begin
a=16'b0010110101100110;b=16'b1010010001101011;
#5
a=16'b00010010001110011;b=16'b100001111110111;
#5
$finish();
end
endmodule

        """
    if bit_width == 32 and operation == "Multiplier" and type == "Wallace Tree":
        # Verilog code for 8-bit Wallace Tree
        code = """
        // Verilog code for 32-bit Wallace Tree//
        module fa(a,b,cin,sum,cout);
input a,b,cin;
output sum,cout;
assign sum=a^b^cin;
assign cout=a&b|b&cin|cin&a;
endmodule
module ha(a,b,sum,cout);
input a,b;
output sum,cout;
assign sum=a^b;
assign cout=a&b;
endmodule
module wall8bit(a,b,asn);
input [7:0]a;
input [7:0]b;
output [15:0]asn;
wire [7:0] p1,p2,p3,p4,p5,p6,p7,p8;
wire [15:0] c1p1,c1p2,c1p3,c1p4,c1p5,c1p6;
wire [15:0] s1p1,s1p2,s1p3,s1p4,s1p5,s1p6;
wire c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12;
assign p1[0] = a[0]&b[0];
assign p1[1] = a[1]&b[0];
assign p1[2] = a[2]&b[0];
assign p1[3] = a[3]&b[0];
assign p1[4] = a[4]&b[0];
assign p1[5] = a[5]&b[0];
assign p1[6] = a[6]&b[0];
assign p1[7] = a[7]&b[0];
assign p2[0] = a[0]&b[1];
assign p2[1] = a[1]&b[1];
assign p2[2] = a[2]&b[1];
assign p2[3] = a[3]&b[1];
assign p2[4] = a[4]&b[1];
assign p2[5] = a[5]&b[1];
assign p2[6] = a[6]&b[1];
assign p2[7] = a[7]&b[1];
assign p3[0] = a[0]&b[2];
assign p3[1] = a[1]&b[2];
assign p3[2] = a[2]&b[2];
assign p3[3] = a[3]&b[2];
assign p3[4] = a[4]&b[2];
assign p3[5] = a[5]&b[2];
assign p3[6] = a[6]&b[2];
assign p3[7] = a[7]&b[2];
assign p4[0] = a[0]&b[3];
assign p4[1] = a[1]&b[3];
assign p4[2] = a[2]&b[3];
assign p4[3] = a[3]&b[3];
assign p4[4] = a[4]&b[3];
assign p4[5] = a[5]&b[3];
assign p4[6] = a[6]&b[3];
assign p4[7] = a[7]&b[3];
assign p5[0] = a[0]&b[4];
assign p5[1] = a[1]&b[4];
assign p5[2] = a[2]&b[4];
assign p5[3] = a[3]&b[4];
assign p5[4] = a[4]&b[4];
assign p5[5] = a[5]&b[4];
assign p5[6] = a[6]&b[4];
assign p5[7] = a[7]&b[4];
assign p6[0] = a[0]&b[5];
assign p6[1] = a[1]&b[5];
assign p6[2] = a[2]&b[5];
assign p6[3] = a[3]&b[5];
assign p6[4] = a[4]&b[5];
assign p6[5] = a[5]&b[5];
assign p6[6] = a[6]&b[5];
assign p6[7] = a[7]&b[5];
assign p7[0] = a[0]&b[6];
assign p7[1] = a[1]&b[6];
assign p7[2] = a[2]&b[6];
assign p7[3] = a[3]&b[6];
assign p7[4] = a[4]&b[6];
assign p7[5] = a[5]&b[6];
assign p7[6] = a[6]&b[6];
assign p7[7] = a[7]&b[6];
assign p8[0] = a[0]&b[7];
assign p8[1] = a[1]&b[7];
assign p8[2] = a[2]&b[7];
assign p8[3] = a[3]&b[7];
assign p8[4] = a[4]&b[7];
assign p8[5] = a[5]&b[7];
assign p8[6] = a[6]&b[7];
assign p8[7] = a[7]&b[7];
assign s1p1[0] = p1[0];
ha h0( p1[1],p2[0],s1p1[1],c1p1[0] );
fa h1(p1[2],p2[1],p3[0],s1p1[2],c1p1[1]);
fa h2(p1[3],p2[2],p3[1],s1p1[3],c1p1[2]);
fa h3(p1[4],p2[3],p3[2],s1p1[4],c1p1[3]);
fa h4(p1[5],p2[4],p3[3],s1p1[5],c1p1[4]);
fa h5(p1[6],p2[5],p3[4],s1p1[6],c1p1[5]);
fa h6(p1[7],p2[6],p3[5],s1p1[7],c1p1[6]);
ha h7(p2[7],p3[6],s1p1[8],c1p1[7]);
assign s1p1[9] = p3[7];
assign s1p2[0] = p4[0];
ha h9( p4[1],p5[0],s1p2[1],c1p2[0] );
fa h10(p4[2],p5[1],p6[0],s1p2[2],c1p2[1]);
fa h11(p4[3],p5[2],p6[1],s1p2[3],c1p2[2]);
fa h12(p4[4],p5[3],p6[2],s1p2[4],c1p2[3]);
fa h13(p4[5],p5[4],p6[3],s1p2[5],c1p2[4]);
fa h14(p4[6],p5[5],p6[4],s1p2[6],c1p2[5]);
fa h15(p4[7],p5[6],p6[5],s1p2[7],c1p2[6]);
ha h16(p5[7],p6[6],s1p2[8],c1p2[7]);
assign s1p2[9] = p6[7];
assign s1p3[0] = s1p1[0];
assign s1p3[1] = s1p1[1];
ha h17(s1p1[2],c1p1[0],s1p3[2],c1p3[0]);
fa h18(s1p1[3],c1p1[1],s1p2[0],s1p3[3],c1p3[1]);
fa h19(s1p1[4],c1p1[2],s1p2[1],s1p3[4],c1p3[2]);
fa h20(s1p1[5],c1p1[3],s1p2[2],s1p3[5],c1p3[3]);
fa h21(s1p1[6],c1p1[4],s1p2[3],s1p3[6],c1p3[4]);
fa h22(s1p1[7],c1p1[5],s1p2[4],s1p3[7],c1p3[5]);
fa h23(s1p1[8],c1p1[6],s1p2[5],s1p3[8],c1p3[6]);
fa h24(s1p1[9],c1p1[7],s1p2[6],s1p3[9],c1p3[7]);
assign s1p3[10] = s1p2[7];
assign s1p3[11] = s1p2[8];
assign s1p3[12] = s1p2[9];
assign s1p4[0] = c1p2[0];
ha h25(c1p2[1],p7[0],s1p4[1],c1p4[0]);
fa h26(c1p2[2],p7[1],p8[0],s1p4[2],c1p4[1]);
fa h27(c1p2[3],p7[2],p8[1],s1p4[3],c1p4[2]);
fa h28(c1p2[4],p7[3],p8[2],s1p4[4],c1p4[3]);
fa h29(c1p2[5],p7[4],p8[3],s1p4[5],c1p4[4]);
fa h30(c1p2[6],p7[5],p8[4],s1p4[6],c1p4[5]);
fa h31(c1p2[7],p7[6],p8[5],s1p4[7],c1p4[6]);
ha h32(p7[7],p8[6],s1p4[8],c1p4[7]);
assign s1p4[9] = p8[7];
assign s1p5[0] = s1p3[0];
assign s1p5[1] = s1p3[1];
assign s1p5[2] = s1p3[2];
ha h33(s1p3[3],c1p3[0],s1p5[3],c1p5[0]);
ha h41(s1p3[4],c1p3[1],s1p5[4],c1p5[1]);
fa h34(s1p3[5],c1p3[2],s1p4[0],s1p5[5],c1p5[2]);
fa h35(s1p3[6],c1p3[3],s1p4[1],s1p5[6],c1p5[3]);
fa h36(s1p3[7],c1p3[4],s1p4[2],s1p5[7],c1p5[4]);
fa h37(s1p3[8],c1p3[5],s1p4[3],s1p5[8],c1p5[5]);
fa h38(s1p3[9],c1p3[6],s1p4[4],s1p5[9],c1p5[6]);
fa h39(s1p3[10],c1p3[7],s1p4[5],s1p5[10],c1p5[7]);
ha h40(s1p3[11],s1p4[6],s1p5[11],c1p5[8]);
ha h42(s1p3[12],s1p4[7],s1p5[12],c1p5[9]);
assign s1p5[13] = s1p4[8];
assign s1p5[14] = s1p4[9];
assign s1p6[0] = s1p5[0];
assign s1p6[1] = s1p5[1];
assign s1p6[2] = s1p5[2];
assign s1p6[3] = s1p5[3];
ha h43(s1p5[4],c1p5[0],s1p6[4],c1p6[0]);
ha h44(s1p5[5],c1p5[1],s1p6[5],c1p6[1]);
ha h45(s1p5[6],c1p5[2],s1p6[6],c1p6[2]);
fa f1(s1p5[7],c1p5[3],c1p4[0],s1p6[7],c1p6[3]);
fa f2(s1p5[8],c1p5[4],c1p4[1],s1p6[8],c1p6[4]);
fa f3(s1p5[9],c1p5[5],c1p4[2],s1p6[9],c1p6[5]);
fa f4(s1p5[10],c1p5[6],c1p4[3],s1p6[10],c1p6[6]);
fa f5(s1p5[11],c1p5[7],c1p4[4],s1p6[11],c1p6[7]);
fa f6(s1p5[12],c1p5[8],c1p4[5],s1p6[12],c1p6[8]);
fa f7(s1p5[13],c1p5[9],c1p4[6],s1p6[13],c1p6[9]);
ha h46(s1p5[14],c1p4[7],s1p6[14],c1p6[10]);
assign asn[0] = s1p6[0];
assign asn[1] = s1p6[1];
assign asn[2] = s1p6[2];
assign asn[3] = s1p6[3];
assign asn[4] = s1p6[4];
ha h47(s1p6[5],c1p6[0],asn[5],c1);
fa h48(s1p6[6],c1p6[1],c1,asn[6],c2);
fa h49(s1p6[7],c1p6[2],c2,asn[7],c3);
fa h50(s1p6[8],c1p6[3],c3,asn[8],c4);
fa h51(s1p6[9],c1p6[4],c4,asn[9],c5);
fa h52(s1p6[10],c1p6[5],c5,asn[10],c6);
fa h53(s1p6[11],c1p6[6],c6,asn[11],c7);
fa h54(s1p6[12],c1p6[7],c7,asn[12],c8);
fa h55(s1p6[13],c1p6[8],c8,asn[13],c9);
fa h56(s1p6[14],c1p6[9],c9,asn[14],c10);
ha h57(c1p6[10],c10,asn[15],c11);
endmodule
module wall32bit (a,b,asn);
input [31:0] a;
input [31:0] b;
output [63:0] asn;
wire [31:0] in1,tmp1,tmp2,tmp3,tmp4;
wire [47:0] in2,in3;
wire [63:0] in4;
wall16bit w12(a[15:0],b[15:0],tmp1);
wall16bit w22(a[15:0],b[31:16],tmp2);
wall16bit w33(a[31:16],b[15:0],tmp3);
wall16bit w44(a[31:16],b[31:16],tmp4);
assign in1 = tmp1;
assign in2 = tmp2<<16;
assign in3 = tmp3<<16;
assign in4 = tmp4<<32;
assign asn= in1+in2+in3+in4;
endmodule

//Testbench
`timescale 1ns/1ps
module code3tb();
reg [31:0]a;
reg [31:0]b;
wire [63:0]asn;
wall32bit uut(a,b,asn);
initial
begin
a=32'b00101010000000011111111010110011;b=32'b10100101010011001100110011010111;
#5
a=32'b00010101000000000000000001110011;b=32'b10000111111110000000000111110111;
#5
$finish();
end
endmodule
        """

    return code

def main():
    st.title("Verilog Code Generator")

    # Select bit width with unique key
    bit_width = st.selectbox("Select bit width:", [8, 16, 32], key='bit_width')

    # Select operation with unique key
    operation = st.selectbox("Select operation:", ["Adder", "Multiplier"], key='operation')

    # Select type with unique key
    if operation == "Adder":
        type = st.selectbox("Select adder type:", ["Kogge-stone", "Brent Kung"], key='adder_type')
    elif operation == "Multiplier":
        type = st.selectbox("Select multiplier type:", ["Wallace Tree"], key='multiplier_type')

    # Generate Verilog code based on selected options
    if st.button("Generate Verilog Code and its testbench"):
        verilog_code = generate_verilog_code(bit_width, operation, type)
        st.code(verilog_code, language='verilog')

if __name__ == "__main__":
    main()
