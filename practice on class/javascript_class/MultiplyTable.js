document.write("<center><table border='1px'>");
for (var a = 1; a < 11; a++) {
  document.write("<tr style='height:40px'>");
  for (var b = 1; b < 11; b++) {
    document.write("<td style='width:40px'><center><font size='4'>" + a * b + "</center></font></td>");
  }
  document.write("</tr>");
}
document.write("</table></center>");