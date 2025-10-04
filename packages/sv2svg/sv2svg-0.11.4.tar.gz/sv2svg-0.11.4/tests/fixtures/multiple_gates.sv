// Multiple gates test
module multiple_gates(a, b, c, y);
  input logic a, b, c;
  output logic y;

  logic n1, n2, n3;

  AND u1(a, b, n1);
  
  OR u2(n1, c, n2);

  XOR u3(n1,n2,n3);
  NOT u4(n3, y);
endmodule
